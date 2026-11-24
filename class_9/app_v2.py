import streamlit as st

st.title("🎓 Will this student pass?")

hours = st.slider("Hours studied", 0.0, 10.0, 5.0, step=0.1)
attendance = st.slider("Attendance %", 40, 100, 75)
prev_marks = st.slider("Previous marks", 0, 100, 60)

st.write("You chose:", hours, attendance, prev_marks)
