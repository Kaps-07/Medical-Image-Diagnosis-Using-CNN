from flask import Flask, jsonify, request, redirect, session, render_template
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import pymongo
import config
from src.mri_utils import MRI
from src.xray_utils import XRAY
from src.skin_utils import SKIN
from src.database.mri_database import save_mri_prediction
from src.database.xray_database import save_xray_prediction
from src.database.skin_database import save_skin_prediction

import datetime
import base64

app = Flask(__name__)
mri_obj = MRI()
xray_obj = XRAY()
skin_obj = SKIN()

app.config['JWT_SECRET_KEY'] = "secret"
app.config["SECRET_KEY"] = "flask-session-secret"
jwt = JWTManager(app)

mongo_client = pymongo.MongoClient(config.MONGO_URL)
db = mongo_client[config.db_name]
user_collection = db[config.doctor_collection_name]

# ── Page Routes ──────────────────────────────────────────────────────────────

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")

@app.route("/register", methods=["GET"])
def register_page():
    return render_template("register.html")

@app.route("/forgot-password", methods=["GET"])
def forgot_password_page():
    return render_template("forgot_password.html")

@app.route("/predict/xray", methods=["GET"])
def predict_xray_page():
    return render_template("predict_xray.html")

@app.route("/predict/mri", methods=["GET"])
def predict_mri_page():
    return render_template("predict_mri.html")

@app.route("/predict/skin", methods=["GET"])
def predict_skin_page():
    return render_template("predict_skin.html")

# ── API Routes ───────────────────────────────────────────────────────────────

@app.route("/register", methods=["POST"])
def register():
    user_data = request.form
    doctor_name = user_data["dr_name"]
    doctor_email = user_data["dr_email"]
    medical_registration_no = user_data["med_reg_no"]
    specialization = user_data["specialization"]
    password = user_data["password"]

    responce = user_collection.find_one({"medical_registration_no": medical_registration_no})
    if not responce:
        user_collection.insert_one({
            "doctor_name": doctor_name,
            "doctor_email": doctor_email,
            "medical_registration_no": medical_registration_no,
            "specialization": specialization,
            "password": password
        })
        return jsonify({
            "status": "success",
            "message": "Doctor registered successfully."
        })
    else:
        return jsonify({
            "status": "exists",
            "message": "Doctor already registered."
        })

@app.route("/login", methods=["POST"])
def login():
    user_data = request.form
    doctor_name = user_data["dr_name"]
    password = user_data["password"]

    response = user_collection.find_one({"doctor_name": doctor_name, "password": password})
    if response:
        access_token = create_access_token(identity=doctor_name, expires_delta=datetime.timedelta(minutes=10))
        return jsonify({
            "status": "success",
            "message": "Login successful.",
            "token": access_token
        })
    else:
        return jsonify({
            "status": "failed",
            "message": "Invalid credentials."
        })

@app.route("/forgot_password", methods=["POST"])
def forgot_password():
    user_data = request.form
    doctor_name = user_data["dr_name"]
    medical_registration_no = user_data["med_reg_no"]
    new_password = user_data["new_password"]

    response = user_collection.find_one({"doctor_name": doctor_name, "medical_registration_no": medical_registration_no})
    if response:
        user_collection.update_one(
            {"medical_registration_no": medical_registration_no},
            {"$set": {"password": new_password}}
        )
        return jsonify({
            "status": "success",
            "message": "Password updated successfully."
        })
    else:
        return jsonify({
            "status": "failed",
            "message": "Invalid credentials."
        })

@app.route("/predict_mri", methods=["POST"])
@jwt_required()
def predict_mri():
    user_data = request.form
    patient_name = user_data["patient_name"]
    age = user_data["age"]
    gender = user_data["gender"]
    image_file = request.files["image_file"]
    prediction, confidence = mri_obj.predict(image_file)

    save_mri_prediction(patient_name, age, gender, image_file, prediction, confidence)
    return jsonify({
        "message": "Prediction done.",
        "prediction": prediction,
        "confidence": confidence
    })

@app.route("/predict_xray", methods=["POST"])
@jwt_required()
def predict_xray():
    user_data = request.form
    patient_name = user_data["patient_name"]
    age = user_data["age"]
    gender = user_data["gender"]
    image_file = request.files["image_file"]
    prediction, confidence = xray_obj.predict(image_file)

    save_xray_prediction(patient_name, age, gender, image_file, prediction, confidence)
    return jsonify({
        "message": "Prediction done.",
        "prediction": prediction,
        "confidence": confidence
    })

@app.route("/predict_skin", methods=["POST"])
@jwt_required()
def predict_skin():
    user_data = request.form
    patient_name = user_data["patient_name"]
    age = user_data["age"]
    gender = user_data["gender"]
    image_file = request.files["image_file"]
    prediction, confidence = skin_obj.predict(image_file)

    save_skin_prediction(patient_name, age, gender, image_file, prediction, confidence)
    return jsonify({
        "message": "Prediction done.",
        "prediction": prediction,
        "confidence": confidence
    })

if __name__ == "__main__":
    app.run(host=config.FLASK_HOST, port=config.FLASK_PORT, debug=True)
