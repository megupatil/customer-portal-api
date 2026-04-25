from flask import Flask, request

from auth.login import login
from uploads.file_upload import save_file
from customers.customer_service import search_customer
from reports.report_generator import load_report
from orders.order_service import get_orders_by_email
from integrations.webhook_service import call_webhook
from payments.payment_service import generate_transaction_id
from xml.xml_parser import parse_xml
from temp.temp_file_handler import create_temp_file

app = Flask(__name__)

app.config.from_object("config")


@app.route("/")
def home():

    return "Customer Portal API Running"


# -------------------------
# LOGIN
# -------------------------

@app.route("/login", methods=["POST"])
def user_login():

    username = request.form["username"]

    password = request.form["password"]

    if login(username, password):

        return "Login Successful"

    return "Login Failed"


# -------------------------
# CUSTOMER SEARCH
# -------------------------

@app.route("/search")
def search():

    name = request.args.get("name")

    result = search_customer(name)

    return str(result)


# -------------------------
# FILE UPLOAD
# -------------------------

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]

    save_file(file.filename, file.read())

    return "Uploaded"


# -------------------------
# REPORT DESERIALIZATION
# -------------------------

@app.route("/report", methods=["POST"])
def report():

    data = request.data

    report = load_report(data)

    return str(report)


# -------------------------
# XSS VULNERABILITY
# -------------------------

@app.route("/profile")
def profile():

    name = request.args.get("name")

    return "<h1>Welcome " + name + "</h1>"


# -------------------------
# SQL INJECTION (ORDERS)
# -------------------------

@app.route("/orders")
def orders():

    email = request.args.get("email")

    start_date = request.args.get("start")

    end_date = request.args.get("end")

    results = get_orders_by_email(email, start_date, end_date)

    return str(results)


# -------------------------
# SSRF VULNERABILITY
# -------------------------

@app.route("/webhook")
def webhook():

    url = request.args.get("url")

    response = call_webhook(url)

    return response


# -------------------------
# XML PARSER (XXE)
# -------------------------

@app.route("/parse-xml", methods=["POST"])
def xml_parser():

    xml_data = request.data

    parsed = parse_xml(xml_data)

    return str(parsed)


# -------------------------
# TEMP FILE CREATION
# -------------------------

@app.route("/temp-file")
def temp_file():

    path = create_temp_file()

    return path


# -------------------------
# PAYMENT TRANSACTION
# -------------------------

@app.route("/transaction")
def transaction():

    transaction_id = generate_transaction_id()

    return transaction_id


# -------------------------
# HEALTH CHECK
# -------------------------

@app.route("/health")
def health():

    return "OK"


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
