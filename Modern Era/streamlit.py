import streamlit as st
import pandas as pd
import numpy as np
import streamlit_pandas as sp
@st.cache(allow_output_mutation=True)
def load_data():

    df = pd.read_csv('/Users/nandjillelola/Documents/Data Science/NBA Draft/NBA Analysis /Modern Era/nba_player_stats_years.csv')
    df = df.drop(columns= ['Rank','Season Start Year','Player ID','Team ID'])
    seasons = [
    "2012-13",
    "2013-14",
    "2014-15",
    "2015-16",
    "2016-17",
    "2017-18",
    "2018-19",
    "2019-20",
    "2020-21",
    "2021-22",
    "2022-23",
]
    
    modern = df[(df['Year'].isin(seasons))]
    
    return modern

ign_columns = ['Fg %','3-Pt Fg Made','3-Pt Fg Attempts','3-Pt Fg %','Ft Attempts','Ft %','Offensive Rebounds','Defensive Rebounds','Rebounds','Assists','Steals','Blocks','Turnovers','Personal Fouls','Points Scored','Efficency','Ast/Tov','Stl/Tov']

modern = load_data()



st.title("NBA Data Viz")
st.write() 

widgits = sp.create_widgets(modern, ignore_columns= ign_columns)
res = sp.filter_df(modern, widgits)
st.write(res)