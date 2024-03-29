import pandas as pd
import numpy as np

grades = pd.Series([87, 100, 94])
count = grades.count()
min_grade = grades.min()
max_grade = grades.max()
mean_grade = grades.mean()
std_grade = grades.std()
print(count, min_grade, max_grade, mean_grade, std_grade)
print(grades.describe())

grades_1 = pd.Series({'Wally':87, 'Eva':100, 'Sam':94})
print(grades_1.values)
