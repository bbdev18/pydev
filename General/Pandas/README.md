Pandas

Index:
## dataframe_to_html:


1. create dataframe
```
data = {'DATE':  ['2021-10-13','2021-10-14','2021-10-15','2021-10-16','2021-10-17','2021-10-18'],
        'MIN_TEMP': [68,65,60,51,30,70],
        'MAX_TEMP': [71,73,63,55,32,31]}
```
- Create dataframe
```
df_temps = pd.DataFrame(data)
```
2. Convert date to datetime column
```
df_temps['DATE'] = pd.to_datetime(df_temps['DATE'])
```

3. Set Index to Date Column:
```
df_temps.set_index('DATE',inplace=True,drop=True)
```
