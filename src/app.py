from dash import html, dcc
from dash.dependencies import Input, Output
from src.pages.home import home_layout
from src.app_helper_functions.helpers import load_custom_css
import dash
import dash_bootstrap_components as dbc
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


cust_css = load_custom_css()

app = dash.Dash(__name__, title='Live Data Analysis', suppress_callback_exceptions=False, external_stylesheets=[dbc.themes.BOOTSTRAP, cust_css])

server = app.server
app.config.suppress_callback_exceptions = False

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
], style={'background': 'white', 'height': '100vw', 'width': '100vw'})


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    print(pathname)
    if pathname == '/home':
        return home_layout()
    else:
        return home_layout()


if __name__ == '__main__':
    app.run_server(debug=False)
