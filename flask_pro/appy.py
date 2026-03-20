from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

messages = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/manual")
def manual():
    return render_template("manual.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if  request.method == "POST":
        email = request.form.get("email")
        message = request.form.get("message")

        data = {
            "email": email,
            "message": message
        }

        messages.append(data)

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(messages, f, ensure_ascii=False, indent=4)

        return redirect(url_for("home"))

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
