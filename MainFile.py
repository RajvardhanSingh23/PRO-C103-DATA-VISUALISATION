import plotly.express as px
import pandas as pd
df = pd.read_csv("D:/projects_vansh/module3/PROJ103/data.csv")
fig = px.line(df,x="country",y = "cases",color = "date",title = "Per Capita Income")
fig.show()