# coding: utf8
from flask import render_template, request, Blueprint, redirect, url_for, send_from_directory, current_app
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from joblib import load
import calendar


# engine = create_engine('mysql+pymysql://rafik:simplon@localhost/startups50')

# C'est ici qu'on demande à notre appli flask d'acheminer toutes les demandes d'URL à la racine vers la fonction index()
# A chaque fois qu'on ouvrira un navigateur pour accéder à l'indexe, c'est cette fonction qui sera appelé
# @app.route est un décorateur de la varibale app qui va encapsuler la fonction index() et acheminer les demande vers cette fonction


zoneA = [
    '03', '15', '43', '63', '07', '26', '38', '73', '74', '01', '42', '69', '25', '39', '70', '90', '21',
    '58', '71', '89', '24', '33', '40', '47', '64', '19', '23', '87', '16', '17', '79', '86'
]

zoneB = [
    '22', '29', '35', '56', '18', '28', '36', '37', '41', '45', '54', '55', '57', '88', '08', '10', '51', '52', '67', '68', '02', '60',
    '80', '59', '62', '14', '50', '61', '27', '76', '975', '44', '49', '53', '72', '85', '04', '05', '13', '84', '06', '83'
]

zoneC = ['77', '93', '94', '75', '78', '91', '92', '95', '11', '30',
         '34', '48', '66', '09', '12', '31', '32', '46', '65', '81', '82']

zoneAUTRE = ['2A', '2B', '971', '977', '978',
             '972', '974', '976', '986', '987', '988', '973']

controllers = Blueprint("main", __name__, url_prefix="/")


@controllers.route('/')
def index():

    return render_template('index.html')


@controllers.route('/dashboard')
def dashboard():

    return render_template('dashboard.html')


@controllers.route('/accueil')
def accueil():

    return render_template('index.html')


@controllers.route('/formulaire_predict')
def formulaire_predict():

    return render_template('formulaire_predict.html')


@controllers.route('/predict', methods=['POST', 'GET'])
def predict():

    dep = request.form['dep']
    agg = int(request.form['agg'])
    atm = int(request.form['atm'])
    lum = int(request.form['lum'])
    date_request = request.form['date']
    cat_time = int(request.form['cat_time'])
 
    vacances = int(request.form['vacances'])

  

    # convertir le type de date
    #date = datetime.date(int(date_request[0]), int(date_request[1]), int(date_request[2]))
    date = datetime.date(int(date_request[0:4]), int(
        date_request[5:7]), int(date_request[8:]))
    journee = calendar.day_name[date.weekday()]

    print(date)

    model = load('app/static/pro.joblib')

    prediction = model.predict(
        [[dep, lum, agg, atm, date, cat_time, journee, vacances]])[0]
    print(prediction)

    return render_template('predict.html', prediction=prediction, dep=dep, lum=lum, agg=agg, atm=atm, date=date,cat_time=cat_time, journee=journee)


@controllers.route('/offline')
def offline():
    return render_template("offline.html")


@controllers.route('/sw.js')
def sw():
    return send_from_directory(current_app.static_folder, "generate-sw.js")
