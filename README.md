# Artificial Intelligence Project

## Project Team

This project was designed and developed by:

* **Meryem Missaoui Hajib**

  * Database design and implementation
  * Frontend development
  * Graphical user interfaces using HTML, CSS, and JavaScript

* **Mehdi Alkadi**

  * Backend development
  * Retrieval-Augmented Generation design
  * Pipeline and endpoint configuration

* **Ouafae Hmajou**

  * Database design and implementation
  * Frontend development
  * Graphical user interfaces using HTML, CSS, and JavaScript

* **Amr Agouriane**

  * Backend development
  * Retrieval-Augmented Generation design
  * Pipeline and endpoint configuration

---

## Project Overview

This project is a smart expense-management chatbot that allows users to store, manage, and query their financial data.

Users can submit expense data in two ways:

* Manually through the application's graphical interface
* In bulk by uploading a CSV file

> CSV file uploads were selected to simplify the bulk data-import process.

Once the financial data has been stored, users can interact with the chatbot and ask questions about their expenses using natural language.

For example:

```text
What is my latest transportation expense? Give me a detailed overview.
```

---

## Main Features

* Manual expense entry
* Bulk expense import using CSV files
* Persistent expense storage
* Natural-language financial queries
* Retrieval-Augmented Generation
* Interactive web-based user interface
* Detailed responses based on stored expense data

---

## Retrieval-Augmented Generation

The project implements a **Retrieval-Augmented Generation**, or **RAG**, system based on the concepts presented in Lab 6.

The RAG pipeline retrieves relevant expense records from the database and provides them as context to the language model. This allows the chatbot to generate responses based on the user's actual financial data rather than relying only on its general knowledge.

A simplified version of the process is:

```text
User Question
     ↓
Question Embedding
     ↓
Relevant Expense Retrieval
     ↓
Context Construction
     ↓
Google Gemini
     ↓
Generated Response
```

---

## Technologies Used

### Frontend

The graphical user interface was developed using:

* HTML
* CSS
* JavaScript

The interface allows users to add expenses, upload CSV files, and communicate with the chatbot.

### Backend

The backend is responsible for:

* Processing user requests
* Managing expense data
* Handling CSV file uploads
* Connecting the database to the RAG pipeline
* Communicating with the language model and embedding model
* Exposing the required application endpoints

### Database

Expense data is stored using **SQLite 3**.

The application interacts with SQLite through Python's built-in `sqlite3` module, providing lightweight and persistent local data storage.

### Artificial Intelligence Models

The project uses:

* **Google Gemini** as the main conversational language model
* **OpenAI `text-embedding-3-large`** as the embedding model

The embedding model converts expense data and user queries into numerical vector representations. These vectors are used to identify the database records that are most relevant to the user's question.

---

## Example Questions

Users can ask questions such as:

```text
What is my latest transportation expense?
```

```text
How much did I spend on food this month?
```

```text
Show me my most expensive purchase.
```

```text
Give me a detailed overview of my transportation expenses.
```

```text
Which expense category has the highest total?
```

---

## API Key Configuration

> [!IMPORTANT]
> For privacy and security reasons, the API keys used for OpenAI and Google Gemini have been removed from the source code and replaced with placeholders.

To run the project successfully, users must provide their own API keys.

The required keys are:

* OpenAI API key
* Google Gemini API key

Replace the corresponding placeholders in the project configuration before running the application.

Example:

```text
OPENAI_API_KEY=your_openai_api_key
GOOGLE_GEMINI_API_KEY=your_google_gemini_api_key
```

API keys should never be committed directly to a public GitHub repository.

It is strongly recommended to store them in:

* Environment variables
* A local `.env` file
* A secure secrets-management service

When using a `.env` file, ensure that it is included in `.gitignore`.

Example:

```gitignore
.env
```

---

## Security Notice

Never publish real API keys in source code, documentation, screenshots, commit history, or public repositories.

If an API key is accidentally exposed, it should be revoked and replaced immediately.
