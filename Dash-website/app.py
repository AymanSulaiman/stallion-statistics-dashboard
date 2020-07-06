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
from dash.dependencies import Input, Output
# from notebook_html import notebook
import dash_bootstrap_components as dbc
import tableau_graphs as tg


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

PATH = os.path.join('..','Machine_Learning_Model_redo','total.csv')

df = pd.read_csv(PATH)

display_df = df.iloc[:,0:9]

won_svm_df = pd.read_csv('https://horse-racing-data-churchill-downs.s3.us-east-2.amazonaws.com/won_svm.csv')
won_gaussian_df = pd.read_csv('https://horse-racing-data-churchill-downs.s3.us-east-2.amazonaws.com/won_gaussian.csv')
won_xgboost_df = pd.read_csv('https://horse-racing-data-churchill-downs.s3.us-east-2.amazonaws.com/won_xgboost.csv')

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
        A web dashboard for horse racing stats
    '''),

    
    html.Div([
        html.Div([
            html.H2(children='''
            SVM Classification
            '''),
            html.H2(children='''
            Import the code here and it's score and/or classification report
            '''),
            generate_table(won_svm_df),
        ]),
        html.Div([
            html.H2(children='''
            XGBoost Classification
            '''),
            html.H2(children='''
            Import the code here and it's score and/or classification report
            '''),
            generate_table(won_xgboost_df),
        ]),
        html.Div([
            html.H2(children='''
            Naive Bayes Gaussian Classification
            '''),
            html.H2(children='''
            Import the code here and it's score and/or classification report
            '''),
            generate_table(won_gaussian_df),
        ]),
    ],style={'display': 'inline-block'}),
    

    # html.Div([

    #     html.Div([
    #         html.H3('Actual y Values'),
    #         dcc.Graph(
    #             id='fig_tvghorseweight_won',
    #             figure=fig_tvghorseweight_won
    #         ),
    #         html.H3('XGBoost'),
    #         dcc.Graph(
    #             id='fig_tvghorseweight_won_XGBoost',
    #             figure=fig_tvghorseweight_won_XGBoost
    #         )
    #     ], className="pretty_container six columns"),

    #     html.Div([
    #         html.H3('Support Vector Machine'),
    #         dcc.Graph(
    #             id='fig_tvghorseweight_won_SVM',
    #             figure=fig_tvghorseweight_won_SVM
    #         ),
    #         html.H3('Gaussian Naive-Bayes'),
    #         dcc.Graph(
    #             id='fig_tvghorseweight_won_GaussianNB',
    #             figure=fig_tvghorseweight_won_GaussianNB
    #         )
    #     ], className="pretty_container six columns")


    # ], className="flex-display row pretty-container"),


    html.H4(children='horse racing data_1'),
    generate_table(display_df, max_rows=10),
    html.H2(children='''
            Dashbooard 1
            '''),

    html.Div([
        html.Iframe(srcDoc=tg.dashboard_1, width="1600px", height="900px", style={'border':0})
    ],style={'display': 'inline-block', 'width':'auto'}),
    html.H2(children='''
            Dashboard 2
            '''),
    html.Div([
        html.Iframe(srcDoc=tg.dashboard_2, width="1600px", height="900px",style={'border':0}),  
    ]),
    html.Div([
        

        
        # html.Iframe(srcDoc=notebook,style=dict(border=0), width="100%", height="800")
    ],style={'display': 'inline-block'}),

    # html.Div([
    #         html.Iframe(srcDoc=tg.horse_racing_dashboard, width="90%", height="1000px",style={'border':0, 'align': 'center'})
    #     ]),

    
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
    ], className="flex-display row pretty-container"),
    html.H2(children='''
        Built in Python, made with ❤️
    '''),
], style={'textAlign': 'center'})



if __name__ == '__main__':
    app.run_server(debug=True)