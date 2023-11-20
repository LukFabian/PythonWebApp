from flask import Flask
from flask import render_template
import pandas as pd
from random import randint
from json import dumps
from plotly import utils
import plotly.express as px

app = Flask(__name__)


@app.route('/')
def root():
    json_graph = dumps(serve_df_graph(), cls=utils.PlotlyJSONEncoder)
    return render_template('index.html', graph=json_graph)


@app.route('/data')
def serve_df():
    return get_df().to_dict()


def serve_df_graph():
    fig = px.scatter(get_df(), x='a', y='b')        # creates scatter plot from dataframe
    return fig


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
