import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from dataframe_filter import filter_data

app = dash.Dash('Hello World')

app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'leadOwner', 'value': 'leadOwner'},
            {'label': 'TerritoryName', 'value': 'TerritoryName'},
            {'label': 'ProductName', 'value': 'ProductName'},
            {'label': 'Rating', 'value': 'Rating'},
            {'label': 'TeamName', 'value': 'TeamName'},
            {'label': 'ProcessName', 'value': 'ProcessName'},
        ],
        value='TerritoryName'
    ),
    dcc.Graph(id='my-graph')
], style={'width': '1400'})


@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(drop_down_value):
    data_obj = filter_data(drop_down_value)
    return data_obj


app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
if __name__ == "__main__":
    app.run_server()