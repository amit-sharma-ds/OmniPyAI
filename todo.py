import streamlit as st

st.header("📝 To-Do List")

if 'tasks' not in st.session_state:
    st.session_state.tasks = []

new_task = st.text_input("Add a new task:")

if st.button("➕ Add Task"):
    if new_task:
        st.session_state.tasks.append({"task": new_task, "done": False})
        st.success("Task added!")
    else:
        st.warning("Please enter a task.")

if st.session_state.tasks:
    st.subheader("📋 Your Tasks")
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.1, 0.9])
        if col1.checkbox("", value=task["done"], key=f"task_{i}"):
            st.session_state.tasks[i]["done"] = True
        col2.text(task["task"])
else:
    st.info("No tasks yet.")
