
# import urllib2
from urllib.request import urlopen


import json
import csv
import sys
from datetime import datetime
from flask import Flask, jsonify, request, render_template
from elasticsearch import Elasticsearch, helpers
import pandas as pd
import time

es = Elasticsearch()

data = pd.read_csv("hotels_with_tones.csv")
cols = list(data.columns)

D = []
for row in range(data.shape[0]):
    body = {}
    for col, key in enumerate(cols):

        body[key] = data.iloc[row, col]
    D.append(body)

# #    print(body)
#     # name=str(data.iloc[row,6])
#     D.append(body)
#     # res=es.index(index='hotel',doc_type='document',id=row,body=body)

# # retriving one Document
# # res=es.get(index='megacorp',doc_type='employee',id=3)
# # print(res["_source"])
# #
# ###work on some data####
for i in range(len(D)):

    e4 = D[i]
    try:
        res = es.index(index='hotel', doc_type='document', id=i, body=e4)
    except:
        print(f"faield to index ,{i}")

# maxInt = sys.maxsize
# while True:
#     # decrease the maxInt value by factor 10
#     # as long as the OverflowError occurs.

#     try:
#         csv.field_size_limit(maxInt)
#         break
#     except OverflowError:
#         maxInt = int(maxInt/10)

# csv.field_size_limit(maxInt)
# with open("hotels_without_tones.csv") as f:
#     reader = csv.DictReader(f)
#     res = helpers.bulk(es, reader, index='hotel', doc_type='document')


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search']

    body = {"query": {"multi_match": {
        "query": search_term, "fields": ["name", "city"]}}}

    try:
        res = es.search(index='hotel', body=body)
        return render_template('results.html', res=res, term=search_term)
    except:
        return render_template('health.html', res="ERROR: Can't find any ElasticSearch servers.")


@app.route('/health')
def health():
    urlToCall = app.config['ELASTICSEARCH_URL'] + '_cluster/health?pretty=true'
    try:
        req = urlopen.Request(urlToCall)
        res = urlopen.urlopen(req)
        return render_template('health.html', res=res.read())
    except:
        return render_template('health.html', res="ERROR: Can't find any ElasticSearch servers.")


if __name__ == '__main__':
    app.run(debug=True)
