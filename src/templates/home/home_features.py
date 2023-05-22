from src.app_helper_functions.navbar import create_navbar
from dash import html, dash_table, dcc
import dash_bootstrap_components as dbc
import dash_daq as daq
from src.app_helper_functions.datatables_builder import DataTableBuilder

def cat_scatters(prefix):
    return [
        html.Div(className='row', id=f'{prefix}cat-scatter-div', children=[
        dcc.Dropdown(id=f'{prefix}cat-scatter-categorical-dropdown', multi=False, style={'width': '10vw', 'margin': 'auto'}, placeholder='Select a Categorical Variable'),
        dcc.Dropdown(id=f'{prefix}cat-scatter-categorical-yaxis', multi=False, style={'width': '10vw', 'margin': 'auto'}, placeholder='Select y-axis'),
        dcc.Dropdown(id=f'{prefix}cat-scatter-categorical-xaxis', multi=False, style={'width': '10vw', 'margin': 'auto'}, placeholder='Select x-axis'),
    ], style={'width': '40vw', 'margin': 'auto'}),
        html.Div(className='row', children=[
            dcc.Graph(id=f'{prefix}cat-scatter-figure', style={'width': '60%', 'height': '90%'}),
            html.Div(children=[
                html.Div(children=[
                    DataTableBuilder(prefix=prefix).basic_datatable(id=f'{prefix}cat-scatter-table')
                ], style={'width': '80%', 'margin': '5% 10% auto 10%'})
                ], style={'width': '35%', 'height': '90%', 'margin': 'auto'})
        ])
    ]

def timeline_plot(prefix):
    return [
        html.Div(className='row', children=[
            dcc.Dropdown(id=f'{prefix}timeline-rating-dropdown', multi=True,
                         style={'width': '30vw', 'margin': 'auto'}, placeholder='Select rating field(s)')
        ], style={'width': '40vw', 'margin': 'auto'}),
        html.Div(className='row', children=[
            dcc.Graph(id=f'{prefix}timeline-rating-figure', style={'width': '80%', 'height': '90%'})
        ])
    ]


def cat_2_rat_section_1(prefix):
    return [
        html.Div(className='row', children=[
            html.Div(className='column', children=[
                dcc.Dropdown(id=f'{prefix}categorical-rating-cat-dropdown', multi=False,
                             style={'width': '10vw', 'margin': '1vw auto'}, placeholder='Select Categorical Variable'),
                dcc.Dropdown(id=f'{prefix}categorical-rating-rat-dropdown', multi=False,
                             style={'width': '10vw', 'margin': '1vw auto'}, placeholder='Select Rating Field'),
                daq.BooleanSwitch(id=f'{prefix}cat-2-rat-switch', on=False, color="red"),
                html.P("Show Percentages", style={'margin': 'auto', 'text-align': 'center', 'font-size': '12px'})
            ], style={'width': '10%', 'margin': 'auto'}),
            # dcc.Graph(id=f'{prefix}test', style={'width': '100%', 'height': '90%', 'margin': 'auto'})
            html.Div(id=f'{prefix}cat-2-rat-fig-container', hidden=False, className='column', children=[
                dcc.Graph(id=f'{prefix}test', style={'width': '100%', 'height': '90%', 'margin': 'auto'})
            ], style={'width': '80%', 'margin': 'auto'})
        ])
    ]

def page_layout(prefix):
    content = [
        create_navbar(),
        dbc.Accordion(
            children=[
                dbc.AccordionItem(title='Categorical Ratings', children=cat_2_rat_section_1(prefix)),
                dbc.AccordionItem(title='Categorical Scatter Plot', children=cat_scatters(prefix)),
                dbc.AccordionItem(title='Time Series Analysis', children=timeline_plot(prefix))
            ]
        )
    ]
    return content











#