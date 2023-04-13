from dash import html, dcc
from dash.dependencies import Input, Output
from src.pages.home import create_page_home
from src.pages.populations import populations_layout
from src.helper_functions.helpers import load_custom_css
from src.pages.page_3 import create_page_3
import dash
import dash_bootstrap_components as dbc
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


cust_css = load_custom_css()

app = dash.Dash(__name__, suppress_callback_exceptions=False, external_stylesheets=[dbc.themes.BOOTSTRAP, cust_css])

server = app.server
app.config.suppress_callback_exceptions = False

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/populations':
        print('running pop page')
        return populations_layout()
    if pathname == '/page-3':
        return create_page_3()
    else:
        return create_page_home()


if __name__ == '__main__':
    app.run_server(debug=False)