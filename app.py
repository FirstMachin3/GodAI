from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
api_key = "YOUR_OPENAI_KEY"
openai.api_key = api_key

# Create a list to store conversation history
conversation_history = []

@app.route('/')
def index():
    return render_template('index.html', conversation=conversation_history)

import string

@app.route('/ask', methods=['POST'])
def ask_god():
    user_input = request.form['user_input']

    # Use OpenAI's API to generate a response based on user input
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Form a response to the following as God in AI form: {user_input}",
        max_tokens=150
    )

    god_response = response.choices[0].text.strip()

    # Remove the ", god." part if it exists at the beginning of the response
    if god_response.startswith("god. "):
        god_response = god_response[len("god. "):]

    if god_response.startswith(" , "):
        god_response = god_response[len(" , "):]

    if god_response.startswith("."):
        god_response = god_response[len("."):]    


    # Add the user input and modified God's response to the conversation history
    conversation_history.append({'user': user_input, 'god': god_response})

    # Return the modified God's response as JSON
    return jsonify({'god_response': god_response, 'user_input': user_input})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

