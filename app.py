from flask import Flask, request
from auth.login import login
from uploads.file_upload import save_file
from customers.customer_service import search_customer
from reports.report_generator import load_report

app = Flask(__name__)

app.config.from_object("config")

@app.route("/login", methods=["POST"])
def user_login():

    username = request.form["username"]

    password = request.form["password"]

    if login(username, password):

        return "Login Successful"

    return "Login Failed"


@app.route("/search")
def search():

    name = request.args.get("name")

    result = search_customer(name)

    return str(result)


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]

    save_file(file.filename, file.read())

    return "Uploaded"


@app.route("/report", methods=["POST"])
def report():

    data = request.data

    report = load_report(data)

    return str(report)


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
