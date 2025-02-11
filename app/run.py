import json
import plotly
import pandas as pd

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar
#from joblib import load
from sklearn.externals import joblib

# Setting up connection to sqlite
import sqlite3

app = Flask(__name__)

def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

# load data
conn = sqlite3.connect('data/DisasterResponse.db')
# load data from database, the tablename is hardcoded in the script that performs the ETL.
df = pd.read_sql('SELECT * FROM Disaster_ETL', conn)

# load model
model = joblib.load("models/classifier.pkl")

# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():

    # extract data needed for visuals
    genre_counts = df.groupby('genre').count()['message']
    genre_names = list(genre_counts.index)
    
    aid_counts = df.groupby('aid_related').count()['message']
    aid_names = ['no', 'yes']
    
    water_counts = df.groupby('water').count()['message']
    water_names = ['no', 'yes']    
    
    # create visuals
    graphs = [
        {
            'data': [
                Bar(
                    x=genre_names,
                    y=genre_counts
                )
            ],

            'layout': {
                'title': 'Distribution of Message Genres',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Genre"
                }
            }
        },
        {
            'data': [
                Bar(
                    x=water_names,
                    y=water_counts
                )
            ],

            'layout': {
                'title': 'Distribution of Water messages',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Water"
                }
            }
        },
		{
		        'data': [
                Bar(
                    x=aid_names,
                    y=aid_counts
                )
            ],

            'layout': {
                'title': 'Distribution of aid messages',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Aid"
                }
            }
        }
		
    ]
    
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()