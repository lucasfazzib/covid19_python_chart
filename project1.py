from typing import final
import requests as r
import datetime as dt
import csv
from PIL import Image
from IPython.display import display
from urllib.parse import quote

url = 'https://api.covid19api.com/dayone/country/brazil'
resp = r.get(url)
#print(resp.status_code)

raw_data = resp.json()
#print(raw_data[0])
#{'ID': '5b679794-2952-4c4c-a873-af6ff457b0fd', 'Country': 'Brazil', 'CountryCode': 'BR', 'Province': '', 'City': '', 'CityCode': '', 'Lat': '-14.24', 'Lon': '-51.93', 'Confirmed': 1, 'Deaths': 0, 'Recovered': 0, 'Active': 1, 'Date': '2020-02-26T00:00:00Z'}

final_data = []
for obs in raw_data:
    final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])

final_data.insert(0, ['confirmados', 'obitos', 'recuperados', 'ativos', 'data'])
#print(final_data)

CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4

for i in range(1, len(final_data)):
    final_data[i][DATA] = final_data[i][DATA][:10]

#print(final_data)

#print(dt.time(12, 6, 21, 7), 'Hora:minuto:segundo.microsegundo')
#print('---------')
#print(dt.date(2020, 4, 25), 'Ano-mês-dia')
#print('---------')
#print(dt.datetime(2020, 4, 25, 12, 6, 21, 7), 'Ano-mês-dia Hora:minuto:segundo.microsegundo')

natal = dt.date(2020, 12, 25)
reveillon = dt.date(2011, 1, 1)

#print(reveillon - natal)
#print((reveillon - natal).days)
#print((reveillon - natal).seconds)
#print((reveillon - natal).microseconds)

with open('brasil-covid.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(final_data)


for i in range(1, len(final_data)):
    final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], '%Y-%m-%d')

#print(final_data)

def get_dataset(y, labels):
    if type(y[0]) == list:
        datasets = []
        for i in range(len(y)):
            datasets.append({
                'label': labels[i],
                'data' : y[i]
            })
        
        return datasets
    else:
        return [
            {
                'label': labels[0],
                'data' : y
            }
        ]

def set_title(title=''):
    if title != '':
        display = 'true'
    else:
        display = 'false'
    return {
        'title'  : title,
        'display': display
    }


def create_chart(x, y, labels, kind='bar', title=''):
    dataset = get_dataset(y, labels)
    options = set_title(title)

    chart = {
        'type': kind,
        'data': {
            'labels': x,
            'datasets' : dataset
        },
        'options' : options
    }

    return chart


def get_api_chart(chart):
    url_base = 'https://quickchart.io/chart'
    resp = r.get(f'{url_base}?c={str(chart)}')
    return resp.content

def save_image(path, content):
    with open(path, 'wb') as image:
        image.write(content)


def display_image(path):
    img_pil = Image.open(path)
    display(img_pil)

y_data_1 = []
for obs in final_data[1::10]:
    y_data_1.append(obs[CONFIRMADOS])

y_data_2 = []
for obs in final_data[1::10]:
    y_data_2.append(obs[RECUPERADOS])

labels = ['Confirmados', 'Recuperados']

x = []
for obs in final_data[1::10]:
    x.append(obs[DATA].strftime('%d/%m/%Y'))

chart = create_chart(x, [y_data_1, y_data_2], labels, title='Gráfico Confirmados vs Recuperados')
chart_content = get_api_chart(chart)
save_image('meu-grafico-covid.png', chart_content)
display_image('meu-grafico-covid.png')



def get_api_qrcode(link):
    text = quote(link) #parsing the link to url
    url_base = 'https://quickchart.io/qr'
    resp = r.get(f'{url_base}?text={text}')
    return resp.content

url_base = 'https://quickchart.io/chart'
link = f'{url_base}?c={str(chart)}'
save_image('qr-code.png', get_api_qrcode(link))










































