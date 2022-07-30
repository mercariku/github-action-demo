import plotly.express as px
import pandas as pd
df = px.data.tips()
print(df)
fig = px.treemap(df, path=[px.Constant("all"), 'sex', 'day', 'time'], 
                 values='total_bill', color='day')
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()