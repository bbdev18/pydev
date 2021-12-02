# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 12:19:48 2021


1. Read in data
2. Analyse data with df.info()
- some columns are missing data and replaced with '.'
- POST_ECHO_RHYTHM: some fields not consistent: - make lower/upper case
- LT_INTERVENTION_TYPE - missing field, one has both 1 and 2 - maybe convert to 3 that include 1 and 3

x. export to html table


"""

import pandas as pd
import matplotlib.pyplot as plt
import webbrowser
import numpy as np


"""
Read in excel file
"""

# dccv = pd.read_excel("dccv.xlsx",engine='openpyxl')
dccv = pd.read_csv("dccv_cc.csv")

"""
Set Pin as the index column
"""

dccv.set_index('PIN',inplace=True)

"""
Rename verbose column names
"""
dccv = dccv.rename(columns=
                   {"LT_INTERVENTION_TYPE (0=NIL, 1=dccv, 2= AFCA, 3= Pace and ablate)": "LT_INTERVENTION_TYPE",
                    "LONGTERM_RHYTHM  (TRUE=SR, FALSE = AF)": "LONGTERM_RHYTHM",
                    "PRE_ETOH 2=excess 1=normal limits 0=none": "PRE_ETOH",
                    "PRE_AF_DURATION (0-3 days, 4 days to 3 months, > 3 months)": "PRE_AF_DURATION"})


# print(dccv["Symptoms"][1:2])

# dccv=dccv.drop(['CHANGE_LAVI'],inplace=True,axis=1)

"""
 - some columns are missing data and replaced with '.' NaN
"""
dccv=dccv.replace('.',float("NaN"))

"""
POST_ECHO_RHYTHM: some fields not consistent: - make lower/upper case
"""

dccv["POST_ECHO_RHYTHM"] = dccv["POST_ECHO_RHYTHM"].str.upper()

"""
LT_INTERVENTION_TYPE - missing field, one has both 1 and 2 - maybe convert to 3 that include 1 and 3
"""

dccv["LT_INTERVENTION_TYPE"][30] = 1
dccv["LT_INTERVENTION_TYPE"] = dccv["LT_INTERVENTION_TYPE"].astype(float)


"""
The describe(), max, head method provides a quick overview of the DataFrame.

"""
print(dccv.info())

# print(dccv.max())
# 
# print(dccv.describe())

# print(dccv["Age"].describe())

# print(dccv.head(10))


"""
Certain range of data and above age 60, the inner bracket is actually a new series of true and false
"""

# print(dccv[["Age","Symptoms","POST_ECHO_RHYTHM"]])

# above_60 = dccv[dccv["Age"] > 60]

# print(above_60[["Age","Symptoms","POST_ECHO_RHYTHM"]])

# dccv_above_60 = above_60[["Age","Symptoms","POST_ECHO_RHYTHM"]]

# dccv_above_60.to_excel("dccv_above_60.xlsx", sheet_name="data")

"""
Specifc fields

"""

# class_AF_SR = dccv[dccv["POST_ECHO_RHYTHM"].isin(["AF"])]

# class_AF_SR = dccv[(dccv["POST_ECHO_RHYTHM"] == "AF") | (dccv["POST_ECHO_RHYTHM"] == "SR")]

# class_AF_SR = dccv[(dccv["POST_ECHO_RHYTHM"] == "SR")]

# print(class_AF_SR[["Age","Symptoms","POST_ECHO_RHYTHM"]])

# print(class_AF_SR[["Age","Symptoms","POST_ECHO_RHYTHM"]][1:10])

"""
Ignore NaN fields
"""

# lt_inter_type_no_na = dccv[dccv["LT_INTERVENTION_TYPE"].notna()]

# print(lt_inter_type_no_na["LT_INTERVENTION_TYPE"])

"""
Iâ€™m interested in the POST_ECHO_RHYTHM of the patiends older than 60 years.
"""

# over_60_POST_ECHO = dccv.loc[dccv["Age"] > 60, "POST_ECHO_RHYTHM"]

# print(over_60_POST_ECHO)

"""
loc is used for index name and iloc used for index
"""


"""
Iâ€™m interested in the rows 10 till 25 and columns 3 to 5..
"""

# print(dccv.iloc[9:25, 2:5])

"""
PLots
"""

# dccv[["Age","Symptoms","POST_ECHO_RHYTHM"]].plot()
# dccv.plot.scatter(x="CHANGE_LVEF",y="CHANGE_LVID",alpha=0.5)
# axs = dccv.plot.area(figsize=(12, 4), subplots=True)

"""
Stats
"""
# print(dccv["CHANGE_LVEF"].mean())
# print(dccv[["CHANGE_LVEF","CHANGE_LVID"]].mean())
# print(dccv.iloc[9:25, 2:5].mean())
# print(dccv[["CHANGE_LVEF","CHANGE_LVID"]].describe())
# print(dccv.groupby("Sex")[["CHANGE_LVEF","CHANGE_LVID"]].mean())
# print(dccv.groupby(["Sex","POST_ECHO_RHYTHM"])[["CHANGE_LVEF","CHANGE_LVID"]].mean())
# print(dccv.groupby(["Sex","POST_ECHO_RHYTHM"])[["CHANGE_LVEF","CHANGE_LVID"]].count())
# print(dccv.sort_values(by="Age").head())
# print(dccv.sort_values(by=["Age","CHANGE_LVEF"]).head())
# print(dccv.pivot(index="Sex",columns="Symptoms",values="CHANGE_LVEF"))
# print(pd.pivot_table(data=dccv,index=["Sex"]))



"""
Render HTML
"""

html = dccv.to_html()
text_file = open("index.html", "w")
text_file.write(html)
text_file.close()

# webbrowser.open_new_tab('index.html')

"""
Create New Excel File
"""
# dccv.to_excel("dccv_1.xlsx", sheet_name="data")
