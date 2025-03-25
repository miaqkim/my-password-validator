import flask

# TODO: change this to your academic email
AUTHOR = "kimmia@sas.upenn.edu"


app = flask.Flask(__name__)


# This is a simple route to test your server


@app.route("/")
def hello():
    return f"Hello from my Password Validator! &mdash; <tt>{AUTHOR}</tt>"


# This is a sample "password validator" endpoint
# It is not yet implemented, and will return HTTP 501 in all situations


@app.route("/v1/checkPassword", methods=["POST"])
def check_password():
    data = flask.request.get_json() or {}
    pw = data.get("password", "")

    # FIXME: to be implemented
    if len(pw) < 8:
        return flask.jsonify({"valid": False, "reason": "password length must be greater than or equal to 8."}), 501

    # Check 2: At least one uppercase letter
    upper_exists = any(c.isupper() for c in pw)
    if not upper_exists:
        return flask.jsonify({"valid": False, "reason": "password must have at least 1 uppercase letter."}), 501

    # Check 3: At least one digit
    digit_exists = any(c.isdigit() for c in pw)
    if not digit_exists:
        return flask.jsonify({"valid": False, "reason": "[assword must have at least 1 digit."}), 501

    # Check 4: At least one special character from !@#$%^&*
    special_chars = "!@#$%^&*"
    special_exists = any(c in special_chars for c in pw)
    if not special_exists:
        return flask.jsonify({"valid": False, "reason": "password must have at least 1 special character."}), 501

    # All checks passed
    return flask.jsonify({"valid": True, "reason": ""}), 200
