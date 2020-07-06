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
import notebook_html 
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

lost_svm_df = pd.read_csv('https://horse-racing-data-churchill-downs.s3.us-east-2.amazonaws.com/lost_svm.csv')
lost_gaussian_df = pd.read_csv('https://horse-racing-data-churchill-downs.s3.us-east-2.amazonaws.com/lost_gaussian.csv')
lost_xgboost_df = pd.read_csv('https://horse-racing-data-churchill-downs.s3.us-east-2.amazonaws.com/lost_xgboost.csv')

total_df = pd.read_csv('https://horse-racing-data-churchill-downs.s3.us-east-2.amazonaws.com/total.csv') 
train_df = pd.read_csv('https://horse-racing-data-churchill-downs.s3.us-east-2.amazonaws.com/train.csv')
test_df = pd.read_csv('https://horse-racing-data-churchill-downs.s3.us-east-2.amazonaws.com/test.csv')

app.layout = html.Div(children=[
    html.H1(children='Stalion Statistics'),

    html.H2(children='''
        A web dashboard for horse racing stats
    '''),

    html.Div([
        html.H4(children='horse racing data_1'),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in total_df.columns],
            data=total_df.to_dict('records'),
            style_table={
                'maxHeight': '400px',
                'overflowY': 'scroll'
            },
        )
        
    ],style={'display': 'inline-block'}),
    
    html.Div([
        html.Div([
            html.H2(children='''
            SVM Classification
            '''),
            html.Iframe(srcDoc=notebook_html.svm, width="600px", height="700px", style={'border':0}),
            html.H3(children=f'''
            SVM Correct Winning Prediction
            Count: {len(won_svm_df)}
            '''),
            dash_table.DataTable(
                id='table1_won',
                columns=[{"name": i, "id": i} for i in won_svm_df.columns],
                data=won_svm_df.to_dict('records'),
                style_table={
                'maxHeight': '400px',
                'overflowY': 'scroll'
                },
            ),
            
            html.H3(children=f'''
            SVM Correct Loosing Prediction
            Count: {len(lost_svm_df)}
            '''),
            dash_table.DataTable(
                id='table1_lost',
                columns=[{"name": i, "id": i} for i in lost_svm_df.columns],
                data=lost_svm_df.to_dict('records'),
                style_table={
                'maxHeight': '400px',
                'overflowY': 'scroll'
                },
            ),
            
        ]),
        html.Div([
            html.H2(children='''
            XGBoost Classification
            '''),
            html.H2(children='''
            Import the code here and it's score and/or classification report
            '''),
            html.Iframe(srcDoc=notebook_html.xgboost,width="480px", height="920px", style={'border':0}),
            html.H3(children=f'''
            XGBoost Correct Winning Prediction
            Count: {len(won_xgboost_df)}
            '''),
            dash_table.DataTable(
                id='table2_won',
                columns=[{"name": i, "id": i} for i in won_xgboost_df.columns],
                data=won_xgboost_df.to_dict('records'),
                style_table={
                'maxHeight': '400px',
                'overflowY': 'scroll'
                },
            ),
            html.H3(children=f'''
            XGBoost Correct Loosing Prediction
            Count: {len(lost_xgboost_df)}
            '''),
            dash_table.DataTable(
                id='table2_lost',
                columns=[{"name": i, "id": i} for i in lost_xgboost_df.columns],
                data=lost_xgboost_df.to_dict('records'),
                style_table={
                'maxHeight': '400px',
                'overflowY': 'scroll'
                },
            ),
        ]),
        html.Div([
            html.H2(children='''
            Naive Bayes Gaussian Classification
            '''),
            html.H2(children='''
            Import the code here and it's score and/or classification report
            '''),
            html.Iframe(srcDoc=notebook_html.gaussian,width="480px", height="920px", style={'border':0}),
            html.H3(children=f'''
            Naive-Bayes Correct Winning Prediction
            Count: {len(won_gaussian_df)}
            '''),
            dash_table.DataTable(
                id='table3_won',
                columns=[{"name": i, "id": i} for i in won_gaussian_df.columns],
                data=won_gaussian_df.to_dict('records'),
                style_table={
                'maxHeight': '400px',
                'overflowY': 'scroll'
                },
            ),
            html.H3(children=f'''
            Naive-Bayes Correct Loosing Prediction
            Count: {len(lost_gaussian_df)}
            '''),dash_table.DataTable(
                id='table3_lost',
                columns=[{"name": i, "id": i} for i in lost_gaussian_df.columns],
                data=lost_gaussian_df.to_dict('records'),
                style_table={
                'maxHeight': '400px',
                'overflowY': 'scroll'
                },
            ),
        ]),
    ],style={'display': 'inline-block'}),
    

    
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
            ),

            html.Br(),

            html.A(children='''
            GitHub
            ''', 
            href='''
            https://github.com/AymanSulaiman
            ''',
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
            ''' ,
            target='_blank'
            ),

            html.Br(),

            html.A(children='''
            GitHub
            ''', 
            href='''
            https://github.com/hharutyunyan1
            ''',
            target='_blank'
            ) 

        ], className="pretty_container six columns")
    ], className="flex-display row pretty-container"),
    html.H2(children='''
        Built in Python, made with ❤️
    '''),
], style={'textAlign': 'center'})



if __name__ == '__main__':
    app.run_server(debug=True)