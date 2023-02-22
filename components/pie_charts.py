from dash import Dash, html, dcc
import plotly.express as px
from utill import get_comments, get_rate

def render(app):
    df = get_comments()
    fig = px.pie(df, values = 'total_comments', names = "index", title = 'Total Comments')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart")

def render1(app):
    df = get_rate()
    fig = px.pie(df, values = 'review_rating', names = "index", title = 'Review Rating')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart1")