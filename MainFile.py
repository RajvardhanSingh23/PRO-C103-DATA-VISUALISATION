import plotly.express as px
import pandas as pd
df = pd.read_csv('data.csv')
fig = px.line(df,x="country",y = "cases",color = "date",title = "Per Capita Income")
fig.show()
