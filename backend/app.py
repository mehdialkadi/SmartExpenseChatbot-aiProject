from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from backend.database import add_transaction, get_all_transactions, update_transaction, delete_transaction
from backend.models import retrieve_and_generate  # Import the RAG pipeline function
import os
import csv

# Initialize Flask app
app = Flask(__name__)
app = Flask(__name__, template_folder="../templates")  # Adjust the path as needed
db_path = 'data/expenses.db'  # Path to SQLite database
DB_PATH = 'data/expenses.db'  # Path to SQLite database

@app.route('/')
def home():
    """Render the homepage."""
    return render_template('home.html')

@app.route('/transactions', methods=['GET', 'POST'])
def transactions():
    """Manage transactions: Add and view all."""
    message = request.args.get("message", "")
    success = request.args.get("success", "false") == "true"

    if request.method == 'POST':
        # Add transaction
        description = request.form['description']
        category = request.form['category']
        amount = float(request.form['amount'])
        date = request.form['date']

        add_transaction(db_path, description, category, amount, date)
        return redirect(url_for('transactions', message="Transaction added successfully!", success=True))

    # Fetch all transactions
    all_transactions = get_all_transactions(db_path)
    return render_template('transactions.html', transactions=all_transactions, message=message, success=success)

@app.route('/transactions/data', methods=['GET'])
def get_transactions_data():
    """Return all transactions as JSON data."""
    all_transactions = get_all_transactions(db_path)
    return jsonify(all_transactions)

@app.route('/update_transaction/<int:transaction_id>', methods=['POST'])
def update(transaction_id):
    description = request.form['description']
    category = request.form['category']
    amount = float(request.form['amount'])
    date = request.form['date']

    # Ensure DB_PATH is passed explicitly
    update_transaction(transaction_id, description, category, amount, date, db_path=DB_PATH)
    return redirect(url_for('transactions'))

@app.route('/delete_transaction/<int:transaction_id>', methods=['POST'])
def delete(transaction_id):
    """Delete a transaction."""
    delete_transaction(transaction_id, db_path=DB_PATH)
    return redirect(url_for('transactions', message="Transaction deleted successfully!", success=True))

@app.route('/upload_csv', methods=['GET', 'POST'])
def upload_csv():
    if request.method == 'GET':
        return render_template('upload_csv.html')

    file = request.files.get('file')

    if not file or file.filename == '':
        return render_template('upload_csv.html', message="No file uploaded!", success=False)

    if file.filename.endswith('.csv'):
        file_path = os.path.join('uploads', file.filename)
        os.makedirs('uploads', exist_ok=True)
        file.save(file_path)

        # Process the CSV file
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                add_transaction(
                    db_path=db_path,
                    description=row['description'],
                    category=row['category'],
                    amount=float(row['amount']),
                    date=row['date'],
                    transaction_type=row.get('transaction_type', 'debit').lower()
                )
        os.remove(file_path)
        return render_template('upload_csv.html', message="CSV file uploaded and processed successfully!", success=True)

    return render_template('upload_csv.html', message="Please upload a valid CSV file.", success=False)



@app.route('/chat', methods=['GET', 'POST'])
def chat():
    """Chatbot interface testing the RAG pipeline."""
    if request.method == 'POST':
        user_query = request.json.get('query', '')
        
        # Use the RAG pipeline to process the query
        response = retrieve_and_generate(query=user_query, db_path=db_path)

        return jsonify({"response": response})

    # Render the chat page for GET requests
    return render_template('chat.html')


@app.route('/clear_chat', methods=['POST'])
def clear_chat():
    """Clear the chatbot context (not applicable anymore)."""
    return jsonify({"message": "Chat context cleared (not in use)."})

@app.route('/test', methods=['GET'])
def test():
    return "The server is working!"

@app.route('/edit_transaction/<int:transaction_id>', methods=['GET'])
def edit_transaction(transaction_id):
    """Render the edit form for a specific transaction."""
    transaction = next(
        (t for t in get_all_transactions(db_path) if t['id'] == transaction_id), None
    )
    if not transaction:
        return "Transaction not found", 404

    return render_template('edit_transaction.html', transaction=transaction)

if __name__ == '__main__':
    app.run(debug=True)
