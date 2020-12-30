# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 09:43:51 2020

@author: Akinyemi
"""

from flask import Flask, request, jsonify, render_template
import server

app = Flask(__name__, static_url_path="/client", static_folder='../client', template_folder="../client")

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
    
    response = jsonify({
        'model_prediction': server.util.loan_approval(Credit_History,	Total_income, Monthly_loan_payment,	Monthly_Balance)
        })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == '__main__':
    app.run(debug = True)