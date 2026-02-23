# Pest Detection System using Deep Learning 🐛🌾

An intelligent web-based system that automatically detects and classifies crop pests using deep learning, helping farmers and agricultural professionals identify pests and get recommended solutions.

---

## 🎯 Problem Statement

Pests significantly affect agricultural yields, leading to declines in productivity and nutrient depletion. Excessive pesticide usage often results in increased pesticide residues, disrupting the food chain and causing adverse effects on human health and the environment. Manual pest identification is time-consuming, error-prone, and requires expert knowledge.

---

## 💡 Solution

Our deep learning-based solution automates pest detection and classification to address these challenges.  
Users can upload images of pests, and the system will identify the pest type and provide comprehensive information including:

- Organic solutions  
- Chemical treatments  
- Prevention methods  

---

## 🌟 Key Features

### 👤 For Users
- Pest detection using AI from uploaded images  
- Multi-language support (English, Hindi, Bengali)  
- Pest library with detailed information  
- Query system to ask agricultural experts  
- History tracking of past detections and queries  
- Weather-based pest prediction (temperature, humidity, location)

### 🛡️ For Admins
- Dashboard with real-time analytics  
- Pest management (add, edit, delete pests)  
- User management  
- Query response system  
- Analytics charts for pest trends and system usage  

---

## 🔬 Pest Classes Detected

The model can identify **11 pest categories**:

1. Armyworms Group  
2. Corn Worms Group  
3. Small Sap-Sucking Pests  
4. Africanized Honey Bees (Killer Bees)  
5. Brown Marmorated Stink Bugs  
6. Cabbage Loopers  
7. Citrus Canker  
8. Colorado Potato Beetles  
9. Fruit Flies  
10. Tomato Hornworms  
11. Western Corn Rootworms  

---

## 🛠️ Technology Stack

### ⚙️ Backend
- Flask (Python)  
- MongoDB (PyMongo)  
- Authentication: Email/Password & Google OAuth  
- Cloudinary (image storage)

### 🧠 Machine Learning
- Custom CNN using TensorFlow/Keras  
- Image processing: Pillow, NumPy  
- Model size: ~25MB (deployment optimized)

### 🎨 Frontend
- Jinja2 HTML templates  
- Custom responsive CSS  
- Chart.js for analytics visualization

### 🔌 APIs & Integrations
- Google Gemini AI (recommendations & prediction)  
- Google OAuth (login)  
- Cloudinary (image upload)

---

## 👥 User Roles

### 👤 Regular Users
- Register/Login (Email or Google)  
- Upload pest images  
- View pest information  
- Ask questions  
- View detection history  
- Access pest library  
- Get crop recommendations

### 🛡️ Administrators
- Admin dashboard access  
- Pest database management  
- Query response  
- Analytics view  
- User management  
- Upload monitoring  

---

## 🚀 Installation Guide

### ✅ Prerequisites
- Python 3.8+  
- MongoDB (local or Atlas)  
- pip  
- Git  

---

### 📥 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Shreyashet123/pest-detection-project.git
   cd pest-detection-project