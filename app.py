import os
import socket
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'local-dev-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    paid_by = db.Column(db.String(100), nullable=False)
    participants = db.Column(db.String(500), nullable=False)


def compute_balances(expenses):
    balances = {}
    for expense in expenses:
        people = [p.strip() for p in expense.participants.split(',') if p.strip()]
        if not people:
            continue
        share = expense.amount / len(people)
        for person in people:
            balances.setdefault(person, 0.0)
            if person == expense.paid_by.strip():
                balances[person] += expense.amount - share
            else:
                balances[person] -= share
    return balances


def compute_settlements(balances):
    creditors = []
    debtors = []
    for person, balance in balances.items():
        if balance > 0.01:
            creditors.append([person, balance])
        elif balance < -0.01:
            debtors.append([person, -balance])

    creditors.sort(key=lambda x: x[1], reverse=True)
    debtors.sort(key=lambda x: x[1], reverse=True)

    settlements = []
    i = j = 0
    while i < len(debtors) and j < len(creditors):
        amount = min(debtors[i][1], creditors[j][1])
        if amount >= 0.01:
            settlements.append({
                'from_person': debtors[i][0],
                'to_person': creditors[j][0],
                'amount': round(amount, 2),
            })
        debtors[i][1] -= amount
        creditors[j][1] -= amount
        if debtors[i][1] < 0.01:
            i += 1
        if creditors[j][1] < 0.01:
            j += 1
    return settlements


def find_free_port(start=5000):
    port = start
    while port < start + 100:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
        port += 1
    return start


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    expenses = Expense.query.order_by(Expense.id.desc()).all()
    return render_template('index.html', expenses=expenses)


@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        paid_by = request.form.get('paid_by', '').strip()
        participants = request.form.get('participants', '').strip()

        try:
            amount = float(request.form.get('amount', 0))
        except (TypeError, ValueError):
            flash('Please enter a valid amount.', 'error')
            return render_template('add_expense.html')

        if not title or not paid_by or not participants:
            flash('All fields are required.', 'error')
            return render_template('add_expense.html')

        if amount <= 0:
            flash('Amount must be greater than zero.', 'error')
            return render_template('add_expense.html')

        expense = Expense(
            title=title,
            amount=amount,
            paid_by=paid_by,
            participants=participants,
        )
        db.session.add(expense)
        db.session.commit()
        flash('Expense added successfully.', 'success')
        return redirect(url_for('index'))

    return render_template('add_expense.html')


@app.route('/delete/<int:expense_id>', methods=['POST'])
def delete_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    db.session.delete(expense)
    db.session.commit()
    flash('Expense deleted.', 'success')
    return redirect(url_for('index'))


@app.route('/summary')
def summary():
    expenses = Expense.query.all()
    balances = compute_balances(expenses)
    settlements = compute_settlements(balances)
    return render_template('summary.html', balances=balances, settlements=settlements)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', find_free_port(5001)))
    print(f'\n  ExpenseSplit running at http://localhost:{port}\n')
    app.run(host='127.0.0.1', port=port, debug=True)
