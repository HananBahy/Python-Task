# Simple-Elasticsearch-Task

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
install flask 

```
pip install flask
```

install Elasticsearch
```
pip install elasticsearch
```
download and follow the instructions to install and run Elasticsearch

[choose according to your machine](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)

## Deployment
1- Run Elasticsearch as following :
go to elasticsearch-7.3.1 folder that you have downloaded like
```
cd elasticsearch-7.3.1
```
run via cmd (on windows)
```
.\bin\elasticsearch.bat
```
2- run __init__.py
```
python __init__.py
```
## Built using 
* data from kaggle :[hotel_reviews](https://www.kaggle.com/datafiniti/hotel-reviews)
* IBM Tone Analyzer : [Waston pyrhon lib](https://cloud.ibm.com/apidocs/tone-analyzer?code=python#analyze-customer-engagement-tone)
* Elasticsearch for search Engine : [Getting started](https://medium.com/naukri-engineering/elasticsearch-tutorial-for-beginners-using-python-b9cb48edcedc)






