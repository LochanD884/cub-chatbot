# 🤖 CUB — Christ University Bot

# 📌 Overview
CUB (Christ University Bot) is a specialized AI-powered chatbot designed to provide precise, reliable, and student-friendly information about Christ University.
It uses Google’s Gemini LLM with clear system instructions to ensure it answers only Christ University–related queries — from admissions to attendance rules — and formats responses in clean, readable Markdown.

# 🎯 Objectives

To automate repetitive student FAQs.

To provide up-to-date information about Christ University policies.

To restrict the scope strictly to college-specific queries.

To deliver answers in a clear, structured, user-friendly format.

# 🔑 Key Features
Context-Limited Replies: Only answers questions about Christ University.

Markdown Formatting: Uses headings, bullet points, bold & italics for clean presentation.

Web Chat Interface: User-friendly chat UI built with HTML, CSS & vanilla JS.

Session Memory: Maintains conversation flow within a session.

Feedback Support: Collects user feedback for continuous improvement (future extension).

# ⚙️ How It Works
User Query: The user types a question.

Backend (Flask): Receives the input and sends it to Google Gemini.

LLM Response: Gemini returns a college-specific, Markdown-formatted answer.

Frontend Display: The bot displays the response in a styled chat bubble.

Feedback: Option to submit a rating & comment at the end.

# 📂 Components
app.py — Flask server to handle routes, API calls, and LLM integration.

index.html — Clean chat UI with input box, send button, and Markdown rendering.

.env — Stores the API key securely (excluded from Git).

requirements.txt — Python package dependencies.

# 🧩 Technologies Used
Component	Technology

Backend	Python, Flask, google-generativeai

Frontend	HTML, CSS, JavaScript, Marked.js

LLM	Google Gemini gemini-2.0-flash model

Extras	dotenv, fuzzywuzzy (for keyword checks)

# 📁 Project Workflow
Step	Description

1️⃣	Clone the repo

2️⃣	Add your Google Generative AI API key to .env

3️⃣	Install dependencies: pip install -r requirements.txt

4️⃣	Run: python app.py

5️⃣	Open in browser at http://localhost:5000

# ✅ Highlights
Restricts non-college queries: “I’m designed only to help with college-related queries for Christ University.”

Real-time Markdown parsing for rich-text answers.

Fully local, simple to deploy, and extendable with RAG or database storage.

Feedback form integrated for quality assurance.

# 🗂️ Future Scope
✅ Integrate a vector database for rulebook-based RAG (Retrieval-Augmented Generation).

✅ Store feedback and conversation logs for fine-tuning.

✅ Add authentication for admin or staff usage.

✅ Deploy on GCP, Heroku, or Render with HTTPS.

