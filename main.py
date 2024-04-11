import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# Define some global variables
events = {}
tasks = []

# Function to save tasks to a dataframe
def save_to_dataframe(tasks):
    df = pd.DataFrame({"Tasks": tasks})
    return df

# Function to save events to a dataframe
def save_events_to_dataframe(events):
    df = pd.DataFrame({"Date": list(events.keys()), "Event": list(events.values())})
    return df

# Function to save notes 
def save_notes(notes_content):
    with open("notes.txt", "w") as f:
        f.write(notes_content)

# Function to set background image using CSS
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
    set_background_image("https://images.squarespace-cdn.com/content/v1/5e949a92e17d55230cd1d44f/ca7a4e4c-f254-42b4-a69e-3925af5547dd/Autumn+Gradients1x1.png?format=1000w")

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
            df = save_events_to_dataframe(events)
            st.write(df)

    elif selected == "To-Do List":
        st.header("To-Do List")
        task = st.text_input("Task:", "")
        if st.button("Add Task"):
            tasks.append(task)
            st.success(f"Task '{task}' added")
            df = save_to_dataframe(tasks)
            st.write(df)

    elif selected == "Class Schedule":
        st.header("Class Schedule")
        class_details = st.text_input("Class Details:", "")
        if st.button("Add Class"):
            st.write(class_details)

    elif selected == "Notes":
        st.header("Notes")
        notes_content = st.text_area("Enter your notes here:", "")
        if st.button("Save Notes"):
            save_notes(notes_content)
            st.success("Notes saved successfully")

if __name__ == "__main__":
    main()
