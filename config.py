import os

image_height=224
image_width=224

mri_model_path=os.path.join(os.getcwd(),"artifacts","mri_best_model.keras")
xray_model_path=os.path.join(os.getcwd(),"artifacts","xray_best_model.keras")
skin_model_path=os.path.join(os.getcwd(),"artifacts","skin_best_model.keras")