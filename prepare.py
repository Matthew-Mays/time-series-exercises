from acquire import df_combine, get_powerdf
import pandas as pd
import seaborn as sns

def get_store_item_sale_data():
    stores = pd.read_csv('stores.csv')
    items = pd.read_csv('items.csv')
    sales = pd.read_csv('sales.csv')
    df = df_combine(sales, stores, items)
    return df

def date_reindex(df):
    df.sale_date = pd.to_datetime(df.sale_date)
    return df

def sale_plotter():
    by_date_sales = df.groupby(['sale_date']).sale_amount.sum().reset_index()
    by_date_sales.plot(x='sale_date', y='sale_amount')

def add_columns(df):
    df['month'] = df.index.month
    df['day_of_week'] = df.index.weekday
    return df

