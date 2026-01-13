from flask import Flask, render_template, request
from data import scenario, options, disclaimer
from logic import process_decision

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", scenario=scenario)

@app.route("/decision")
def decision():
    return render_template("decision.html", options=options)

@app.route("/result", methods=["POST"])
def result():
    user_choice = request.form.get("choice")
    outcome = process_decision(user_choice)

    return render_template(
        "result.html",
        outcome=outcome,
        disclaimer=disclaimer
    )

if __name__ == "__main__":
    app.run(debug=True)
