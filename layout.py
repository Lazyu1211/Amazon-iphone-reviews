from dash import Dash,html
import dash_bootstrap_components as dbc
from components import pie_charts, bar_charts

image_path = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyFWFy7uWeLPCugDhn3_hSud_H83s8ksj8kA&usqp=CAU"
image_path1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuyipVQhNHORf_fvMzDk2HhVWzaxb9px23Vw&usqp=CAU"

def create_layout(app):
    return dbc.Container(children=[
        dbc.Row([
        html.P(children="🛒🛒🛒🛒🛒🛒🛍️🛍️🛍️🛍️🛍️🛍️✨✨✨✨✨✨✨✨✨", className="header-emoji"),
        html.H1(
                "Amazon iPhone 11 Reviews Analysis", className="header-title"
              ),
        html.P(
                "Base on the dataset we can analysis Amazon iPhone 11 Reviews!!!🔥🔥🔥✨✨✨",
                className="header-description",
                ),
        html.Img(src=image_path, style={"width": "660px", "height": "400px"}),
        html.Img(src=image_path1, style={"width": "660px", "height": "400px"})     
,       
    ],className="mt-4"),
        dbc.Row([
            dbc.Col(pie_charts.render(app),lg=6),
            dbc.Col(pie_charts.render1(app),lg=6),
            dbc.Col(bar_charts.render(app),lg=6),
            dbc.Col(bar_charts.render1(app),lg=6)
        ],className="mt-4")
    ])