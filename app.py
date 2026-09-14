import os

import spacy
from flask import Flask, jsonify, request

app = Flask(__name__)

SPACY_MODEL = os.getenv("SPACY_MODEL", "en_core_web_sm")
nlp = spacy.load(SPACY_MODEL)
nlp.max_length = int(os.getenv("SPACY_MAX_LENGTH", "5000000"))


@app.route("/", methods=["GET", "POST"])
def normalize_corpus():
    """Lemmatize a supplied corpus for the original datathon pipeline."""
    corpus = request.values.get("corpus_clean")
    if corpus is None:
        return jsonify({"error": "missing required parameter: corpus_clean"}), 400

    if len(corpus) > nlp.max_length:
        return jsonify({"error": "corpus exceeds configured maximum length"}), 413

    parsed = nlp(corpus)
    return jsonify({"corpus_normalized": [token.lemma_ for token in parsed]})
