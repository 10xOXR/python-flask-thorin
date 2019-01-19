import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "bear_fur_is_better"

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

@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}

    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["link"] == member_name:
                member = obj

    return render_template("member.html", member=member)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method =="POST":
        flash("Thanks {}, we have received your message!".format(request.form["name"]))
    pageTitle = "Contact"
    return render_template("contact.html", page_title=pageTitle, tab_title=pageTitle + tabTitle)

@app.route("/careers")
def careers():
    pageTitle = "Careers"
    return render_template("careers.html", page_title=pageTitle, tab_title=pageTitle + tabTitle)

if __name__ == "__main__":
    app.run(host= '0.0.0.0',
            port=os.environ.get("PORT"),
            debug=True)