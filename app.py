from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key="AIzaSyCC4l6tXu0RofuR8oYFarMJuJW73XJmCJo")

def chat_with_gemini(prompt):
    """Function to interact with Gemini AI."""
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

@app.route('/')
def index():
    """Render the homepage with options."""
    return render_template('index.html')

@app.route('/ask', methods=['GET', 'POST'])
def ask():
    """Ask a study question."""
    if request.method == 'POST':
        data = request.json
        question = data.get("question")
        answer = chat_with_gemini(question)
        return jsonify({"answer": answer})
    return render_template('ask.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    """Generate a quiz."""
    if request.method == 'POST':
        data = request.json
        subject = data.get("subject")
        prompt = f"Create a 5-question quiz with multiple-choice answers on {subject}."
        quiz = chat_with_gemini(prompt)
        return jsonify({"quiz": quiz})
    return render_template('quiz.html')

@app.route('/plan', methods=['GET', 'POST'])
def plan():
    """Create a study plan."""
    if request.method == 'POST':
        data = request.json
        topic = data.get("topic")
        duration = data.get("duration")
        prompt = f"Create a {duration}-long study plan to master {topic}."
        study_plan = chat_with_gemini(prompt)
        return jsonify({"study_plan": study_plan})
    return render_template('plan.html')

if __name__ == '__main__':
    app.run(debug=True)
