# Medical Image Diagnosis Using CNN

An AI-powered web application for medical image diagnosis built with Flask and EfficientNet deep learning models. It supports three diagnostic modules — Chest X-Ray, Brain MRI, and Skin Disease — each backed by a trained CNN model with a clean, modern web UI.

---

## UI Screenshots

### Home Page
![Home Page](https://i.imgur.com/placeholder-home.png)

> **Hero section** — gradient background, doctor illustration, AI Powered badge, stats, and Start Diagnosis CTA.

---

### Diagnosis Selection
The home page includes a **Choose Your Diagnosis** section with three cards:

| Chest X-Ray | Brain MRI | Skin Disease |
|---|---|---|
| EfficientNet model | EfficientNet model | EfficientNet model |
| NORMAL · PNEUMONIA | Glioma · Meningioma · No Tumor · Pituitary | Benign · Malignant |

---

### Prediction Pages
Each prediction page has:
- Patient information form (name, age, gender)
- Drag & drop image upload zone with preview
- Analyze button with loading spinner
- Result panel showing detected condition, confidence score bar, and clinical recommendation

---

### Login Page
Split-layout page with feature highlights panel on the left and login form on the right. Includes remember me, forgot password link, and JWT token storage on success.

---

### Register Page
Two-column form with doctor name, email, medical registration number, specialization dropdown, password with live strength meter, and confirm password.

---

## Features

- **3 AI diagnosis modules** — Chest X-Ray, Brain MRI, Skin Disease
- **EfficientNet backbone** for all three models (224×224 input)
- **JWT authentication** — doctors register and login to get a time-limited access token
- **Patient records** — every prediction is saved to MongoDB with patient info and result
- **Drag & drop upload** — image preview before analysis
- **Live confidence bar** — animated progress bar showing model confidence
- **Clinical recommendations** — contextual advice based on prediction output
- **Forgot password** — verified via doctor name + medical registration number
- **Responsive UI** — works on desktop and mobile

---

## Project Structure

```
Medical-Image-Diagnosis-Using-CNN/
│
├── artifacts/                      # Trained Keras model files
│   ├── mri_best_model.keras
│   ├── skin_best_model.keras
│   └── xray_best_model.keras
│
├── src/
│   ├── mri_utils.py                # MRI model loader + predictor
│   ├── xray_utils.py               # X-Ray model loader + predictor
│   ├── skin_utils.py               # Skin model loader + predictor
│   └── database/
│       ├── mri_database.py         # Save MRI predictions to MongoDB
│       ├── xray_database.py        # Save X-Ray predictions to MongoDB
│       └── skin_database.py        # Save Skin predictions to MongoDB
│
├── templates/                      # Jinja2 HTML templates
│   ├── index.html                  # Home page
│   ├── login.html                  # Login page
│   ├── register.html               # Register page
│   ├── forgot_password.html        # Forgot password page
│   ├── predict_xray.html           # Chest X-Ray prediction page
│   ├── predict_mri.html            # Brain MRI prediction page
│   └── predict_skin.html           # Skin Disease prediction page
│
├── static/
│   ├── css/style.css               # All page styles
│   └── js/main.js                  # Navbar scroll highlight
│
├── config.py                       # App configuration (paths, DB, server)
├── main.py                         # Flask app — all routes
├── requirements.txt
└── README.md
```

---

## Models & Classes

### Chest X-Ray — `xray_best_model.keras`
| Class | Description |
|---|---|
| **NORMAL** | Healthy chest, no abnormality detected |
| **PNEUMONIA** | Pneumonia infection detected in lungs |

### Brain MRI — `mri_best_model.keras`
| Class | Description |
|---|---|
| **glioma** | Glioma tumour detected |
| **meningioma** | Meningioma tumour detected |
| **notumor** | No tumour present |
| **pituitary** | Pituitary tumour detected |

### Skin Disease — `skin_best_model.keras`
| Class | Description |
|---|---|
| **benign** | Non-cancerous skin condition |
| **malignant** | Cancerous / malignant lesion detected |

All three models use **EfficientNet** preprocessing (`preprocess_input`) with input size **224 × 224**.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask, Flask-JWT-Extended |
| Deep Learning | TensorFlow 2.19, Keras 3.15, EfficientNet |
| Database | MongoDB (via PyMongo) |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Icons | Font Awesome 6.5 |
| Auth | JWT (JSON Web Tokens), 10-minute expiry |

---

## API Routes

### Page Routes (GET)
| Route | Description |
|---|---|
| `GET /` | Home page |
| `GET /login` | Login page |
| `GET /register` | Register page |
| `GET /forgot-password` | Forgot password page |
| `GET /predict/xray` | Chest X-Ray prediction page |
| `GET /predict/mri` | Brain MRI prediction page |
| `GET /predict/skin` | Skin Disease prediction page |

### Auth API Routes (POST)
| Route | Fields | Description |
|---|---|---|
| `POST /register` | `dr_name`, `dr_email`, `med_reg_no`, `specialization`, `password` | Register a new doctor |
| `POST /login` | `dr_name`, `password` | Login, returns JWT token |
| `POST /forgot_password` | `dr_name`, `med_reg_no`, `new_password` | Reset password |

### Prediction API Routes (POST · JWT required)
| Route | Fields | Response |
|---|---|---|
| `POST /predict_xray` | `patient_name`, `age`, `gender`, `image_file` | `prediction`, `confidence` |
| `POST /predict_mri` | `patient_name`, `age`, `gender`, `image_file` | `prediction`, `confidence` |
| `POST /predict_skin` | `patient_name`, `age`, `gender`, `image_file` | `prediction`, `confidence` |

All prediction routes require `Authorization: Bearer <token>` header.

---

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Medical-Image-Diagnosis-Using-CNN.git
cd Medical-Image-Diagnosis-Using-CNN
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start MongoDB
Make sure MongoDB is running locally on the default port:
```bash
mongod
```

### 5. Configure the app
Edit `config.py` if needed:
```python
FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5005
MONGO_URL  = "mongodb://localhost:27017"
db_name    = "Medical_Diagnosis"
```

### 6. Run the app
```bash
python main.py
```

Open your browser at `http://localhost:5005`

---

## How It Works

```
User uploads image
      │
      ▼
Patient form filled (name, age, gender)
      │
      ▼
Frontend sends POST request with JWT token
      │
      ▼
Flask validates JWT → loads EfficientNet model
      │
      ▼
Image preprocessed to 224×224 → model.predict()
      │
      ▼
Class index → class label + confidence score
      │
      ▼
Result saved to MongoDB
      │
      ▼
JSON response → frontend renders result panel
(condition badge · confidence bar · recommendation)
```

---

## Database Collections (MongoDB)

**Database:** `Medical_Diagnosis`

| Collection | Stores |
|---|---|
| `doctors_data_collection` | Doctor name, email, medical reg. no., specialization, password |
| `mri_model_data` | Patient info + MRI prediction + confidence |
| `xray_model_data` | Patient info + X-Ray prediction + confidence |
| `skin_model_data` | Patient info + Skin prediction + confidence |

---

## Security Notes

- Passwords are currently stored as plain text — use `bcrypt` or `werkzeug.security` for production.
- JWT secret key is hardcoded — move it to an environment variable for production.
- Token expiry is set to 10 minutes.

---

## License

This project is intended for educational and research purposes in the field of medical 038098
