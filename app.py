from flask import Flask, render_template
import joblib
from joblib import dump, load
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

app = Flask(__name__)

@app.route('/')
def index():

    # loading test data
    url = 'Resources/true_data_3sec.csv'
    test_data = pd.read_csv(url)
    input_data = test_data.drop(['Unnamed: 0'], axis=1)
    input_data = input_data.sample(5)  
    input_data
    print(input_data)
    
    # preprocessing  test data
    X = input_data.drop(['label','filename'], axis=1)
    y = input_data['label']
    X = X[X.columns.drop(list(X.filter(regex='var')))]
    X_scaler = StandardScaler().fit(X)
    X_scaled = X_scaler.transform(X)    

    #loading model
    knn = load('Model/3_sec_model_KNN.joblib')
    #knn.fit(X_scaled, y)
    print('k=3 Test Acc: %.3f' % knn.score(X_scaled, y))

    #making predictions
    predictions = knn.predict(X_scaled)
    model_output = pd.DataFrame({"Prediction": predictions, "Actual": y})
    pred_accuracy = knn.score(X_scaled, y)
    classif_report = pd.DataFrame(classification_report(y, predictions, output_dict=True)).T

    #returning model predictions 
    return render_template("index.html", result=model_output, acc=pred_accuracy, classif_report = classif_report)
    

#result will go into html pages 

    return(flask.render_template('main.html'))


if __name__ == "__main__":
    app.run(debug=True)
