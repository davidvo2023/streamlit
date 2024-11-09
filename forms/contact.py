import re
import json
import streamlit as st

def is_valid_email(email):
    # Basic regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def save_to_json(data, filename="contact_form_submissions.json"):
    # Append the data to a JSON file
    try:
        with open(filename, "a") as file:
            json.dump(data, file)
            file.write("\n")  # Write each submission on a new line
    except Exception as e:
        st.error(f"Error saving to file: {e}", icon="⚠️")

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        # Validate the inputs
        if not name:
            st.error("Please provide your name.", icon="🧑")
            st.stop()

        if not email:
            st.error("Please provide your email address.", icon="📨")
            st.stop()

        if not is_valid_email(email):
            st.error("Please provide a valid email address.", icon="📧")
            st.stop()

        if not message:
            st.error("Please provide a message.", icon="💬")
            st.stop()

        # Prepare the data payload
        data = {"email": email, "name": name, "message": message}

        # Save the data to a JSON file
        save_to_json(data)

        # Success message
        st.success("Your message has been saved successfully! 🎉", icon="🚀")
