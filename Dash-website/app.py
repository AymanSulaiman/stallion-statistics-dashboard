# -*- coding: utf-8 -*-
import dash
import os
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import ml_outputs as mo
from dash.dependencies import Input, Output
from notebook_html import notebook
import dash_bootstrap_components as dbc


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('cleaned_tvg_cd_data.csv')

features = [
    'tvghorseweight',            # 0
    'tvghorseage',               # 1
    'tvghorsedaysoff',           # 2
    'tvghorsenumberofwins',      # 3
    'tvghorsepowerrating',       # 4
    'tvghorseaverageclassrating' # 5
]

target = 'tvghorseaveragespeed'
x = df[features[4]]
y = df[target]

m, c = np.polyfit(x, y, 1)

fig_example = go.Figure()

fig_example.add_trace(go.Scatter(x=x, y=y,
                    mode='markers',
                    name='power, speed'))

fig_example.add_trace(go.Scatter(x=x, y=(x*m)+c,
                    mode='lines',
                    name='Line of best fit'))

fig_example.update_layout(
            title="Power and speed of horse",
            xaxis_title="Power",
            yaxis_title="Speed",
            font=dict(
                family="Courier New, monospace",
                size=16,
                color="#7f7f7f"
            )
)

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])



app.layout = html.Div(children=[
    html.H1(children='Stalion Statistics'),

    html.H2(children='''
        A web dashboard for horse racing stats.
    '''),

    html.H2(children='''
        Built in Python, made with ❤️
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig_example
    ),


    html.H4(children='horse racing data'),
    generate_table(df),

    html.Iframe(srcDoc=notebook,style=dict(border=0), width="100%", height="800")
])



if __name__ == '__main__':
    app.run_server(debug=True)


# assume you have a "wide-form" data frame with no index
# see https://plotly.com/python/wide-form/ for more options
# df = pd.DataFrame({"x": [1, 2, 3], "SF": [4, 1, 2], "Montreal": [2, 4, 5]})

# fig = px.bar(df, x="x", y=["SF", "Montreal"], barmode="group")

# app.layout = html.Div(children=[
#     html.H1(children='Hello Dash'),

#     html.Div(children='''
#         Dash: A web application framework for Python.
#     '''),

#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)