# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Output, Input

import plotly.express as px
import pandas as pd


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.read_csv("vgsales.csv")

def create_dash_application(flask_app):
    dash_app = dash.Dash(
            server = flask_app, name = "Dashboard", url_base_pathname = "/dash/")

    """fig = px.bar(df, x="Genre", y="Japan Sales")

    dash_app.layout = html.Div(
            children=[
                html.H1(children='Hello Dash'),
                html.Div(children='''
                Dash: A web application framework for your data.
                '''),
                dcc.Graph(
                    id='example-graph',
                    figure=fig
                ),
            ]
    )"""

    dash_app.layout=html.Div([
    html.H1("Graph Analysis with Charming Data"),
    dcc.Dropdown(id='genre-choice',
        options=[{'label':x, 'value':x}
            for x in sorted(df.Genre.unique())],
        value='Action'
        ),
    dcc.Graph(id='my-graph',
        figure={}),
    ])

    @dash_app.callback(
            Output(component_id='my-graph', component_property='figure'),
            Input(component_id='genre-choice', component_property='value')
    )

    def interactive_graphs(value_genre):
        print(value_genre)
        dff = df[df.Genre==value_genre]
        fig = px.bar(data_frame=dff, x='Year', y='Japan Sales', barmode="group")
        return fig
    

    return dash_app


