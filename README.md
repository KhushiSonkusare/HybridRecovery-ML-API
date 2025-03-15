# HybridRecovery ML API 🚀

A machine learning-powered Hybrid Recovery decision system that dynamically predicts and optimizes data storage strategies. This API uses a trained Linear SVM model to classify whether to use Replication or Erasure Coding for data redundancy.

---

## 🌐 API Overview
This Flask-based API predicts the optimal data redundancy mechanism based on system workload features.

### ⚙️ Features
- **ML Prediction** (Replication vs Erasure Coding)
- **Confidence Score**
- **Preprocessing & Input Validation**
- Built with **Flask** and **scikit-learn**
- Dockerized for easy deployment (optional)

---

## 🏗️ Folder Structure

```
HybridRecovery/
├── api.py                 # Main Flask app
├── saved_model/           # Trained ML models & scalers
│   ├── linear_svc_model.joblib
│   └── scaler.joblib
├── requirements.txt       # Dependencies list
├── Dockerfile             # Docker instructions
└── README.md              # Project info
```

---

## 🖇️ Prerequisites

- Python 3.10+
- Flask 3.x
- Docker (Optional for containerization)

---

## 🚀 Running Locally

### 1️⃣ Clone the repo
```bash
git clone https://github.com/yourusername/HybridRecovery.git
cd HybridRecovery
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the API
```bash
python api.py
```

API will be available at:
```
http://127.0.0.1:5000
```

---

## 🔮 API Usage

### **Prediction Endpoint**
`POST /predict`

#### ➡️ Sample Request:
```json
{
    "features": {
        "event_type_x": 1,
        "scheduling_class_x": 0,
        "priority": 5,
        "requested_cpu": 3.2,
        "requested_ram": 512,
        "requested_disk_space": 100,
        ...
        "storage_method": 1
    }
}
```

#### ✅ Successful Response:
```json
{
    "prediction": 1,
    "confidence_score": 1439.33
}
```

---

## 🐳 Docker Deployment (Optional)

### 1️⃣ Build the Docker image
```bash
docker build -t hybrid-recovery-api .
```

### 2️⃣ Run the Docker container
```bash
docker run -d -p 5000:5000 hybrid-recovery-api
```

---

## ✨ Author
- **Khushi Sonkusare**
- [Your LinkedIn](http://www.linkedin.com/in/khushi-sonkusare-3b49611b2)
