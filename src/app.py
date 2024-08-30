# app.py
from flask import Flask, request, jsonify
from model import SessionLocal, Transaction
from sqlalchemy import and_

app = Flask(__name__)

@app.route('/transactions', methods=['POST'])
def create_transaction():
    session = SessionLocal()
    data = request.json
    new_transaction = Transaction(
        amount=data['amount'],
        description=data['description'],
        user_id=data['user_id'],
        country=data['country'],
        tags=data.get('tags')
    )
    session.add(new_transaction)
    session.commit()
    session.refresh(new_transaction)
    return jsonify(new_transaction.transaction_id), 201

@app.route('/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    session = SessionLocal()
    transaction = session.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    if transaction:
        return jsonify(transaction), 200
    return jsonify({"error": "Transaction not found"}), 404

@app.route('/transactions/search', methods=['GET'])
def search_transactions():
    session = SessionLocal()
    query = session.query(Transaction)
    if 'amount' in request.args:
        query = query.filter(Transaction.amount == request.args['amount'])
    if 'date_from' in request.args and 'date_to' in request.args:
        query = query.filter(and_(Transaction.date_time >= request.args['date_from'], Transaction.date_time <= request.args['date_to']))
    if 'description' in request.args:
        query = query.filter(Transaction.description.like(f"%{request.args['description']}%"))
    transactions = query.all()
    return jsonify(transactions), 200

@app.route('/transactions/report', methods=['GET'])
def generate_report():
    session = SessionLocal()
    # Example: Summary of transactions for a given period
    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')
    transactions = session.query(Transaction).filter(and_(Transaction.date_time >= date_from, Transaction.date_time <= date_to)).all()
    total_amount = sum(t.amount for t in transactions)
    return jsonify({"total_amount": total_amount, "transaction_count": len(transactions)}), 200

if __name__ == '__main__':
    app.run(debug=True)