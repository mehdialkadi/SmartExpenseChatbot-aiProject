# Artificial Intelligence Project
Project created and made by :
- Meryem Missaoui Hajib - Database Design/Implementation + Frontend Developement - GUIs (HTML + CSS + JS).
- Mehdi Alkadi - Backend Developement. RAG Design + Pipeline/Endpoint configuration.
- Ouafae Hmajou - Database Design/Implementation + Frontend Developement - GUIs (HTML + CSS + JS).
- Amr Agouriane - Backend Developement. RAG Design + Pipeline/Endpoint configuration.

The project is about a smart expense chatbot, where the user submits his financial data (either manually or in bulk via csv file upload - for the sake of simplicity -).
  - The project implement RAG (Retrieval Augmented Generation) system, as seen in the Lab 6.
  - The application interacts with the user via a GUI (Graphical User Interface) coded in HTML. Data persistance is done via SQLite3, which is a core function of python.
  - The used Chatbot is Google Gemini, and the used embedding model is OpenAI text-embedding-3-large.
  - The Chatbot lets you ask questions about all the expenses found in the database (Example: What is my latest transportation expense? Give me a detailed view.)


PS : Please note that for *privacy purposes*, the **API** keys for the chatbots ***(OpenAI - Google Gemini)*** have been *removed* from the code and replaced with placeholders. So in order for the code to run properly, ****your own API keys should be filled in****.
