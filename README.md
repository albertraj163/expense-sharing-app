# Expense Sharing App

A full-stack Flask app to track shared expenses and calculate who owes whom.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/albertraj163/expense-sharing-app)

**Repository:** https://github.com/albertraj163/expense-sharing-app

## Features

- Add shared expenses with description, amount, payer, and participants
- View all expenses with per-person split amounts
- Balance summary showing who should receive or owes money
- Suggested settlements to minimize transactions
- Delete expenses
- Responsive dark-theme UI

## Local Setup

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000

## Deploy for Free

This repo includes a `render.yaml` blueprint for [Render's free tier](https://render.com/docs/free):

1. Push this repo to GitHub
2. Go to [dashboard.render.com/blueprints](https://dashboard.render.com/blueprints)
3. Click **New Blueprint Instance** and connect this repository
4. Render will deploy automatically — your app gets a public URL like `https://expense-sharing-app.onrender.com`

## Usage

1. **Add Expense** — enter a description, total amount, who paid, and comma-separated participant names
2. **Expenses** — view all recorded expenses
3. **Balances** — see net balances and suggested payments to settle up

## Tech Stack

- Python / Flask
- SQLite (via Flask-SQLAlchemy)
- Gunicorn (production server)
