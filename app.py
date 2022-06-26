from flask import Flask,render_template,url_for,request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger
import os

app=Flask(__name__)
Swagger(app)

model_path=os.path.abspath("models/deploy")
mle_file=model_path+'/mle_deployment_senti_model.pkl'
tfidf_file=model_path+'/tfidf_imdb.pkl'

mle = pickle.load(open(mle_file,'rb'))
tfidf_vect = pickle.load(open(tfidf_file,'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():

    if request.method == 'POST':
        Reviews = request.form['Reviews']
        data = [Reviews]
        vect = tfidf_vect.transform(data).toarray()
        my_prediction = mle.predict(vect)
    return render_template('predict.html',prediction = my_prediction)



if __name__ == '__main__':
    app.run(debug=True)