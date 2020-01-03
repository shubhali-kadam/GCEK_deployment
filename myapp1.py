
from flask import Flask,render_template,request
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
import numpy as np
import pickle
app=Flask(__name__)
@app.route('/')
def hello_world():
   return render_template('appht.html')
@app.route('/predict',methods=['POST'])
def get_result():
   poly=pickle.load(open('poly.pkl','rb'))
   model=pickle.load(open('model.pkl','rb'))
   query=[[float(request.form['text2'])]]
   X_query=poly.transform(query)
   sal=model.predict(X_query)
   #use model.predict to predict salary
   return 'Dear'+request.form["text1"]+ 'Your Expected Salary after '+request.form["text2"]+'Experience is:'+str(sal);

if __name__ == '__main__':
   app.run(debug=True)
