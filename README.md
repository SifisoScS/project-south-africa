# Project South Africa: Powered by iKhaya AI

## Overview
One-stop-shop web application to empower disadvantaged communities in South Africa with digital literacy, health education, wellness support and community engagement.

## Quickstart (development)
1. Copy `.env.example` to `.env` and fill in values (DATABASE_URL, FIREBASE_CREDENTIALS, SECRET_KEY).
2. Create a virtualenv and install requirements: `pip install -r requirements.txt`
3. Run the Flask dev server: `python run.py`
4. To run tests: `pytest -q`

## Notes
- This repo uses SQL Server connection strings (SQLAlchemy). For local dev you can use a different DB by updating `DATABASE_URL`.
- Firebase integration requires a service account JSON file. Place its path in `FIREBASE_CREDENTIALS` or set up environment variable.
