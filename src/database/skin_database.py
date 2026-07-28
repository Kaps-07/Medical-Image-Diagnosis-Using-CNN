import pymongo
import base64
import config

client=pymongo.MongoClient(config.MONGO_URL)
db=client[config.db_name]
data_collection=db[config.skin_collection_name]

def save_skin_prediction(patient_name,age,gender,image_file,prediction,confidence):
    image_file.seek(0)
    encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
    data_collection.insert_one({
        "patient_name":patient_name,
        "age":age,
        "gender":gender,
        "image": encoded_image,
        "prediction":prediction,
        "confidence":confidence
    })
    return