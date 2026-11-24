"""
Student Pass Predictor — our class 8 model, now as a web app.
Run locally:  streamlit run app.py
"""

import pandas as pd
import streamlit as st
from sklearn.linear_model import LogisticRegression

# ---------------------------------------------------------------- page setup
st.set_page_config(page_title="Student Pass Predictor", page_icon="🎓")

st.title("🎓 Will this student pass?")
st.write(
    "This is the logistic regression model we built in class 8, "
    "now running as a website anyone can use."
)


# ---------------------------------------------------------------- the model
# @st.cache_resource means: train this ONCE, not on every click.
@st.cache_resource
def load_model():
    students = pd.read_csv("class_9/students.csv")
    X = students[["hours_studied", "attendance", "prev_marks"]]
    y = students["passed"]
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    return model, students


model, students = load_model()


# ---------------------------------------------------------------- the inputs
st.subheader("Enter the student's details")

hours = st.slider("Hours studied", 0.0, 10.0, 5.0, step=0.1)
attendance = st.slider("Attendance %", 40, 100, 75)
prev_marks = st.slider("Previous marks", 0, 100, 60)


# ---------------------------------------------------------------- the answer
if st.button("Predict", type="primary"):

    one_student = pd.DataFrame(
        [[hours, attendance, prev_marks]],
        columns=["hours_studied", "attendance", "prev_marks"],
    )

    prediction = model.predict(one_student)[0]
    chance = model.predict_proba(one_student)[0][1]

    st.divider()

    if prediction == 1:
        st.success(f"### PASS — {chance:.1%} confident")
    else:
        st.error(f"### FAIL — {1 - chance:.1%} confident")

    st.progress(float(chance))
    st.caption(f"Chance of passing: {chance:.1%}")

    if 0.40 < chance < 0.60:
        st.warning(
            "The model is close to 50/50 here — it is honestly unsure. "
            "A hand-written if/else rule could never tell you that."
        )


# ---------------------------------------------------------------- extras
with st.expander("What did the model actually learn?"):
    weights = pd.DataFrame(
        {
            "column": ["hours_studied", "attendance", "prev_marks"],
            "weight": model.coef_[0].round(3),
        }
    )
    st.table(weights)
    st.caption(
        "These three numbers are the whole model. Careful: they are on "
        "different scales, so you cannot compare them directly."
    )

with st.expander("See the training data"):
    st.write(f"{len(students)} students")
    st.dataframe(students, height=260)

st.divider()
st.caption("Built live in class · codeWithShivah · learn.rajeevshivah.me")
