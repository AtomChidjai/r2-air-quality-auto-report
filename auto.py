import requests as req
import json
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from dotenv import load_dotenv
import os

def apiLoad():
    load_dotenv()

    api_key = os.environ.get('API_KEY')
    url = f'http://api.airvisual.com/v2/city?city=Ban%20Pong&state=Ratchaburi&country=Thailand&key={api_key}'
    res = req.get(url)
    load_text = json.loads(res.text)

    air_quality = load_text['data']['current']['pollution']
    weather_info= load_text['data']['current']['weather']

    data = {**air_quality, **weather_info}

    df = pd.DataFrame([data])
    dfx = df.drop(['ts', 'ic', 'mainus', 'maincn'], axis=1)
    metric = dfx.iloc[0]

    df_plot = pd.DataFrame({
        'Metric': metric.index,
        'Value': metric.values
    })

    return df_plot

def graph(dt):
    date_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    date_filename = datetime.today().strftime('%Y_%m_%d_%H_%M_%S')

    plt.figure(figsize=(12, 6))
    sns.barplot(data=dt, x='Metric', y='Value')
    plt.title(f'Ban Pong Air Quality & Weather -- {date_time}')

    plt.savefig(f'{date_filename}.png')

    plt.close()
