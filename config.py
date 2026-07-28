import os

FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5005

MONGO_URL = "mongodb://localhost:27017"
db_name = "Medical_Diagnosis"

doctor_collection_name = 'doctors_data_collection'
mri_collection_name = "mri_model_data"
xray_collection_name = "xray_model_data"
skin_collection_name = "skin_model_data"

image_height=224
image_width=224

mri_model_path=os.path.join(os.getcwd(),"artifacts","mri_best_model.keras")
xray_model_path=os.path.join(os.getcwd(),"artifacts","xray_best_model.keras")
skin_model_path=os.path.join(os.getcwd(),"artifacts","skin_best_model.keras")