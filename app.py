from flask import Flask, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    reviews = data['reviews']
    prompt = """I collected some reviews of a place I was considering visiting.
                Can you summarize the reviews for me? 
                I want pros, cons, what people particularly loved, 
                and what people particularly disliked.
                Make sure given the context of the place, reword the category headers.
                For example, if it is a restaurant or cafe, I would want to know the pros, cons,
                what dishes and drinks that are recommended and not good etc. If you can, 
                if it's a cafe, check if they have outlets and plugs."""
    prompt += "\n" + reviews

    completion = model.generate_content(
        prompt,
        generation_config={
            'temperature': 0,
            'max_output_tokens': 800
        }
    )

    return jsonify({'summary': completion.text})

if __name__ == '__main__':
    app.run(debug=True)
