import pandas as pd
import plotly_express as px
import csv

path = "E:\Python\WHJR_PYTHON\cl107\data.csv"
df = pd.read_csv(path)
mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
fig = px.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")
fig.show()
