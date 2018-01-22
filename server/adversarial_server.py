from flask import Flask
from flask_cors import CORS, cross_origin
import pandas as pd
import numpy as np
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return '{"test": "1"}'

@app.route('/drawn/<number>/<coordinates>')
def drawn(number,coordinates):
    #data = np.array([float(c) for c in coordinates.split(',')])
    df = pd.DataFrame({'number':[number],'coords':coordinates})#json.dumps(data.tolist())})
    with open('training.csv', 'a') as f:
        df.to_csv(f, header=False)
    return '{}'
    
    
@app.route('/getcomparison/<comparisonid>/<choice>')
def getcomparison(comparisonid,choice):
    
    df = pd.DataFrame({'comparisonid':[comparisonid],'choice':[choice]})
    with open('comparison_record.csv', 'a') as f:
        df.to_csv(f, header=False)
    totest = pd.read_csv('comparison_tests.csv')
    
    chosen_test = totest.iloc[np.random.randint(len(totest))]
    coords = json.loads(chosen_test.coords)
    chosen_test2 = totest.iloc[np.random.randint(len(totest))]
    coords2 = np.array(json.loads(chosen_test2.coords))
    coords2[:,0]+=400
    coords.extend(coords2.tolist())
    
    return json.dumps({'number':int(chosen_test.target), 'coords':coords})
    

