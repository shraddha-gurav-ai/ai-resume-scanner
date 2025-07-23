from flask import Flask, render_template, request
from utils.parse_resume import extract_text_from_pdf
from utils.match_score import calculate_match_score
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    match_score = None
    if request.method == "POST":
        jd_text = request.form.get("jd")
        resume_file = request.files["resume"]

        if resume_file and jd_text:
            file_path = os.path.join(UPLOAD_FOLDER, resume_file.filename)
            resume_file.save(file_path)

            resume_text = extract_text_from_pdf(file_path)
            match_score = calculate_match_score(resume_text, jd_text)

            os.remove(file_path)  # Clean up

    return render_template("index.html", match_score=match_score)

if __name__ == "__main__":
    app.run(debug=True)

