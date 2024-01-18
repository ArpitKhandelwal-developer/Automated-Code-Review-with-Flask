# main.py

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/review_code', methods=['POST'])
def review_code():
    code = request.form.get('code')

    # Add AI-based code review logic here
    feedback = review_code_with_ai(code)

    return render_template('review_result.html', code=code, feedback=feedback)

def review_code_with_ai(code):
    # Replace this with your AI-based code review logic
    # For simplicity, let's assume a basic rule: code should not have the word "bug"
    if 'bug' in code.lower():
        return "Potential issue found: Avoid using the word 'bug' in code."
    else:
        return "Code review passed successfully."

if __name__ == '__main__':
    app.run(debug=True)
