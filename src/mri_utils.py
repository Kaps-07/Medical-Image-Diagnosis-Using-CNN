import config
from tensorflow.keras import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input

class MRI:
    def __init__(self):
        pass

    def load_model(self):
        self.model=load_model(config.mri_model_path)
        return 

    def image_processing(self,image_file):
        img=image.load_img(image_file,target_size=(config.image_height,config.image_width))
        image_array=image.img_to_array(img)
        image_array = preprocess_input(image_array)
        image_array=np.expand_dims(image_array,axis=0)
        return image_array

    def predict(self,image_file):
        self.load_model()
        preprocessed_image=self.image_processing(image_file)
        prediction=self.model.predict(preprocessed_image)
        class_index=np.argmax(prediction)
        class_labels=["glioma","meningioma","notumor","pituitary"]
        predicted_class=class_labels[class_index]
        return predicted_class