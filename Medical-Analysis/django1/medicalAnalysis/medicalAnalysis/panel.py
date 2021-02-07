import param
import panel as pn
import pandas as pd
import numpy as np
import holoviews as hv
from holoviews import opts
import io
import datetime
import csv
import google.cloud
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import hvplot
import hvplot.pandas
import hvplot.dask
import dask.dataframe as dd

# https://www.kaggle.com/utkarshxy/who-worldhealth-statistics-2020-complete

frames = []

path = "/home/tyler/Desktop/School Stuff/Applied Programming/Medical-Analysis/django1/medicalAnalysis/medicalAnalysis/"

collections = ['lifeExpectancyAtBirth',
 'maternalMortalityRatio',
 'newHivInfections',
 'cleanFuelAndTech',
 '.ipynb_checkpoints',
 'hepatitusBsurfaceAntigen',
 'birthAttendedBySkilledPersonal',
 'medicalDoctors',
 'crudeSuicideRates',
 'mortalityRatePoisoning',
 'population25SDG3.8.2']
try: 
    # Use a service account
    cred = credentials.Certificate('/home/tyler/Desktop/School Stuff/Applied Programming/Medical-Analysis/django1/medicalAnalysis/medicalAnalysis/workshop1-60a05-firebase-adminsdk-egq5y-bda0fb5ee1 (1).json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    for x in collections[:1]:
        docs = db.collection(x).get()
        data = []
        for doc in docs:
            data.append(doc.to_dict())
        df = pd.DataFrame(data)
        frames.append(df)
except:
    frames = []
    collections = []

    file_list = os.listdir(f'{path}csvs')
    for file in file_list:
        file_path = f"{path}csvs/{file}"
        df = pd.read_csv(file_path)
        frames.append(df)
        collection_name = f"{file}".split('.csv')[0]
        collections.append(collection_name)


df = frames[0]
year_list = range(2000,2021)

class DataSetSelect(param.Parameterized):
    """
    This is where all the action happens. This is a self
    contained class where all the parameters are dynamic
    and watch each other for changes. 
    See https://panel.holoviz.org/ for details
    and https://discourse.holoviz.org/c/panel/5 for help

    Widgets and Parameters in this class need to be added
    to pn_app.py to be able to display.
    """

    hv.extension('bokeh')

    css = """

    .bk{
        width = 1000;
    }

    .bk.bk-btn.bk-btn-default {
        font-family: Arial;
        font-weight: bold;
        text-align: center;
        color: #0077ff
    }

    .bk-root h2 {
        font-family: Arial;
        font-weight: bold;
        text-align: center;
        color: black;
    }

    .bk-root h6 {
        font-family: Arial;
        font-weight: bold;
        text-align: center;
        color: black;
    }

    .bk-root label {
        font-family: Arial;
        font-weight: bold;
        color: black;
    }

    .bk-root .bk-tabs-header .bk-tab.bk-active {
        background-color: #0077ff;
        color: white;
        font-weight: bold;
    }
    """

    pn.extension(raw_css=[css])

    title = '##' + 'Medical Analysis'
    message = ''

    countries = list((frames[collections.index(collections[0])])['Location'].unique())
    countries.append('World')

    data_select = param.ObjectSelector(objects=collections, label='Select Data', 
        default=collections[0],
        precedence=1)

    date_select = param.ObjectSelector(objects=year_list, label='Start Date', 
        default=year_list[0],
        precedence=1)

    date_select1 = param.ObjectSelector(objects=year_list, label='End Date', 
        default=year_list[-1],
        precedence=1)

    country_select = param.ObjectSelector(objects= countries, label='Country', 
        default=((frames[collections.index(collections[0])])['Location'].unique())[0],
        precedence=1)

    # find_country = param.Action(lambda self: self.param.trigger('view_report'), label='View Report', precedence=1)
    
    def add_title(self):
        return self.title

    @param.depends('message', watch=True)
    def outputs(self):
        return self.message
 
    @param.depends('data_select', watch=True)
    def change_country_list(self):
        countries = list((frames[collections.index(self.data_select)])['Location'].unique())
        countries.append('World')
        self.param.country_select.objects= countries
        self.param.default=((frames[collections.index(self.data_select)])['Location'].unique())[0]

    @param.depends('data_select', 'country_select', 'date_select', 'date_select1', watch=True)
    def view_data(self):
        df = frames[collections.index(self.data_select)]
        df = df[(df['Period'] >= self.date_select) & (df['Period'] <= self.date_select1)]
        if self.country_select != "World":
            df = df.loc[df['Location'] == self.country_select]
        df = df.sort_values('Location')

        return hv.Table(data=df).opts(width=1000)

    @param.depends('data_select', 'country_select', 'date_select', 'date_select1', watch=True)
    def view_data2(self):
        df = frames[collections.index(self.data_select)]
        df = df[(df['Period'] >= self.date_select) & (df['Period'] <= self.date_select1)]

        if self.country_select != "World":
            df = df.loc[df['Location'] == self.country_select]

        try:
            if self.country_select != "World":
                self.message = '######' + df.loc[0]["Indicator"] + f"""
                Average: {df["First Tooltip"].mean()} | Max: {df["First Tooltip"].max()} |
                Min: {df["First Tooltip"].min()}"""
            else:
                self.message = '######' + df.loc[0]["Indicator"] + f"""
                Average: {df["First Tooltip"].mean()} | Max: {df["First Tooltip"].max()}, {df.loc[df['First Tooltip'].idxmax()]["Location"]} |
                Min: {df["First Tooltip"].min()}, {df.loc[df['First Tooltip'].idxmin()]["Location"]}"""
        except:
            self.message = '######' + collections[collections.index(self.data_select)]

        if self.country_select != "World":
            return df.hvplot(y='First Tooltip', x='Period')
        else:
            return df.hvplot.scatter(y='First Tooltip', x='Period')