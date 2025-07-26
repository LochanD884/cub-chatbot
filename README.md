# 🤖 CUB — Christ University Bot
A college-specific AI chatbot built to answer queries exclusively related to Christ University using Gemini Pro with a custom UI and strict system instructions.

## 📌 Overview
CUB (Christ University Bot) is a web-based chatbot designed to assist students and visitors by providing clear, reliable, and formatted responses about Christ University's processes, policies, and academic 
details.

Unlike general-purpose bots, CUB is tightly scoped — it refuses to answer questions outside of Christ University and formats all replies using readable Markdown (headings, bullet points, bold, etc.).

## ✨ Features
🎯 Strictly Christ University Only,

📖 Answers based on Gemini Pro's training + rules,

🧠 Maintains chat context within session,

📝 Markdown-styled responses for readability,

🚫 Refuses off-topic questions,

📤 Feedback system for future enhancements,

🌐 Clean, responsive chat interface.

## 🛠️ Tech Stack
### Layer	Tools Used
**Frontend**:	HTML, CSS, JavaScript, Marked.js,

**Backend**:	Python Flask, Google Generative AI SDK,

**AI Model**:	Gemini Pro (via google.generativeai),

**Env Handling**:	python-dotenv.

## 🧩 Project Structure
```
CUB/
├── static/
│   └── script.js
├── templates/
│   └── index.html
├── app.py
├── .env
├── requirements.txt
└── README.md
```

## 🚀 How to Run Locally
### 1. Clone the Repo
```
git clone https://github.com/your-username/CUB-Christ-University-Bot.git
cd CUB-Christ-University-Bot
```
### 2. Install Requirements
```
pip install -r requirements.txt
```
### 3. Set Up Your API Key
Create a .env file in the root folder:

```GOOGLE_API_KEY=your_api_key_here```

Get your key from Google AI Studio.

### 4. Run the App
``` python app.py ```

Now open your browser at ```http://localhost:5000```

### 🎯 Bot Behavior (Gemini System Instructions)
#### Identity: 
*CUB — Christ University Bot*

#### Behavior:

Answers only Christ University–related queries,

Responds with Markdown-formatted replies,

Refuses to answer anything outside scope,

#### Sample refusal:

```“I'm designed only to help with college-related queries for Christ University.”```

## 📬 Feedback Feature
After chat, users can:

Rate the conversation,

Leave optional comments,

(Stored or logged — optional to plug into a database or Google Sheet.)

## 🧠 Future Improvements
 Integrate PDF rulebooks using RAG (Retrieval-Augmented Generation),

 Store chat history in a database,

 User authentication,

 Admin dashboard for monitoring queries & feedback,

 Deploy to Heroku/Render.
