# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import request
import json
import spacy

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    corpus_clean = str(request.args.get('corpus_clean'))
    nlp = spacy.load('en_core_web_trf')
    nlp.max_length = 5000000
    corpus_parsed = nlp(corpus_clean)
    corpus_normalized = [token.lemma_ for token in corpus_parsed]
    return json.dumps({'corpus_normalized': corpus_normalized})
