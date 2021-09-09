import pandas as pd
from pymongo import MongoClient
import matplotlib.pyplot as plt
import seaborn as sns
from joblib import load
import matplotlib.pyplot as plt
import ssl
import pyautogui

#client = MongoClient("mongodb+srv://marie:Tablesimplon06@cluster0.h2acd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
#db = 



def predict(dep,agg, atm, lum, date, cat_time, journee):    
    model = load('app/static/se.joblib')
    secours = model.predict([[dep,agg, atm, lum, date, cat_time, journee]])
    return secours
	
