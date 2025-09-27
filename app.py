import streamlit as st
from database import init_db, get_employees, add_employee, apply_leave, get_leaves, update_leave
from chatbot import setup_gemini, ask_gemini
from utils import apply_css, load_policy_texts
from chatbot import build_vector_store



# Load policy document
policy_chunks = load_policy_texts("data/Sample_HR_Policy.txt")
index, embeddings, policy_texts = build_vector_store(policy_chunks)

# ----------------- Setup -----------------
init_db()
theme = st.sidebar.radio("🌈 Choose Theme", ["Light", "Dark", "Custom"])
title_color, subtitle_color = apply_css(theme)

# Title
st.markdown(f"<h1 style='text-align: center; color:{title_color};'>ABDUL.ai</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; font-size:18px; color:{subtitle_color};'>HR Assistant with Chatbot</p>", unsafe_allow_html=True)

# Load Gemini
model = setup_gemini(st.secrets["GOOGLE_API_KEY"])

# ----------------- Tabs -----------------
tab1, tab2, tab3 = st.tabs(["💬 Chatbot", "👥 Employees", "📝 Leaves"])

# 💬 Chatbot
with tab1:
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for msg in st.session_state.messages:
        role = "user" if msg["role"] == "user" else "bot"
        st.markdown(f"<div class='message {role}'>{msg['content']}</div>", unsafe_allow_html=True)

    def send_message():
        user_msg = st.session_state.chat_input.strip()
        if not user_msg:
            return
        st.session_state.messages.append({"role": "user", "content": user_msg})
        reply = ask_gemini(model, user_msg, index=index, policy_texts=policy_texts)
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.session_state.chat_input = ""
        st.rerun()

    st.text_input("Type a message...", key="chat_input", label_visibility="collapsed", on_change=send_message)

# 👥 Employees
with tab2:
    st.subheader("Add Employee")
    with st.form("emp_form"):
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        department = st.text_input("Department")
        position = st.text_input("Position")
        date_of_hire = st.date_input("Date of Hire")
        salary = st.number_input("Salary", min_value=0.0)
        address = st.text_area("Address")
        if st.form_submit_button("Add Employee"):
            add_employee((first_name,last_name,email,phone,department,position,str(date_of_hire),salary,address))
            st.success("✅ Employee added!")

    st.subheader("Employee List")
    st.table(get_employees())

# 📝 Leaves
with tab3:
    st.subheader("Apply Leave")
    with st.form("leave_form"):
        emp_id = st.number_input("Employee ID", min_value=1, step=1)
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date")
        reason = st.text_area("Reason")
        if st.form_submit_button("Apply"):
            apply_leave(emp_id, str(start_date), str(end_date), reason)
            st.success("✅ Leave applied!")

    st.subheader("Leaves List")
    leaves = get_leaves()
    st.table(leaves)

    leave_id = st.number_input("Leave ID to update", min_value=1, step=1)
    action = st.radio("Action", ["Approved", "Rejected"])
    if st.button("Update Leave"):
        update_leave(leave_id, action)
        st.success(f"Leave {action}!")
