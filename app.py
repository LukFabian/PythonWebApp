from flask import Flask
import pandas as pd
from random import randint

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/data')
def serve_df():
    return get_df().to_dict()


# get_df returns a dataframe object with two columns
def get_df():
    data = {'a': []}
    for i in range(1000):
        data['a'].append(randint(0, 100))
    df = pd.DataFrame(data)
    df['b'] = df['a'] % 10
    return df


if __name__ == '__main__':
    app.run()
