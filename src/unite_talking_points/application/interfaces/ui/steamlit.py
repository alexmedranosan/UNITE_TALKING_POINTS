import streamlit as st
from src.unite_talking_points.application.interfaces.console.console_app import main  # Import your main function from your module

def main_streamlit():
    st.title("Chat Interface")
    st.write("Welcome to the chat interface!")

    st.sidebar.title("Navigation")
    choices = ["Home", "Run Chat Interface"]
    selected_choice = st.sidebar.radio("Select an option", choices)

    if selected_choice == "Home":
        st.write("This is the home page. Use the sidebar to navigate.")

    elif selected_choice == "Run Chat Interface":
        st.write("Running the chat interface...")
        main()  # Call your main function here

if __name__ == "__main__":
    main_streamlit()
