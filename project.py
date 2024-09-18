import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from datetime import datetime

events = {}
tasks = []

def save_to_dataframe(tasks):
    df = pd.DataFrame({"Tasks": tasks})
    df.to_csv("tasks.csv", index=False)


def save_events_to_dataframe(events):
    df = pd.DataFrame({"Date": list(events.keys()), "Event": list(events.values())})
    df.to_csv("events.csv", index=False)


def save_notes(notes_content):
    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_name = f"notes_{current_time}.txt"
    with open(file_name, "w") as f:
        f.write(notes_content)


def save_class_schedule(class_schedule):
    df = pd.DataFrame(class_schedule)
    df.to_csv("class_schedule.csv", index=False)


def set_background_image(image_url):
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("''' + image_url + '''");
        background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Function that runs the app
def main():
    # Set the background image
    set_background_image("https://wallpapercave.com/wp/wp5502848.jpg")
    
    # Title of the app
    st.title("Study Planner")

    # Using option_menu for navigation
    selected = option_menu("Main Menu", ["Calendar", "To-Do List", "Class Schedule", "Notes"], icons=['calendar', 'check', 'book', 'edit'])
    
    if selected == "Calendar":
        st.header("Calendar")
        st.subheader("Select Date:")
        selected_date = st.date_input("", help="Pick a date")
        event = st.text_input("Event:", "")
        if st.button("Add Event"):
            events[selected_date] = event
            st.success(f"Event '{event}' added on {selected_date}")
            save_events_to_dataframe(events)
            st.write(pd.read_csv("events.csv"))
    
    elif selected == "To-Do List":
        st.header("To-Do List")
        task = st.text_input("Task:", "")
        if st.button("Add Task"):
            tasks.append(task)
            st.success(f"Task '{task}' added")
            save_to_dataframe(tasks)
            st.write(pd.read_csv("tasks.csv"))
    
    elif selected == "Class Schedule":
        st.header("Class Schedule")
        class_schedule = []
        day = st.selectbox("Day of the Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        start_time = st.time_input("Start Time")
        end_time = st.time_input("End Time")
        class_name = st.text_input("Class Name", "")
    
        if st.button("Add Class"):
            class_info = {"Day": day, "Start Time": start_time, "End Time": end_time, "Class Name": class_name}
            class_schedule.append(class_info)
            st.success(f"Class '{class_name}' added on {day} from {start_time.strftime('%H:%M')} to {end_time.strftime('%H:%M')}")
            save_class_schedule(class_schedule)
    
    elif selected == "Notes":
        st.header("Notes")
        notes_content = st.text_area("Write your notes here:", "")
        if st.button("Save Notes"):
            save_notes(notes_content)
            st.success("Notes saved successfully!")


if __name__ == "__main__": 
    main()
