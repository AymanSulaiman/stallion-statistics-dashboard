# -*- coding: utf-8 -*-
import dash
import os
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import ml_outputs as mo
from dash.dependencies import Input, Output
from notebook_html import notebook
import dash_bootstrap_components as dbc
import tableau_graphs as tg


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])

df = pd.read_csv('cleaned_tvg_cd_data.csv')

display_df = df[
    ['horsename',
     'tvghorseweight',      
     'tvghorseage',         
     'tvghorsedaysoff',     
     'tvghorsenumberofwins',
     'tvghorsepowerrating',
     'tvghorseaverageclassrating',
     'tvghorseaveragespeed',
     'winpayoutbinary']
]

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

fig_example_1 = go.Figure()

fig_example_1.add_trace(go.Scatter(x=x, y=y,
                    mode='markers',
                    name='power, speed'))

fig_example_1.add_trace(go.Scatter(x=x, y=(x*m)+c,
                    mode='lines',
                    name='Line of best fit'))

fig_example_1.update_layout(
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
            ], style={'align': 'center'}) for i in range(min(len(dataframe), max_rows))
        ], style={'align': 'center'})
    ], style={'align': 'center'})


app.layout = html.Div(children=[
    html.H1(children='Stalion Statistics'),

    html.H2(children='''
        A web dashboard for horse racing stats.
    '''),

    html.H2(children='''
        Built in Python, made with ❤️
    '''),


    html.Div([

        html.Div([
            html.H3('column 1'),
            dcc.Graph(
                id='example-graph-1',
                figure=fig_example_1
            )
        ], className="pretty_container six columns"),

        html.Div([
            html.H3('column 2'),
            dcc.Graph(
                id='example-graph',
                figure=fig_example
            )
        ], className="pretty_container six columns")


    ], className="flex-display row pretty-container"),


    html.H4(children='horse racing data_1'),
    generate_table(display_df, max_rows=10),

    html.Div([
        html.Div([
            html.Iframe(srcDoc=tg.beyer_one_ranking, width="100%", height="900", style={'border':0})
        ], className="pretty_container six columns"),

        html.Div([
            html.Iframe(srcDoc=tg.avg_horse_power, width="100%", height="900",style={'border':0}),  
        ], className="pretty_container six columns"),

        
        # html.Iframe(srcDoc=notebook,style=dict(border=0), width="100%", height="800")
    ], className="flex-display row pretty-container"),

    html.Div([
            html.Iframe(srcDoc=tg.horse_racing_dashboard, width="90%", height="1000px",style={'border':0, 'align': 'center'})
        ]),

    
    html.Div([
        html.Div([

            html.H2(children='''
            Syed Ayman Sulaiman
            '''),

            html.A(children='''
            LinkedIn
            ''',
            href='https://www.linkedin.com/in/s-ayman-sulaiman',
            target='_blank'),

            html.Br(),

            html.A(children='''
            Resume
            ''', 
            href='https://drive.google.com/file/d/1NXci3kPUlxHqQ8PDRxlInGBnUZYTSNlp/view?usp=sharing',
            target='_blank'
            )
        ], className="pretty_container six columns"),

        html.Div([
            html.H2(children='''
            Hakob Harutyunyan
            '''),

            html.A(children = '''
            LinkedIn
            ''',
            href='''
            https://www.linkedin.com/in/hakob-harutyunyan-4a7360199/
            ''' 
            ) 

        ], className="pretty_container six columns")
    ], className="flex-display row pretty-container")
], style={'textAlign': 'center'})



if __name__ == '__main__':
    app.run_server(debug=True)