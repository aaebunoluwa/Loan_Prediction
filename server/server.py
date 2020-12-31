# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 09:43:51 2020

@author: Akinyemi
"""

from flask import Flask, request, jsonify, render_template
#import util

import json
import pickle
import numpy as np
import logging
import sys
import os

__model = None
__data_columns = None


path = os.path.dirname(__file__)
artifacts = os.path.join(path, "artifacts")


def loan_approval(Credit_History,	Total_income,	Monthly_loan_payment,	Monthly_Balance):
    load_artifacts()
    X = np.array([Credit_History,	Total_income,	Monthly_loan_payment,	Monthly_Balance])
    return int(__model.predict([X])[0])
    

def load_artifacts():
    
    global __model, __data_columns
    
    
    with open(artifacts[0]+'/Loan_prediction_model.pickle', 'rb') as f:
        __model = pickle.load(f)
        
        
    with open(artifacts[0]+'/data_columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
    

app = Flask(__name__, static_url_path="/client", static_folder='../client', template_folder="../client")
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route('/', methods=['GET'])
def index():
    if request.method=="GET":
        return render_template("app.html")

@app.route('/make_prediction', methods = ['POST'])
def predict_approval():
    Credit_History = float(request.form['Credit_History'])
    Total_income = float(request.form['Total_Income'])
    Monthly_loan_payment = float(request.form['Monthly_Loan_Payment'])
    Monthly_Balance = float(request.form['Monthly_Balance'])
    
    result = loan_approval(Credit_History,	Total_income, Monthly_loan_payment,	Monthly_Balance)
    
            
    response = jsonify({
        'model_prediction': result
        })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == '__main__':
    app.run(debug = True)