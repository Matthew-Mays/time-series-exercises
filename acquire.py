import pandas as pd
import numpy as np
import os
import requests
import warnings
warnings.filterwarnings("ignore")

def get_items_data(base_url):
    response = requests.get(base_url)
    data = response.json()
    df = pd.DataFrame(data['payload']['items'])
    for i in range(1, data['payload']['max_page']):
        response = requests.get(base_url[:23] + data['payload']['next_page'])
        data = response.json()
        df = pd.concat([df, pd.DataFrame(data['payload']['items'])]).reset_index(drop=True)
    return df

def get_stores_data(base_url):
    response = requests.get(base_url)
    data = response.json()
    df = pd.DataFrame(data['payload']['stores'])
    for i in range(1, data['payload']['max_page']):
        response = requests.get(base_url[:23] + data['payload']['next_page'])
        data = response.json()
        df = pd.concat([df, pd.DataFrame(data['payload']['stores'])]).reset_index(drop=True)
    return df

def get_sales_data(base_url):
    response = requests.get(base_url)
    data = response.json()
    df = pd.DataFrame(data['payload']['sales'])
    for i in range(1, data['payload']['max_page']):
        response = requests.get(base_url[:23] + data['payload']['next_page'])
        data = response.json()
        df = pd.concat([df, pd.DataFrame(data['payload']['sales'])]).reset_index(drop=True)
    return df

def df_to_csv(items, stores, sales):
    items.to_csv('items.csv', index=False)
    stores.to_csv('stores.csv', index=False)
    sales.to_csv('sales.csv', index=False)

def df_combine(sales, stores, items):
    full_df = sales.merge(stores, left_on='store', right_on ='store_id')
    full_df = full_df.merge(items, left_on='item', right_on='item_id')
    return full_df

def get_powerdf():
    power = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
    return power

