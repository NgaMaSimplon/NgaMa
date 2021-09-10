import pandas as pd
from pymongo import MongoClient
import matplotlib.pyplot as plt
import seaborn as sns
from joblib import load
import matplotlib.pyplot as plt
import ssl
import pyautogui


def predict(dep,agg, atm, lum, date, cat_time, journee, vacances):    
    model = load('app/static/visa.joblib')
    secours = model.predict([[dep,agg, atm, lum, date, cat_time, journee, vacances]])
    return secours
	
