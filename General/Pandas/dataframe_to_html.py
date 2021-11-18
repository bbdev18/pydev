# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 01:25:55 2021
# https://pythonexamples.org/pandas-render-dataframe-as-html-table/
"""

import pandas as pd

data = {'DATE':  ['2021-10-13','2021-10-14','2021-10-15','2021-10-16','2021-10-17','2021-10-18'],
        'MIN_TEMP': [68,65,60,51,30,70],
        'MAX_TEMP': [71,73,63,55,32,31]}

#Create dataframe
df_temps = pd.DataFrame(data)

#Convert date to datetime column
df_temps['DATE'] = pd.to_datetime(df_temps['DATE'])

df_temps.set_index('DATE',inplace=True,drop=True)

def min_temp(row):    

    lightblue = 'background-color: lightblue;'
    red = 'background-color: red;'
    darkblue = 'background-color: blue;'
    default = ''
    # must return one string per cell in this row
    if row['MIN_TEMP'] <= 68 and row['MIN_TEMP'] >= 32:
        return [lightblue]
    elif row['MIN_TEMP'] > 68:
        return [red]
    elif row['MIN_TEMP'] < 32:
        return [darkblue]
    else:
        return [default]
    
def max_temp(row):    

    lightblue = 'background-color: lightblue;'
    red = 'background-color: red;'
    darkblue = 'background-color: blue;'
    default = ''
    # must return one string per cell in this row
    if row['MAX_TEMP'] <= 68 and row['MAX_TEMP'] >= 32:
        return [lightblue]
    elif row['MAX_TEMP'] > 68:
        return [red]
    elif row['MAX_TEMP'] < 32:
        return [darkblue]
    else:
        return [default]

style1 = df_temps.style.apply(min_temp, subset=['MIN_TEMP'], axis=1).apply(max_temp, subset=['MAX_TEMP'], axis=1).set_table_styles(
    [{"selector": "", "props": [("border", "1px solid grey")]},
      {"selector": "tbody td", "props": [("border", "1px solid grey")]},
     {"selector": "th", "props": [("border", "1px solid grey")]}
    ]
)


df_html = style1.render()

text_file = open("index.html", "w")
text_file.write(df_html)
text_file.close()
