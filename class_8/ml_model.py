"""
THE ML WAY — I write NO rule.
I hand the data to the machine and it finds the rule by itself.
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression

students = pd.read_csv("class_8/students.csv")

X = students[["hours_studied", "attendance", "prev_marks"]]   # the questions
y = students["passed"]                                        # the answers

model = LogisticRegression()
model.fit(X, y)          # <-- this one line IS the learning

correct = (model.predict(X) == y).sum()

print("Students checked :", len(students))
print("Model got right  :", correct)
print("Accuracy         :", round(correct / len(students) * 100, 1), "%")

print()
print("I never wrote a rule. Look what it figured out on its own:")
for name, weight in zip(X.columns, model.coef_[0]):
    print(f"   {name:<15} importance = {weight:+.3f}") 