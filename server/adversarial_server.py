from flask import Flask
from flask_cors import CORS, cross_origin
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return '{"test": "1"}'

@app.route('/drawn/<number>/<coordinates>')
def drawn(number,coordinates):
    data = np.array([float(c) for c in coordinates.split(',')])
    df = pd.Series([data])
    with open('my_csv.csv', 'a') as f:
        df.to_csv(f, header=False)
    return '{}'
