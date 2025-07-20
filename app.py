from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai
from fuzzywuzzy import fuzz
import os

# Environment Setup
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Flask App Setup
app = Flask(__name__)

# Generative AI Model Setup
model = genai.GenerativeModel(
    'gemini-2.0-flash',
    system_instruction="""
You are CUB — Christ University Bot.
You ONLY answer questions about Christ University.
Reply using clear Markdown: use headings, lists, bold, and italics where helpful.
If a question is NOT related to Christ University, politely reply:
"I'm designed only to help with college-related queries for Christ University."
"""
)

chat = model.start_chat(history=[])

college_keywords = [
    "CIA", "exam", "syllabus", "marks", "course", "event",
    "professor", "hostel", "campus", "placement", "fees",
    "attendance", "department", "Christ", "Christ University",
    "college", "university"
]

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json['message']

    if not is_college_related(user_message):
        return jsonify({'reply': "I'm designed only to help with college-related queries for Christ University."})

    response = chat.send_message(user_message)
    bot_reply = ''.join([part.text for part in response.parts])

    return jsonify({'reply': bot_reply})


@app.route('/feedback', methods=['POST'])
def feedback():
    rating = request.form['rating']
    comment = request.form['comment']
    print(f"Feedback received — Rating: {rating}, Comment: {comment}")
    return 'OK'

# Fuzzy Functions
def is_college_related(message):
    for keyword in college_keywords:
        if fuzz.partial_ratio(keyword.lower(), message.lower()) > 60:
            return True
    return False

# Run the app
if __name__ == '__main__':
    app.run(debug=True)