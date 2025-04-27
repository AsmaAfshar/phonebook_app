import streamlit as st
import json
import os

# Load contacts
def load_contacts():
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r") as file:
            return json.load(file)
    return {}

# Save contacts
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

# Initialize
contacts = load_contacts()
st.set_page_config(page_title="📱 Phonebook", layout="centered")
st.title("📱 Stylish Phonebook App")

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Menu
menu = ["Add Contact", "Search Contact", "Delete Contact", "Display All"]
choice = st.sidebar.selectbox("📂 Menu", menu)

# 1. Add Contact
if choice == "Add Contact":
    st.subheader("➕ Add New Contact")
    with st.form(key="add_form"):
        name = st.text_input("Name")
        phone = st.text_input("Phone Number")
        submit = st.form_submit_button("Add")

        if submit and name and phone:
            contacts[name] = phone
            save_contacts(contacts)
            st.success(f"{name} added to phonebook!")

# 2. Search Contact
elif choice == "Search Contact":
    st.subheader("🔍 Search Contact")
    search_name = st.text_input("Enter name to search")
    if st.button("Search"):
        if search_name in contacts:
            st.info(f"{search_name}'s number is {contacts[search_name]}")
        else:
            st.warning(f"{search_name} not found.")

# 3. Delete Contact
elif choice == "Delete Contact":
    st.subheader("❌ Delete Contact")
    delete_name = st.text_input("Enter name to delete")
    if st.button("Delete"):
        if delete_name in contacts:
            del contacts[delete_name]
            save_contacts(contacts)
            st.success(f"{delete_name} has been deleted.")
        else:
            st.warning(f"{delete_name} not found.")

# 4. Display All Contacts
elif choice == "Display All":
    st.subheader("📇 All Contacts")
    if contacts:
        for name, phone in contacts.items():
            st.write(f"**{name}**: {phone}")
    else:
        st.info("No contacts found.")
