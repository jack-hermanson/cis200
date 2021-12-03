from flask import Blueprint, render_template, jsonify, request, url_for
from time import sleep

contact = Blueprint("contact", __name__, url_prefix="/contact")


@contact.route("/")
def index(success: bool or None = None):
    return render_template("contact/index.html", success=success)


@contact.route("/", methods=["POST"])
def submit_contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    number = request.form.get("number")

    failed_test = False
    try:
        parsed_number = int(number)
        if parsed_number >= 0:
            failed_test = True
    except ValueError:
        failed_test = True

    if failed_test:
        contact_route = url_for('contact.index')
        sleep(1)
        return f"""
        <p>You failed the bot test. If you're a human, please click the back button or click <a href="{contact_route}">here</a> to try again.</p>
        <p>Make sure you enter a <b>negative number</b>.</p>
        """

    # Todo: connect with an email account to actually send the emails
    return index(True)
