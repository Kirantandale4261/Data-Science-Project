# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 12:42:04 2023

@author: Shashi
"""

import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from pickle import load
from sklearn.cluster import KMeans

#loading the model
model=load(open("world.sav","rb"))

world=pd.read_excel("World_development_mesurement.xlsx")
st.header("Global Development Measurement")
def input_parameter():
    Country=st.selectbox("Country:",world["Country"].unique())
    Birth=st.number_input("Birth Rate")
    BTR=st.number_input("Business Tax Rate")
    CO2=st.number_input("CO2 Emissions")
    Days=st.number_input("Days to Start Business")
    Energy=st.number_input("Energy Usage")
    GDP=st.number_input("GDP")
    healthGDP=st.number_input("Health Exp % GDP")
    healthCapita=st.number_input("Health Exp/Capita")
    Mobile=st.number_input("Mobile Phone Usage")
    Male=st.number_input("Life Expectancy Female")
    Female=st.number_input("Life Expectancy Male")
    pop_1=st.number_input("Population 0-14")
    pop_2=st.number_input("Population 15-64")
    pop_3=st.number_input("Population 65+")
    Total=st.number_input("Population Total")
    urban=st.number_input("Population Urban")
    Inbound=st.number_input("Tourism Inbound")
    Outbound=st.number_input("Tourism Outbound")
    tax=st.number_input("Hours to do Tax")
    Infant=st.number_input("Infant Mortality Rate")
    Interest=st.number_input("Lending Interest")
    Usage=st.number_input("Internet Usage")
    dict_data={'Birth Rate':[Birth],'Business Tax Rate':[BTR],'CO2 Emissions':[CO2],
               'Country':[Country],'Days to Start Business':[Days],'Energy Usage':[Energy],
               'GDP':[GDP],'Health Exp % GDP':[healthGDP],'Health Exp/Capita':[healthCapita],
               'Hours to do Tax':[tax],'Infant Mortality Rate':[Infant],'Internet Usage':[Usage],
               'Lending Interest':[Interest],'Life Expectancy Female':[Female],
               'Life Expectancy Male':[Male],'Mobile Phone Usage':[Mobile],'Population 0-14':[pop_1],
               'Population 15-64':[pop_2],'Population 65+':[pop_3],'Population Total':[Total],
               'Population Urban':[urban],'Tourism Inbound':[Inbound],'Tourism Outbound':[Outbound]}
    data=pd.DataFrame(dict_data,index=[1,2,3])
    return data
 
    
data=input_parameter() #function call
 
#Cleaning the data
world.drop(['Ease of Business','Number of Records','Country'],axis=1,inplace=True)
world["Tourism Inbound"]=world["Tourism Inbound"].str.replace("$","")
world["Tourism Outbound"]=world["Tourism Outbound"].str.replace("$","")
world["Health Exp/Capita"]=world["Health Exp/Capita"].str.replace("$","")
world["GDP"]=world["GDP"].str.replace("$","")
world["Business Tax Rate"]=world["Business Tax Rate"].str.replace("%","")
world["Tourism Inbound"]=world["Tourism Inbound"].str.replace(",","")
world["Tourism Outbound"]=world["Tourism Outbound"].str.replace(",","")
world["Health Exp/Capita"]=world["Health Exp/Capita"].str.replace(",","")
world["GDP"]=world["GDP"].str.replace(",","")

world['Tourism Inbound']=pd.to_numeric(world['Tourism Inbound'])
world['Tourism Outbound']=pd.to_numeric(world['Tourism Outbound'])
world['Health Exp/Capita']=pd.to_numeric(world['Health Exp/Capita'])
world['GDP']=pd.to_numeric(world['GDP'])
world['Business Tax Rate']=pd.to_numeric(world['Business Tax Rate'])
            

country=data['Country'].unique()
data=data.drop("Country",axis=1)

scaledf=(data-world.mean())/(world.std())


clus=model.fit_predict(scaledf)

if st.button("Predict"):
    if (clus[0]==0):
        st.write("The country ",country,"is Developed")
    if (clus[0]==1):
        st.write("The country ",country,"is Devloping")
    if (clus[0]==2):
        st.write("The country ",country,"is Under-Developed")