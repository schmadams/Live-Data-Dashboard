import sys
import dash_bootstrap_components as dbc
from src.app_helper_functions.helpers import load_nav_logo
from pathlib import Path
from dash import html, get_asset_url
from PIL import Image
import importlib

#todo - make navbar luton airport theme
def create_navbar():
    nav_item = dbc.NavItem(dbc.NavLink("Home", href="/home", style={'color': 'black'}))
    dropdown = dbc.DropdownMenu(
                    nav=True,
                    in_navbar=True,
                    label="Menu",
                    children=[
                        dbc.DropdownMenuItem("Home", href='/home'),
                        dbc.DropdownMenuItem(divider=True),
                    ],
                    toggle_style={'color': 'black'}

    )

    logo = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src=Image.open(load_nav_logo()), height="40px", width='80px')),
                        ],
                        align="left",
                        className="g-0",
                    ),
                    href="https://www.amey.co.uk/",
                    style={"textDecoration": "none"},
                ),
                dbc.NavbarToggler(id="navbar-toggler2", n_clicks=0),
                dbc.Collapse(
                    dbc.Nav(
                        [nav_item, dropdown],
                        className="ms-auto",
                        navbar=True,
                        style={'color': 'black'}
                    ),
                    id="navbar-collapse2",
                    navbar=True,
                )
            ]
        ),
        color="#D3D3D3",
        dark=True,
        sticky="top",
        className="mb-5",
        style={'height': '80px'}
    )
    return logo

