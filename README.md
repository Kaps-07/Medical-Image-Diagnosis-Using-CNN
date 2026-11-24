# 🏥 Medical Image Diagnosis Using CNN

An AI-powered medical image classification application built using **Python, Flask, TensorFlow, and EfficientNet-based CNN models**. The application analyzes Brain MRI, Chest X-Ray, and Skin images to generate classification predictions with confidence scores.

<p align="center">
  <img src="screenshots/home.png" alt="Medical AI Home Page" width="850"/>
</p>

## 📌 Overview

Medical Image Diagnosis Using CNN is a deep learning-based web application designed to demonstrate automated medical image classification.

The system provides three independent prediction modules:

- **Brain MRI:** Brain tumor classification.
- **Chest X-Ray:** Pneumonia detection.
- **Skin Disease:** Benign and malignant classification.

Doctors can register, log in, provide patient information, upload medical images, and view prediction results through a web interface.

The application integrates trained CNN models with a Flask backend and MongoDB Atlas for data storage.

## ✨ Features

### 1. Doctor Authentication
- Doctor registration and login.
- JWT-based authentication.
- Login session management using browser local storage.
- Logout functionality.

### 2. Brain MRI Prediction
- Upload brain MRI images.
- CNN-based tumor classification.
- Display predicted condition.
- Confidence score visualization.
- Prediction recommendation.

### 3. Chest X-Ray Prediction
- Upload chest X-ray images.
- Normal and Pneumonia classification.
- Confidence score visualization.
- Prediction recommendation.

### 4. Skin Disease Prediction
- Upload skin images.
- Benign and Malignant classification.
- Confidence score visualization.
- Prediction recommendation.

### 5. Patient Information Management
- Patient name.
- Patient age.
- Patient gender.
- Prediction-related information storage.

### 6. Interactive Dashboard
- Clean and responsive interface.
- Image preview before prediction.
- Prediction result visualization.
- Navigation between prediction modules.

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend Framework | Flask |
| Deep Learning | TensorFlow, Keras |
| Model Architecture | EfficientNet, CNN |
| Numerical Computing | NumPy |
| Image Processing | Pillow |
| Authentication | Flask-JWT-Extended |
| Database | MongoDB Atlas |
| Database Integration | PyMongo |
| Frontend | HTML, CSS, JavaScript |
| Icons | Font Awesome |
| Deployment | Render |

## 📋 Requirements

- Python 3.11
- MongoDB Atlas account
- Git
- VS Code or another Python IDE

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Kaps-07/Medical-Image-Diagnosis-Using-CNN.git
```

### 2. Navigate to the Project

```bash
cd Medical-Image-Diagnosis-Using-CNN
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

**Windows:**

```powershell
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔐 Configuration

The application uses MongoDB Atlas for database connectivity.

Create a `.env` file in the project root directory.

Add the following configuration:

```env
MONGO_URL=mongodb+srv://USERNAME:PASSWORD@YOUR_CLUSTER.mongodb.net/
```

Replace the placeholders with your MongoDB Atlas credentials.

### Database Configuration

| Database / Collection | Purpose |
|---|---|
| `Medical_Diagnosis` | Main database |
| `doctors_data_collection` | Doctor account information |
| `mri_model_data` | MRI prediction-related records |
| `xray_model_data` | X-Ray prediction-related records |
| `skin_model_data` | Skin prediction-related records |

**Important:** Never commit `.env` to GitHub. Add it to `.gitignore`.

## 🚀 Running the Application

After installing the dependencies and configuring MongoDB Atlas, start the Flask application:

```bash
python main.py
```

Open the application in your browser:

```text
http://127.0.0.1:8000
```

Register a doctor account or log in with an existing account to access the prediction modules.

## 📂 Project Structure

```text
Medical-Image-Diagnosis-Using-CNN/
│
├── artifacts/
│   ├── mri_best_model.keras
│   ├── xray_best_model.keras
│   └── skin_best_model.keras
│
├── screenshots/
│   ├── dashboard.png
│   ├── home.png
│   ├── login.png
│   └── Prediction Result.png
│
├── src/
│   └── Model and application source files
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── mri.html
│   ├── xray.html
│   └── skin.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── config.py
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

*The structure is representative; retain the actual filenames and directories from your repository.*

## 🔄 How It Works

The application follows a simple image classification workflow.

```text
           Doctor Login
                |
                v
        Medical AI Dashboard
                |
                v
       Select Prediction Module
                |
       +--------+--------+
       |        |        |
       v        v        v
      MRI     X-Ray     Skin
       |        |        |
       +--------+--------+
                |
                v
         Upload Medical Image
                |
                v
        Image Preprocessing
                |
                v
       Trained CNN / EfficientNet
                |
                v
       Image Classification
                |
                v
       Prediction + Confidence
                |
                v
        Display Prediction Result
                |
                v
          MongoDB Storage
```

### Prediction Workflow

1. The doctor logs into the application.
2. The doctor selects MRI, Chest X-Ray, or Skin Disease prediction.
3. Patient information is entered.
4. A medical image is uploaded.
5. The backend processes the uploaded image.
6. The corresponding trained deep learning model performs classification.
7. The application displays the predicted condition and confidence score.
8. Prediction-related information is stored in the configured database.

## 🔌 API Endpoints

The application exposes the following main authentication and prediction endpoints.

| Method | Endpoint | Description |
|---|---|---|
| POST | `/register` | Register a doctor |
| POST | `/login` | Authenticate a doctor |
| POST | `/predict_mri` | Perform MRI prediction |
| POST | `/predict_xray` | Perform Chest X-Ray prediction |
| POST | `/predict_skin` | Perform Skin Disease prediction |

Prediction endpoints use JWT Bearer authentication.

Example authorization header:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## 🗄️ Database Integration

MongoDB Atlas is used as the application's cloud database.

PyMongo connects the Flask application to MongoDB Atlas using the `MONGO_URL` environment variable.

The application uses separate collections for doctor information and prediction-related records.

## ☁️ Deployment

The application is deployed on **Render**, with MongoDB Atlas used for cloud database connectivity.

### Live Application

https://medical-image-diagnosis-using-cnn.onrender.com

### Deployment Configuration

| Setting | Value |
|---|---|
| Platform | Render |
| Python Version | 3.11.15 |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn main:app --timeout 300 --workers 1 --threads 1` |
| Database | MongoDB Atlas |

Configure `MONGO_URL` in Render's Environment Variables rather than committing database credentials to the repository.

## 🔒 Security

- JWT-based authentication for protected prediction requests.
- MongoDB Atlas connection through environment variables.
- `.env` excluded from Git tracking.
- Authentication and prediction requests handled through the Flask backend.

**Production improvement:** Doctor passwords should be stored using a secure password-hashing mechanism rather than plaintext.

## 🔮 Future Enhancements

- Improve model performance with larger and more diverse datasets.
- Add prediction history and report generation.
- Introduce downloadable PDF prediction reports.
- Improve authentication and authorization.
- Add additional medical image classification models.
- Enhance model evaluation and explainability.
- Improve dashboard analytics.

## ⚠️ Medical Disclaimer

This project is developed for educational and research purposes.

The model predictions are not clinically validated diagnoses and must not be used as the basis for medical treatment decisions. Always consult qualified healthcare professionals for medical evaluation and diagnosis.

## 👨‍💻 Author

**Kapil Patil**

- GitHub: [Kaps-07](https://github.com/Kaps-07)
- LinkedIn: [Kapil Patil](https://www.linkedin.com/in/kapil-patil-6b4607257/)

---

⭐ If you find this project useful, consider giving the repository a star!
