from dash import html, dcc
from dash.dependencies import Input, Output
from src.pages.home import home_layout
import dash
import dash_bootstrap_components as dbc
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)



app = dash.Dash(__name__, title='Live Data Analysis', suppress_callback_exceptions=True,#
                external_stylesheets=[dbc.themes.BOOTSTRAP,
                                      "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css",
                                      "../assets/styles.css"])

app = dash.Dash(__name__, external_stylesheets=[])


server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
], style={'background': 'white', 'height': '100vw', 'width': '100vw'})

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/home':
        return home_layout()
    else:
        return home_layout()


if __name__ == '__main__':
    app.run_server(debug=True)
