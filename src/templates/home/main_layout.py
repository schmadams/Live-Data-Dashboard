from src.templates.home.home_features import page_layout
from dash import html
from dash import dcc
def page_template(prefix):
    content = make_storages(prefix) + page_layout(prefix)
    layout = html.Div(id=f'{prefix}page', children=content, style={'background': 'white'})
    return layout

def make_storages(prefix):
    content = [
        dcc.Store(id=f'{prefix}data', storage_type='memory'),
        dcc.Store(id=f'{prefix}config', storage_type='memory')
    ]
    return content