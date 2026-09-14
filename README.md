# IBM Datathon 2023 — text normalization API

A small Flask service created as supporting infrastructure for the 2023 IBM datathon work. It accepts a text corpus and returns spaCy lemmas for downstream analysis.

> **Repository status:** historical datathon utility. The associated analysis/submission lives in the separate `ibm_datathon_2023_submission` repository.

## API

Run locally:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Unix/macOS: source .venv/bin/activate
pip install -r requirements.txt
flask --app app run
```

Example request:

```text
GET /?corpus_clean=The%20students%20were%20running
```

The response is JSON containing `corpus_normalized`, a list of lemmas.

## Implementation notes

- The spaCy model is loaded once when the process starts rather than on every request.
- The model defaults to `en_core_web_sm` and can be changed with `SPACY_MODEL`.
- `SPACY_MAX_LENGTH` controls the maximum accepted corpus length.
- Missing input returns HTTP 400; oversized input returns HTTP 413.

The service is intentionally small and documents one component of the original datathon pipeline rather than acting as a general-purpose NLP API.
