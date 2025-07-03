from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from core import handle_article, handle_link

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    source_type = data.get("source_type")
    content = data.get("content")
    question = data.get("question", None)

    if not content or source_type not in ["url", "text"]:
        return jsonify({"error": "Invalid input"}), 400

    if source_type == "url":
        result = handle_link(content, question)
    else:
        result = handle_article(content, question)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

