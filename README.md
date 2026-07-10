# 🧠 NeuroGuard — Stroke Risk Prediction

NeuroGuard is a machine learning web app that estimates a patient's stroke risk
from clinical and demographic data. It was built as an academic project under
the supervision of **Dr. Bilal Ahmad** at UET Lahore (Faisalabad Campus).

The app takes inputs like age, hypertension, heart disease, average glucose
level, BMI, and smoking status, and returns a risk classification along with a
plain-language summary.

> ⚠️ **Disclaimer:** This tool is for educational and academic demonstration
> purposes only. It is **not** a medical diagnostic device and should not be
> used as a substitute for professional medical advice.

---

## 🚀 Live Demo

**[Try NeuroGuard →](#)** *(WORKING ON DEPLOYMENT!!!!!!!)*

---

## 🧩 How It Works

1. The user fills in patient details through a form.
2. The FastAPI backend receives the request and one-hot encodes the
   categorical fields (gender, work type, residence type, smoking status) to
   match the exact feature layout the model was trained on.
3. A **Random Forest Classifier**, trained with scikit-learn on a stroke
   prediction dataset, outputs a class (stroke risk / no significant risk)
   along with class probabilities.
4. The result is returned to the frontend and displayed with a risk badge and
   a breakdown of the inputs used.

---

## 🛠️ Tech Stack

| Layer      | Technology                              |
|------------|-------------------------------------------|
| Model      | scikit-learn `RandomForestClassifier`      |
| Backend    | FastAPI (Python)                           |
| Frontend   |  HTML, CSS, JavaScript    |


---

## 📂 Project Structure

```
neuroguard/
├── app.py                   # FastAPI app & routes
├── inference.py              # Model loading & prediction logic
├── random_forest_model.pkl   # Trained model
├── requirements.txt
├── app.py
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   └── index.html

```

---

## ⚙️ Running Locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Visit `http://127.0.0.1:8000`.

---

## 🐳 Docker

```bash
docker build -t neuroguard .
docker run -p 7860:7860 neuroguard
```

---

## 📊 Model

- **Algorithm:** Random Forest Classifier (100 estimators)
- **Features:** age, hypertension, heart disease, average glucose level, BMI,
  gender, marital status, work type, residence type, smoking status
- **Target:** binary stroke risk classification

---

## 🙏 Acknowledgements

Developed by **Sohaib Mehmood** (Computer Engineering, UET Lahore, Faisalabad
Campus), with supervision and guidance from **Dr. Bilal Ahmad**.

---

## 📄 License

This project is intended for academic and educational use.
