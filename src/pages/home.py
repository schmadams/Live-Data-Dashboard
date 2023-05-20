from src.templates.home.main_layout import page_template
from src.helper_functions.helpers import load_raw_data, load_config, data_table_content
from src.pipelines.plots.cat_scatter_plot import CatScatter
from src.pipelines.plots.rating_timeline import RatingTimeline
from dash import callback, Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd


prefix = 'home-'

def home_layout():
    return page_template(prefix=prefix)

@callback(
    Output(f'{prefix}data', 'data'),
    Output(f'{prefix}config', 'data'),
    Input(f'{prefix}page', 'children')
)
def initial_load(container):
    data = load_raw_data()
    for name, df in data.items():
        if name == 'data':
            df = df[df['Status'] == 'Completed']
        data[name] = df.to_dict('records')
    config = load_config()

    return data, config

@callback(
    Output(f'{prefix}cat-scatter-categorical-dropdown', 'options'),
    Output(f'{prefix}cat-scatter-categorical-dropdown', 'value'),
    Input(f'{prefix}data', 'data'),
    State(f'{prefix}cat-scatter-categorical-dropdown', 'value'),
    State(f'{prefix}config', 'data'),
    prevent_initial_call=True
)
def populate_categorical_dropdown(data, selected, config):
    options = [{'label': str(name).replace('_', ''), 'value': name}
               for name in config['raw_data']['categorical_fields']]
    return options, selected

@callback(
    Output(f'{prefix}cat-scatter-categorical-yaxis', 'options'),
    Output(f'{prefix}cat-scatter-categorical-yaxis', 'value'),
    Input(f'{prefix}data', 'data'),
    State(f'{prefix}cat-scatter-categorical-yaxis', 'value'),
    State(f'{prefix}config', 'data'),
    prevent_initial_call=True
)
def populate_yaxis_dropdown(data, selected, config):
    options = [{'label': str(name).replace('_', ''), 'value': name}
               for name in config['raw_data']['rating_fields']]
    return options, selected


@callback(
    Output(f'{prefix}cat-scatter-categorical-xaxis', 'options'),
    Output(f'{prefix}cat-scatter-categorical-xaxis', 'value'),
    Input(f'{prefix}cat-scatter-categorical-yaxis', 'value'),
    State(f'{prefix}cat-scatter-categorical-xaxis', 'value'),
    State(f'{prefix}config', 'data'),
    prevent_initial_call=True
)
def populate_xaxis_dropdown(yaxis, selected, config):
    options = [{'label': str(name).replace('_', ''), 'value': name}
               for name in config['raw_data']['rating_fields'] if name != yaxis]
    return options, selected

@callback(
    Output(f'{prefix}cat-scatter-figure', 'figure'),
    Output(f'{prefix}cat-scatter-table', 'columns'),
    Output(f'{prefix}cat-scatter-table', 'data'),
    Input(f'{prefix}cat-scatter-categorical-yaxis', 'value'),
    Input(f'{prefix}cat-scatter-categorical-xaxis', 'value'),
    Input(f'{prefix}cat-scatter-categorical-dropdown', 'value'),
    State(f'{prefix}data', 'data'),
    prevent_initial_call=True
)
def create_cat_scatter(yax, xax, cat, data):
    if None in [cat, yax, xax, data]:
        raise PreventUpdate
    df = pd.DataFrame(data['data'])
    fig, grouped_df = CatScatter(data=df, cat=cat, y=yax, x=xax).create_fig()
    table_data, columns = data_table_content(grouped_df)
    return fig, columns, table_data

@callback(
    Output(f'{prefix}timeline-rating-dropdown', 'options'),
    Output(f'{prefix}timeline-rating-dropdown', 'value'),
    Input(f'{prefix}config', 'data'),
    State(f'{prefix}timeline-rating-dropdown', 'value'),
    prevent_initial_call=True
)
def rating_timeline_dropdown(config, selected):
    if not isinstance(selected, list):
        selected = [selected]
    options = [{'label': str(name).replace('_', ''), 'value': name}
               for name in config['raw_data']['rating_fields'] if name not in selected]
    return options, selected

@callback(
    Output(f'{prefix}timeline-rating-figure', 'figure'),
    Input(f'{prefix}timeline-rating-dropdown', 'value'),
    State(f'{prefix}data', 'data'),
    prevent_inital_call=True
)
def create_rating_timeline_plot(selected_fields, data):
    if not isinstance(selected_fields, list):
        selected_fields = [selected_fields]

    vars = selected_fields + [data]
    if None in vars:
        raise PreventUpdate

    df = pd.DataFrame(data['data'])

    fig = RatingTimeline(data=df, fields=selected_fields).create_fig()
    return fig

@callback(
    Output(f'{prefix}categorical-rating-cat-dropdown', 'options'),
    Output(f'{prefix}categorical-rating-cat-dropdown', 'value'),
    Input(f'{prefix}config', 'data'),
    State(f'{prefix}categorical-rating-cat-dropdown', 'value'),
    prevent_initial_call=True
)
def cat_2_rat_cat_dropdown(config, selected):
    options = [{'label': str(name).replace('_', ''), 'value': name}
               for name in config['raw_data']['categorical_fields']]
    return options, selected


@callback(
    Output(f'{prefix}categorical-rating-rat-dropdown', 'options'),
    Output(f'{prefix}categorical-rating-rat-dropdown', 'value'),
    Input(f'{prefix}config', 'data'),
    State(f'{prefix}categorical-rating-rat-dropdown', 'value'),
    prevent_initial_call=True
)
def cat_2_rat_rat_dropdown(config, selected):
    options = [{'label': str(name).replace('_', ''), 'value': name}
               for name in config['raw_data']['rating_fields']]
    return options, selected