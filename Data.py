import pandas as pd
import plotly.express as px
path = "E:\Python\WHJR_PYTHON\cl103\Copy+of+data+-+data (1).csv"
df = pd.read_csv(path)
fig = px.scatter(df, x="date", y="cases", color="country", size_max=60)
fig.show()