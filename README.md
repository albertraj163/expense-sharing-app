# ExpenseSplit

A local app to track shared expenses and split bills with your group.

Runs **only on localhost** — no internet or external hosting.

## App Link

| Page | URL |
|------|-----|
| Home | http://localhost:5001 |
| Add Expense | http://localhost:5001/add |
| Balances | http://localhost:5001/summary |

> Port: **5001** · Host: **127.0.0.1** (localhost only)

## Run

```bash
pip3 install -r requirements.txt
python3 app.py
```

Or:

```bash
./run.sh
```

Then open **http://localhost:5001** in your browser.

## Features

- Add, view, and remove shared expenses
- See who paid and how much each person owes
- Balance summary with settlement suggestions
- Clean, professional UI

## Usage

1. **Add Expense** — description, amount (₹), payer, participants
2. **Expenses** — view all records
3. **Balances** — who owes whom

## Tech

- Python 3 / Flask
- SQLite (`database.db` saved locally)
