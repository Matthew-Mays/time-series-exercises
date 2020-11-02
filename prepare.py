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

def g_weather_dtformat(df):
    df.Date = pd.to_datetime(df.Date)
    return df

def g_weather_pairplot(df):
    sns.pairplot(df)

def g_weather_reindex(df):
    df = df.set_index('Date').sort_index()
    return df

def g_weather_new_cols(df):
    df['month'] = df.index.month
    df['year'] = df.index.year
    return df

def g_weather_missing(df):
    df.Wind = df.Wind.fillna(df.Wind.mean())
    df.Solar = df.Solar.fillna(df.Solar.mean())
    df['Wind+Solar'] = df['Wind+Solar'].fillna(df.Wind + df.Solar)
    return df