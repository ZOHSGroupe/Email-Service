from flask import Flask, request, jsonify, render_template,Blueprint
from flask_cors import CORS,cross_origin
import os
from dotenv import load_dotenv
from email_ import send_email, is_valid_email
from random_secret import generate_random_code

app = Flask(__name__)
CORS(app,resources={
    r"/*/*" : {
        "origins": "*"
    }
})



load_dotenv()


def send_email_(subject, body, message: bool = False, verification_code: bool = False):
    try:
        verification_codei:str=""
        # Get JSON data from the request body
        data = request.json

        # Check if 'email' field exists in the JSON data
        if 'email' not in data:
            return jsonify({"message": "'email' field is missing in the JSON payload", "status": "error"}), 400

        if 'username' not in data:
            return jsonify({"message": "'username' field is missing in the JSON payload", "status": "error"}), 400
        if message:
            if 'message' not in data:
                return jsonify({"message": "'message' field is missing in the JSON payload", "status": "error"}), 400

        # Check if the provided email has a valid format
        if not is_valid_email(data['email']):
            return jsonify({"message": "Invalid email format", "status": "error"}), 400

        # Send the account creation failure email
        if message:
            is_sended: bool = send_email(data['email'], subject,
                                         body.format(username=data["username"], message=data["message"]), None)
            return jsonify({"message": "Email sent successfully", "status": "success"}), 200
        elif verification_code:
            verification_codei: str = generate_random_code()
            # Send the verification code email
            is_sended: bool = send_email(data['email'], subject,
                                         body.format(verification_code=verification_codei, username=data["username"]),
                                         None)
        else:
            is_sended: bool = send_email(data['email'], subject, body.format(username=data["username"]), None)
        if is_sended and verification_code:
            return jsonify({"message": "Email sent successfully", "status": "success", "code": verification_codei}), 200
        elif is_sended:
            return jsonify({"message": "Email sent successfully", "status": "success"}), 200
        else:
            return jsonify({"message": "Failed to send email", "status": "error"}), 500

    except Exception as e:
        return jsonify({"message": str(e), "status": "error"}), 500


@app.route('/', methods=['GET'])
@cross_origin()
def index():
    return jsonify({"message": "Email service work"}), 200


@app.route('/email/send-verification-code', methods=['POST'])
def send_email_to_for_code_verification():
    return send_email_(os.getenv("SUBJECT_EMAIL_CODE_VERIFICATION"), os.getenv("BODY_EMAIL_CODE_VERIFICATION"), False,
                       True)


@app.route('/email/account-pending', methods=['POST'])
def account_created_pending():
    return send_email_(os.getenv("SUBJECT_EMAIL_ACCOUNT_PENDING"), os.getenv("BODY_EMAIL_ACCOUNT_PENDING"))


@app.route('/email/account-created', methods=['POST'])
def account_created_successfully():
    return send_email_(os.getenv('SUBJECT_EMAIL_ACCOUNT_CREATE_SUCCESSFULLY'),
                       os.getenv("BODY_EMAIL_ACCOUNT_CREATE_SUCCESSFULLY"))


@app.route('/email/account-not-created', methods=['POST'])
def account_not_created_successfully():
    return send_email_(os.getenv("SUBJECT_EMAIL_PROBLEM_IN_CREATE_ACCOUNT"),
                       os.getenv('BODY_EMAIL_PROBLEM_IN_CREATE_ACCOUNT'), True)


@app.route('/email/vihecule-pending', methods=['POST'])
def vihecule_created_pending():
    return send_email_(os.getenv("SUBJECT_EMAIL_VEHICLE_PENDING"), os.getenv("BODY_EMAIL_VEHICLE_PENDING"))


@app.route('/email/vihecule-created', methods=['POST'])
def vihecule_created_successfully():
    return send_email_(os.getenv("SUBJECT_EMAIL_VEHICLE_ADDED_SUCCESSFULLY"),
                       os.getenv("BODY_EMAIL_VEHICLE_ADDED_SUCCESSFULLY"))


@app.route('/email/vihecule-not-created', methods=['POST'])
def vihecule_not_added_successfully():
    return send_email_(os.getenv("SUBJECT_EMAIL_PROBLEM_IN_CREATE_VEHICLE"),
                       os.getenv("BODY_EMAIL_PROBLEM_IN_CREATE_VEHICLE"), True)


@app.route('/email/licence-driver-pending', methods=['POST'])
def permit_created_pending():
    return send_email_(os.getenv("SUBJECT_EMAIL_PERMIT_PENDING"), os.getenv("BODY_EMAIL_PERMIT_PENDING"))


@app.route('/email/licence-driver-created', methods=['POST'])
def permit_created_successfully():
    return send_email_(os.getenv("SUBJECT_EMAIL_PERMIT_ADDED_SUCCESSFULLY"),
                       os.getenv("BODY_EMAIL_PERMIT_ADDED_SUCCESSFULLY"))


@app.route('/email/licence-driver-not-created', methods=['POST'])
def permit_not_added_successfully():
    return send_email_(os.getenv("SUBJECT_EMAIL_PROBLEM_IN_ADD_PERMIT"), os.getenv("BODY_EMAIL_PROBLEM_IN_ADD_PERMIT"),
                       True)


@app.route('/email/assurance-pending', methods=['POST'])
def assurance_created_pending():
    return send_email_(os.getenv("SUBJECT_EMAIL_ASSURANCE_PENDING"), os.getenv("BODY_EMAIL_ASSURANCE_PENDING"))


@app.route('/email/assurance-created', methods=['POST'])
def assurance_created_successfully():
    return send_email_(os.getenv("SUBJECT_EMAIL_ASSURANCE_ADDED_SUCCESSFULLY"),
                       os.getenv("BODY_EMAIL_ASSURANCE_ADDED_SUCCESSFULLY"))


@app.route('/email/assurance-not-created', methods=['POST'])
def assurance_not_added_successfully():
    return send_email_(os.getenv("SUBJECT_EMAIL_PROBLEM_IN_ADD_ASSURANCE"),
                       os.getenv("BODY_EMAIL_PROBLEM_IN_ADD_ASSURANCE"), True)


@app.route('/docs', methods=['GET'])
def get_docs():
    return render_template('swaggerui.html')


if __name__=="__main__":
     app.run(host="localhost",port=7001)