from msilib.schema import CheckBox
from tkinter.tix import COLUMN
import streamlit as st
import pandas as pd
import plotly.express as px
import pandas_profiling 
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport
import sys
import sweetviz as sv
from dataprep.eda import create_report

option= st.sidebar.selectbox('Select one for the report',('manual','Profile Reporting','Sweetviz','DataPrep'))

st.header(option)



st.write("Welcome!")
upload=st.file_uploader("Upload file in CSV format")
if upload is not None:
    df=pd.read_csv(upload,index_col=0)

else:
    st.write("Please upload file first")    

if option=='manual':
    st.header("Preview data")
    st.write(df.head())
    st.header("Data type")
    st.write(df.dtypes) 
    st.header("rows and column")
    st.write(df.shape)
    st.header("NULL values")
    st.write(df.isna().sum())
    st.header("Duplicate values")
    st.write(df.duplicated().any())
    st.header("overall values")
    st.write(df.describe())
    st.header("Correlation")
    st.write(df.corr())


if option == 'Profile Reporting':
    profile=ProfileReport(df,explorative=True)
    #st.write(df)
    st_profile_report(profile)
    export=profile.to_html()
    st.download_button(label="Download Full Report", data=export,file_name='ProfileReport.html')    

if option=='Sweetviz':
    sweetviz_report=sv.analyze(df)
    sweetviz_report.show_html()    

if option =='DataPrep'  :
    create_report(df).show_browser()

        
else:
    st.header("PLease upload the dataset")        