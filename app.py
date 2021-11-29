import os
import pathlib

import dash
from dash.html.Font import Font
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Input, Output, State
import dash_table
import plotly.graph_objs as go

import pandas as pd


app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
app.title = "Big 6 Stocks - Dashboard"
server = app.server
app.config["suppress_callback_exceptions"] = True

APP_PATH = str(pathlib.Path(__file__).parent.resolve())
stocks_df = px.data.stocks()
stocks_df['date'] = pd.to_datetime(stocks_df['date'])
stocks_df['year'] = stocks_df['date'].dt.year
stocks_df['month'] = stocks_df['date'].dt.month
stocks_df['quarter'] = stocks_df['date'].dt.quarter

first_graph = px.line(stocks_df,x='date',y=['GOOG', 'AAPL', 'AMZN', 'FB', 'NFLX', 'MSFT'],template='plotly_dark')

def filter_time(stocks_df, year, month= None):
    stocks= stocks_df[stocks_df['year']==year]
    if month != None:
        stocks= stocks[stocks['month']==month]
    return stocks


def fourth_graph_data(stocks_df, company_name, year, month= None): 
    stocks= stocks_df[stocks_df['year']==year]
    if month != None:
        stocks= stocks[stocks['month']==month]
    return stocks[['date', company_name]]


def build_banner():
    return html.Div(
        id="banner",
        className="banner",
        children=[
            html.Div(
                id="banner-text",
                children=[
                    html.H5("Big 6 Stocks - Dashboard"),
                ],
            ),
        ],
    )

def build_big_numbers():
    return html.Div(
        className="row",
        children=[
                html.Div(
                    className="card two columns",
                    children=[html.H2("Google"),html.H3("$ "+str(round(stocks_df["GOOG"].max(),3)))]),
                html.Div(
                    className="card two columns",
                    children=[html.H2("Apple"),html.H3("$ "+str(round(stocks_df["AAPL"].max(),3)))]),
                html.Div(
                    className="card two columns",
                    children=[html.H2("Amazon"),html.H3("$ "+str(round(stocks_df["AMZN"].max(),3)))]),
                html.Div(
                    className="card two columns",
                    children=[html.H2("Facebook"),html.H3("$ "+str(round(stocks_df["FB"].max(),3)))]),
                html.Div(
                    className="card two columns",
                    children=[html.H2("Neflix"),html.H3("$ "+str(round(stocks_df["NFLX"].max(),3)))]),
                html.Div(
                    className="card two columns",
                    children=[html.H2("Microsoft"),html.H3("$ "+str(round(stocks_df["MSFT"].max(),3)))]),
                ],
                
    )

def build_first_graph():
    return html.Div(
        id="graphs-container",
        className="row",
        children=[
                generate_section_banner("Overall Stock Performance"),
                dcc.Graph(figure=first_graph),
                ],
    )

def build_second_graph():
    return html.Div(
        id="second-graphs-container",
        className="two columns",
        children=[
                generate_section_banner("Stock Performance for each company"),
                html.Div([
                dcc.Dropdown(className="three columns", id='stocks-drop-down',options=[{'label':k,'value':k} for k in px.data.stocks().columns[1:]],placeholder='Choose a stock ...',value=None),
                dcc.Dropdown(className="three columns", id='year-drop-down',options=[{'label':k,'value':k} for k in stocks_df['year'].unique()],placeholder='Choose a year ...',value=None),
                dcc.Dropdown(className="three columns", id='month-drop-down',options=[{'label':k,'value':k} for k in stocks_df['month'].unique()],placeholder='Choose a month ...',value=None),
                # html.Button(id='second-graph-submit-button',children='Submit'),
                ],className="row"),
                dcc.Graph(id='second-figure',figure={}),
                ],
                
    )

def build_third_graph():
    return html.Div(
        id="third-graphs-container",
        className="two columns",
        children=[
                generate_section_banner("Mean Stock Performance"),
                html.Div([
                dcc.Dropdown(className="three columns", id='year-drop-down-3',options=[{'label':k,'value':k} for k in stocks_df['year'].unique()],placeholder='Choose a year ...',value=None),
                dcc.Dropdown(className="three columns", id='month-drop-down-3',options=[{'label':k,'value':k} for k in stocks_df['month'].unique()],placeholder='Choose a month ...',value=None),
                ],className="row"),
                dcc.Graph(id='third-figure',figure={}),
                ],
                
    )


def build_fourth_graph():
    return html.Div(
        id="fourth-graphs-container",
        className="two columns",
        children=[
                generate_section_banner("Stock Distribution for each company"),
                html.Div([
                dcc.Dropdown(className="three columns", id='stocks-drop-down-4',options=[{'label':k,'value':k} for k in px.data.stocks().columns[1:]],placeholder='Choose a stock ...',value=None),
                dcc.Dropdown(className="three columns", id='year-drop-down-4',options=[{'label':k,'value':k} for k in stocks_df['year'].unique()],placeholder='Choose a year ...',value=None),
                dcc.Dropdown(className="three columns", id='month-drop-down-4',options=[{'label':k,'value':k} for k in stocks_df['month'].unique()],placeholder='Choose a month ...',value=None),
                ],className="row"),
                dcc.Graph(id='fourth-figure',figure={}),
                ],
                
    )

big_number_fig = go.Figure(
    go.Indicator(
        mode="number",
        value=400,
        number={"prefix": "$"},
        domain={"x": [0, 1], "y": [0, 1]},
    )
)

big_number_fig.update_layout(
    paper_bgcolor="lightgray",
    height=200,
    width=200 
)

def second_graph_data(stocks_df, company_name, month, year): 
    stocks= stocks_df[stocks_df['year']==year]
    stocks= stocks[stocks['month']==month]
    return stocks[['date', company_name]]

def generate_section_banner(title):
    return html.Div(className="section-banner", children=title)



app.layout = html.Div(
    id="big-app-container",
    children=[
        build_banner(),
        html.Div(
            id="app-container",
            children=[
                build_big_numbers(),
                build_first_graph(),
                html.Div([build_second_graph(),
                build_third_graph(),
                build_fourth_graph(),],className="row"),
                # Main app
                html.Div(id="app-content"),
            ],
        ),
    ],
)

@app.callback(
    Output(component_id='second-figure', component_property='figure'),
    Input(component_id='stocks-drop-down', component_property='value'),
    Input(component_id='year-drop-down', component_property='value'),
    Input(component_id='month-drop-down', component_property='value'),
    # Input(component_id='second-graph-submit-button',component_property='n_clicks'),
)
def update_div(stock,year,month):
    if (stock is not None) and (year is not None) and (month is not None):
        temp_df = second_graph_data(stocks_df,stock,month,year)
        return px.line(temp_df, x= 'date', y= stock,template='plotly_dark')
    else:
        raise PreventUpdate

@app.callback(
    Output(component_id='third-figure', component_property='figure'),
    Input(component_id='year-drop-down-3', component_property='value'),
    Input(component_id='month-drop-down-3', component_property='value'),
)
def update_div(year,month):
    if (year is not None) or (month is not None):
        s = filter_time(stocks_df, year, month)
        stock_mean = s[['GOOG', 'AAPL', 'AMZN', 'FB', 'NFLX', 'MSFT']].mean()
        return px.bar(stock_mean, y= stock_mean.index, x= stock_mean.values,template='plotly_dark')
    else:
        raise PreventUpdate


@app.callback(
    Output(component_id='fourth-figure', component_property='figure'),
    Input(component_id='stocks-drop-down-4', component_property='value'),
    Input(component_id='year-drop-down-4', component_property='value'),
    Input(component_id='month-drop-down-4', component_property='value'),
)
def update_div(stock, year,month):
    if (stock is not None) and (year is not None):
        df = fourth_graph_data(stocks_df, stock, year,month)
        fig = px.histogram(df, x= stock, nbins= 9,template='plotly_dark')
        fig.add_vline(x= df[stock].mean())
        return fig
    else:
        raise PreventUpdate


# Running the server
if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
