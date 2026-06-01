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

## Run (important — do this first)

Open a terminal in this folder, then run:

```bash
./run.sh
```

Keep that terminal open. Then open in your browser:

**http://localhost:5001**

Or manually:

```bash
pip3 install -r requirements.txt
python3 app.py
```

### "Connection refused" error?

The app is not running. Run `./run.sh` first, wait for `Running on http://127.0.0.1:5001`, then refresh the browser.

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
