import sqlite3
from typing import List, Dict

# Default database path
DB_PATH = "data/expenses.db"

# Add a Transaction
def add_transaction(db_path, description, category, amount, date, transaction_type="debit"):
    """Add a new transaction to the database."""
    if transaction_type not in ("credit", "debit"):
        raise ValueError(f"Invalid transaction type: {transaction_type}. Must be 'credit' or 'debit'.")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO transactions (description, category, amount, date, transaction_type)
        VALUES (?, ?, ?, ?, ?)
    ''', (description, category, amount, date, transaction_type))

    conn.commit()
    conn.close()


# Get All Transactions
def get_all_transactions(db_path=DB_PATH) -> List[Dict]:
    """Fetch all transactions from the database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch all rows from the transactions table
    cursor.execute('SELECT id, date, description, category, amount, transaction_type FROM transactions')
    rows = cursor.fetchall()

    conn.close()
    return [
        {
            "id": row[0],
            "date": row[1],  # Correctly mapped to date
            "description": row[2],  # Correctly mapped to description
            "category": row[3],  # Correctly mapped to category
            "amount": float(row[4]) if row[4] else 0.0,  # Correctly mapped to amount and converted to float
            "transaction_type": row[5],  # Mapped to transaction_type
        }
        for row in rows
    ]

# Update a Transaction
def update_transaction(transaction_id, description, category, amount, date, db_path=DB_PATH):
    print(f"db_path: {db_path}")  # Debugging
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE transactions
        SET description = ?, category = ?, amount = ?, date = ?
        WHERE id = ?
    ''', (description, category, amount, date, transaction_id))

    conn.commit()
    conn.close()


# Delete a Transaction
def delete_transaction(transaction_id: int, db_path=DB_PATH):
    """Delete a transaction from the database."""
    print(f"db_path: {db_path}")  # Debugging

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM transactions WHERE id = ?', (transaction_id,))

    conn.commit()
    conn.close()


# Load Corpus from Database
def load_corpus_from_db(db_path=DB_PATH):
    """Fetch transaction data from SQLite database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT description, category, amount, date, transaction_type FROM transactions")
    rows = cursor.fetchall()
    print(rows)
    conn.close()
    
    return [
        {"description": row[0], "category": row[1], "amount": row[2], "date": row[3], "transaction_type": row[4]}
        for row in rows
    ]
