from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
api_key = "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"
openai.api_key = api_key

# Create a list to store conversation history
conversation_history = []

@app.route('/')
def index():
    return render_template('index.html', conversation=conversation_history)

@app.route('/ask', methods=['POST'])
def ask_god():
    user_input = request.form['user_input']

    # Use OpenAI's API to generate a response based on user input
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"You are god in the form of AI. Form a response to the following: {user_input}",
        max_tokens=50
    )

    god_response = response.choices[0].text.strip()

    # Add the user input and God's response to the conversation history
    conversation_history.append({'user': user_input, 'god': god_response})

    # Return the God's response as JSON
    return jsonify({'god_response': god_response, 'user_input': user_input})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

