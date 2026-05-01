# Quote API

A small Flask API that returns random quotes. Built as a learning project for CI/CD.

![CI](https://github.com/CSmohmmadSH/quote-api/actions/workflows/ci.yml/badge.svg)

## Run locally

\`\`\`bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt
python app.py
\`\`\`

Then visit http://localhost:3000

## Endpoints

- `GET /` — returns a random quote
- `GET /health` — health check
- `GET /count` — returns how many quotes are loaded