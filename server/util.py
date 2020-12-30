# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 09:46:03 2020

@author: Akinyemi
"""

import json
import pickle
import numpy as np

__model = None
__data_columns = None


def loan_approval(Credit_History,	Total_income,	Monthly_loan_payment,	Monthly_Balance):
    load_artifacts()
    X = np.array([Credit_History,	Total_income,	Monthly_loan_payment,	Monthly_Balance])
    return int(__model.predict([X])[0])
    

def load_artifacts():
    
    global __model, __data_columns
    
    
    with open('./artifacts/Loan_prediction_model.pickle', 'rb') as f:
        __model = pickle.load(f)
        
        
    with open('./artifacts/data_columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
    
    
    
if __name__ == '__main__':
    load_artifacts()
    #print(__data_columns)
    print(loan_approval(1.0	, 6096.0	,0.605556	,5490.444444))
    print(loan_approval(0.0	,6085.0	,0.333333	,5751.666667))
    