from dash import Dash, html, dcc
from dash.dependencies import Output,Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_text, get_title

def render(app):
    df = get_text()
    fig = px.bar(
                df,
                x="index",
                y="review_text",
                title="Top 10 review text")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume")

def render1(app):
    df = get_title()
    fig = px.bar(
                df,
                x="index",
                y="review_title",
                title="Top 10 review title")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume1")
