import os

FLASK_HOST = "0.0.0.0"
FLASK_PORT = 8000

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Kaps:pkp%2428feb@docdb-cluster-20260701-0629.global.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000")
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



FLASK_HOST = "0.0.0.0"
FLASK_PORT = 8000

