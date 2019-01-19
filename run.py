import os
import json
from flask import Flask, render_template

app = Flask(__name__)

tabTitle = " | "

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    pageTitle = "About"
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title=pageTitle, tab_title=pageTitle + tabTitle, company = data)

@app.route("/contact")
def contact():
    pageTitle = "Contact"
    return render_template("contact.html", page_title=pageTitle, tab_title=pageTitle + tabTitle)

@app.route("/careers")
def careers():
    pageTitle = "Careers"
    return render_template("careers.html", page_title=pageTitle, tab_title=pageTitle + tabTitle)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=True)