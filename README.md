# ExpenseSplit

A local app to track shared expenses and split bills with your group.

Runs **only on your computer** — no internet or hosting needed.

## Local URL

After starting the app, open:

**http://localhost:5001**

## Quick Start

```bash
pip3 install -r requirements.txt
python3 app.py
```

Or simply:

```bash
./run.sh
```

## Features

- Add, view, and remove shared expenses
- See who paid and how much each person owes
- Balance summary with easy settlement suggestions
- Clean, professional UI

## Usage

1. **Add** — enter description, amount (₹), who paid, and participant names
2. **Home** — view all expenses
3. **Balances** — see who owes whom

## Tech

- Python / Flask
- SQLite (saved locally as `database.db`)
