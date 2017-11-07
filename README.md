# faqbot
A chatbot using chatterbot and flask

## Requirements
Since this is more than an year old now, it has following dependencies
1) Chatterbot = 0.4.2
2) flask

## Setup
Grab the Natural Language Toolkit Data  using the below command
```python
python -m textblob.download_corpora
```
This will fetch and extract the data into a folder named nltk_data in HOME.

## Usage
Run the following to launch the faqbot server
```python
python server.py
```
Head over to the url in the output which will be http://127.0.0.1:5000 in a browser and start conversing
