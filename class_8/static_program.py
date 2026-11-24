"""
THE OLD WAY — a normal program.
I look at the data, I think hard, and I WRITE THE RULE MYSELF.
"""

import pandas as pd

students = pd.read_csv("class_8/students.csv")


# This is the rule. I invented it. It came out of my head, not out of the data.
def will_pass(hours_studied, attendance, prev_marks):
    if hours_studied >= 5 and attendance >= 75:
        return 1
    return 0


# Let's see how often my rule is right.
correct = 0

for _, row in students.iterrows():
    my_answer = will_pass(row.hours_studied, row.attendance, row.prev_marks)
    real_answer = row.passed
    if my_answer == real_answer:
        correct += 1

print("Students checked :", len(students))
print("My rule got right:", correct)
print("Accuracy         :", round(correct / len(students) * 100, 1), "%")
