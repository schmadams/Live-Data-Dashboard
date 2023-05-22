from dash import html, dcc, dash_table


class DataTableBuilder:
    def __init__(self, prefix):
        self.prefix = prefix
    def basic_datatable(self, id):
        return dash_table.DataTable(
            id=id,
            style_data={'whiteSpace': 'normal', 'backgroundColor': 'whtie', 'color': 'black', 'border': 'none'},
            style_header={'textAlign': 'center', 'backgroundColor': '#D3D3D3', 'color': 'black'},
            style_cell={'textAlign': 'center', 'fontSize': 12, 'font-family': 'sans-serif', 'minWidth': '10%'},
            style_table={'overflowY': 'auto'},
            sort_action="native",
            page_size=10,
            style_as_list_view=True,

        )