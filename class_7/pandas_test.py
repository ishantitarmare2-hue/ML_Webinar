import pandas as pd

d = pd.read_csv(r"C:\Users\Ishan Titarmare\Desktop\ML_Webinar\class_7\students_raw.csv")
# print(d.shape)
# print(d.head(3))

toppers = d["prev_marks"]>75
# print(d[toppers])

print((d["hours_studied"]>8).sum())

#print(d["hours_studied"]>8.sum())

#print(d[d["passed"]==1].sum())

# p = d["passed"]==1
# print('passed',p.sum())


# f = d["passed"]==0
# print('failed',f.sum())

m = (d["prev_marks"]>75)
m1 = (d["hours_studied"]>6)
good = d[m & m1]