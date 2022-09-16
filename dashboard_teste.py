# Load exploratory data analysis
import pandas as pd
import numpy as np
import csv
import dash 
import dash_core_components as dcc
import dash_html_components as html

from dash import Dash
from dash import dcc
from dash import html


import plotly.graph_objects as go # or plotly.express as px

df_count_patient = pd.read_csv('patient.csv')

 

fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)

fig.add_trace(go.Indicator(
    value = int(df_count_patient['patient_id (DISTINCT_COUNT)']),
    delta = {'reference': 2000000},
    gauge = {
        'axis': {'visible': False}},
    domain = {'row': 0, 'column': 0}))

fig.add_trace(go.Indicator(
    value = 120,
    gauge = {
        'shape': "bullet",
        'axis' : {'visible': False}},
    domain = {'x': [0.05, 0.5], 'y': [0.15, 0.35]}))

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = 300,
    domain = {'row': 0, 'column': 1}))

fig.add_trace(go.Indicator(
    mode = "delta",
    value = 40,
    domain = {'row': 1, 'column': 1}))

fig.update_layout(
    grid = {'rows': 2, 'columns': 2, 'pattern': "independent"},
    template = {'data' : {'indicator': [{
        'title': {'text': "Total de pacientes únicos no mês"},
        'mode' : "number+delta+gauge",
        'delta' : {'reference': 90}}]
                         }})
app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)])

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False) 
