import yaml
from pathlib import Path
import pandas as pd
import numpy as np
from logging_functions.class_logging import Logger

def load_config():
    for file in Path(__file__).parent.parent.glob('*'):
        if str(file).endswith('yaml'):
            with open(str(file), "r") as stream:
                return yaml.safe_load(stream)


def load_raw_data():
    config, raw_data = load_config(), {}
    for dir in Path(__file__).parent.parent.parent.glob('*'):
        if str(dir).endswith('assets'):
            for file in dir.glob('*'):
                if str(file).endswith(config['raw_data']['raw_data_file']):
                    for sheet in config['raw_data']['sheets']:
                        raw_data[sheet] = pd.read_excel(file, sheet_name=config['raw_data']['sheets'][sheet])
    return raw_data



def header_strings(string):
    return string.lower().strip().replace('_', ' ').title()

def data_table_content(data):
    if not isinstance(data, pd.DataFrame):
        data = pd.DataFrame(data)
    columns = [{'name': header_strings((col)), 'id': col} for col in data.columns]
    return data.to_dict('records'), columns

def load_nav_logo():
    for file in Path(__file__).parent.parent.parent.glob('*'):
        if str(file).endswith('assets'):
            for resource in file.glob('*'):
                if str(resource).endswith('logo.png'):
                    logo_file = resource
    return str(logo_file)

def load_custom_css():
    for file in Path(__file__).parent.parent.parent.glob('*'):
        if str(file).endswith('assets'):
            for resource in file.glob('*'):
                if str(resource).endswith('.css'):
                    customcss = resource
    return str(customcss)

if __name__ == '__main__':
    sic_desc = load_raw_data()
    a=1
    a=1