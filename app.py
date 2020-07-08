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
# import dash_bootstrap_components as dbc
import tableau_graphs as tg


# external_stylesheets = ['https://raw.githubusercontent.com/plotly/dash-sample-apps/master/apps/dash-oil-and-gas/assets/s1.css']
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

total_df = pd.read_csv('https://horse-racing-data-churchill-downs.s3.us-east-2.amazonaws.com/total.csv')

svm_mw_aw_df = pd.read_csv('https://horse-racing-data-churchill-downs.s3.us-east-2.amazonaws.com/svm_mw_aw.csv')
svm_ml_aw_df = pd.read_csv('https://horse-racing-data-churchill-downs.s3.us-east-2.amazonaws.com/svm_ml_aw.csv')
svm_mw_al_df = pd.read_csv('https://horse-racing-data-churchill-downs.s3.us-east-2.amazonaws.com/svm_mw_al.csv')
svm_ml_al_df = pd.read_csv('https://horse-racing-data-churchill-downs.s3.us-east-2.amazonaws.com/svm_ml_al.csv')

xgb_mw_aw_df = pd.read_csv('https://horse-racing-data-churchill-downs.s3.us-east-2.amazonaws.com/xgb_mw_aw.csv')
xgb_ml_aw_df = pd.read_csv('https://horse-racing-data-churchill-downs.s3.us-east-2.amazonaws.com/xgb_ml_aw.csv')
xgb_mw_al_df = pd.read_csv('https://horse-racing-data-churchill-downs.s3.us-east-2.amazonaws.com/xgb_mw_al.csv')
xgb_ml_al_df = pd.read_csv('https://horse-racing-data-churchill-downs.s3.us-east-2.amazonaws.com/xgb_ml_al.csv')

nb_mw_aw_df = pd.read_csv('https://horse-racing-data-churchill-downs.s3.us-east-2.amazonaws.com/nb_mw_aw.csv')
nb_ml_aw_df = pd.read_csv('https://horse-racing-data-churchill-downs.s3.us-east-2.amazonaws.com/nb_ml_aw.csv')
nb_mw_al_df = pd.read_csv('https://horse-racing-data-churchill-downs.s3.us-east-2.amazonaws.com/nb_mw_al.csv')
nb_ml_al_df = pd.read_csv('https://horse-racing-data-churchill-downs.s3.us-east-2.amazonaws.com/nb_ml_al.csv')


app.layout = html.Div(children=[
    html.Div(
        html.Img(src='https://horse-racing-data-churchill-downs.s3.us-east-2.amazonaws.com/stallion_statistics_logo.png',style={'height':'30%', 'width':'30%'})
    ),

    # html.H1(children='Stallion Statistics'),

    # html.H2(children='''
    #     A web dashboard for horse racing stats
    # '''),

    html.H4(children='Data'),

    html.Div([
        
        dash_table.DataTable(
            id='table_total',
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
            html.Iframe(srcDoc=notebook_html.svm, width="800px", height="860px", style={'border':0},className="pretty_container"),
            html.Br(),
            html.H3(children=f'''
            SVM Correct Winning Prediction and Actual
            Count: {len(svm_mw_aw_df)}
            '''),
            html.Br(),
            dash_table.DataTable(
                id='svm_mw_aw_df',
                columns=[{"name": i, "id": i} for i in svm_mw_aw_df.columns],
                data=svm_mw_aw_df.to_dict('records'),
                style_table={
                'maxHeight': '400px',
                'overflowY': 'scroll'
            },  
            ),
            html.Br(),
            html.H3(children=f'''
            SVM Incorrect Winning Prediction and Actual
            Count: {len(svm_mw_al_df)}
            '''),
            html.Br(),
            dash_table.DataTable(
                id='svm_mw_al_df',
                columns=[{"name": i, "id": i} for i in svm_mw_al_df.columns],
                data=svm_mw_al_df.to_dict('records'),
                style_table={
                'maxHeight': '400px',
                'overflowY': 'scroll'
            },  
            ),
            html.Br(),
            html.H3(children=f'''
            SVM Incorrect Losing Prediction and Actual
            Count: {len(svm_ml_aw_df)}
            '''),
            html.Br(),
            dash_table.DataTable(
                id='svm_ml_aw_df',
                columns=[{"name": i, "id": i} for i in svm_ml_aw_df.columns],
                data=svm_ml_aw_df.to_dict('records'),
                style_table={
                'maxHeight': '400px',
                'overflowY': 'scroll'
            },  
            ),
            html.Br(),
            html.H3(children=f'''
            SVM Correct Loosing Prediction and Actual
            Count: {len(svm_ml_al_df)}
            '''),
            html.Br(),
            dash_table.DataTable(
                id='svm_ml_al_df',
                columns=[{"name": i, "id": i} for i in svm_ml_al_df.columns],
                data=svm_ml_al_df.to_dict('records'),
                style_table={
                'maxHeight': '400px',
                'overflowY': 'scroll'
                },
            ),
            
        ], style={'textAlign': 'center'}),
        html.Br(),
        html.Div([
            html.H2(children='''
            XGBoost Classification
            '''),
            html.Br(),
            html.Iframe(srcDoc=notebook_html.xgboost,width="800px", height="850px", style={'border':0}),
            html.Br(),
            html.H3(children=f'''
            XGBoost Correct Winning Prediction and Actual
            Count: {len(xgb_mw_aw_df)}
            '''),
            html.Br(),
            dash_table.DataTable(
                id='xgb_mw_aw_df',
                columns=[{"name": i, "id": i} for i in xgb_mw_aw_df.columns],
                data=xgb_mw_aw_df.to_dict('records'),
                style_table={
                'maxHeight': '400px',
                'overflowY': 'scroll'
                },
            ),
            html.Br(),
            html.H3(children=f'''
            XGBoost Incorrect Winning Prediction and Actual
            Count: {len(xgb_mw_al_df)}
            '''),
            html.Br(),
            dash_table.DataTable(
                id='xgb_mw_al_df',
                columns=[{"name": i, "id": i} for i in xgb_mw_al_df.columns],
                data=xgb_mw_al_df.to_dict('records'),
                style_table={
                'maxHeight': '400px',
                'overflowY': 'scroll'
                },
            ),
            html.Br(),
            html.H3(children=f'''
            XGBoost Incorrect Losing Prediction and Actual
            Count: {len(xgb_ml_aw_df)}
            '''),
            html.Br(),
            dash_table.DataTable(
                id='xgb_ml_aw_df',
                columns=[{"name": i, "id": i} for i in xgb_ml_aw_df.columns],
                data=xgb_ml_aw_df.to_dict('records'),
                style_table={
                'maxHeight': '400px',
                'overflowY': 'scroll'
                },
            ),
            html.Br(),
            html.H3(children=f'''
            XGBoost Correct Loosing Prediction and Actual
            Count: {len(xgb_ml_al_df)}
            '''),
            html.Br(),
            dash_table.DataTable(
                id='table2_lost',
                columns=[{"name": i, "id": i} for i in xgb_ml_al_df.columns],
                data=xgb_ml_al_df.to_dict('records'),
                style_table={
                'maxHeight': '400px',
                'overflowY': 'scroll'
                },
            ),
        ]),
        html.Br(),
        html.Br(),
        html.Div([
            html.H2(children='''
            Naive Bayes Gaussian Classification
            '''),
            html.Br(),
            html.Iframe(srcDoc=notebook_html.gaussian,width="800px", height="820px", style={'border':0}),
            html.Br(),
            html.H3(children=f'''
            Naive-Bayes Correct Winning Prediction
            Count: {len(nb_mw_aw_df)}
            '''),
            html.Br(),
            dash_table.DataTable(
                id='nb_mw_aw_df',
                columns=[{"name": i, "id": i} for i in nb_mw_aw_df.columns],
                data=nb_mw_aw_df.to_dict('records'),
                style_table={
                'maxHeight': '400px',
                'overflowY': 'scroll'
                },
            ),
            html.Br(),
            html.H3(children=f'''
            Naive-Bayes Incorrect Winning Prediction and Actual
            Count: {len(nb_mw_al_df)}
            '''),
            html.Br(),
            dash_table.DataTable(
                id='nb_mw_al_df',
                columns=[{"name": i, "id": i} for i in nb_mw_al_df.columns],
                data=nb_mw_al_df.to_dict('records'),
                style_table={
                'maxHeight': '400px',
                'overflowY': 'scroll'
                },
            ),
            html.Br(),
            html.H3(children=f'''
            Naive-Bayes Incorrect Lossing Prediction and Acutal
            Count: {len(nb_ml_aw_df)}
            '''),
            html.Br(),
            dash_table.DataTable(
                id='nb_ml_aw_df',
                columns=[{"name": i, "id": i} for i in nb_ml_aw_df.columns],
                data=nb_ml_aw_df.to_dict('records'),
                style_table={
                'maxHeight': '400px',
                'overflowY': 'scroll'
                },
            ),
            html.Br(),
            html.H3(children=f'''
            Naive-Bayes Correct Loosing Prediction
            Count: {len(nb_ml_al_df)}
            '''),dash_table.DataTable(
                id='nb_ml_al_df',
                columns=[{"name": i, "id": i} for i in nb_ml_al_df.columns],
                data=nb_ml_al_df.to_dict('records'),
                style_table={
                'maxHeight': '400px',
                'overflowY': 'scroll'
                },
            ),
        ]),
    ],style={'display': 'inline-block'}),
    

    html.Br(),
    html.H2(children='''
            Dashboard 1
            '''),

    html.Br(),
    html.Div([
        html.Iframe(srcDoc=tg.new_dashboard_1, width="1600px", height="900px", style={'border':0})
    ],style={'display': 'inline-block', 'width':'auto'}),
    html.Br(),
    html.H2(children='''
            Dashboard 2
            '''),
    html.Br(),
    html.Div([
        html.Iframe(srcDoc=tg.new_dashboard_2, width="1600px", height="900px",style={'border':0}),  
    ]),
    html.Br(),
    
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
            href='https://drive.google.com/file/d/1o238OMrOX6QuVs-fZ9jS4YN77rKIAWFC/view?usp=sharing',
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
            ),

            html.H2(children='''
            Andrew Wright
            '''),

            html.A(children='''
            LinkedIn
            ''',
            href='https://www.linkedin.com/in/aesdub/',
            target='_blank'),

            html.Br(),

            html.A(children='''
            GitHub
            ''', 
            href='''
            https://github.com/AESDUB
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
            ), 
            html.H2(children='''
            Aldo Garcia
            '''),

            html.A(children = '''
            LinkedIn
            ''',
            href='''
            https://www.linkedin.com/in/aldo-garcia-02/
            ''' ,
            target='_blank'
            ),

            html.Br(),

            html.A(children='''
            GitHub
            ''', 
            href='''
            #
            ''',
            target='_blank'
            ), 

        ], className="pretty_container six columns")
    ], className="flex-display row pretty-container"),
    html.Br(),

    html.A(children='''
        GitHub Repo
        ''', 
        href='''
        https://github.com/AymanSulaiman/stallion-statistics-dashboard
        ''',
        target='_blank'
    ),
    
    html.H2(children='''
        Built in Python, made with ❤️
    '''),

], style={'textAlign': 'center'})



if __name__ == '__main__':
    app.run_server(debug=True)