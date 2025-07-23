from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    resume = request.files['resume']
    jd = request.form['jd']
    return f"Received resume: {resume.filename} <br>JD: {jd[:200]}..."

if __name__ == '__main__':
    app.run(debug=True)
