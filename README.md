
# 🧠 EarlyMind: AI-Powered Autism Screening Tool

**EarlyMind** is a responsive, AI-driven web application designed to assist in the **early detection of Autism Spectrum Disorder (ASD)** in toddlers. Built with Streamlit, it empowers parents, caregivers, and educators to identify early behavioral signs based on the standardized **Q-Chat-10** questionnaire and demographic features.

## 🚀 Live Demo

🎯 **Experience EarlyMind in Action**  

Click the button to launch the live screening app: ➡️ **[EarlyMind](https://earlymindd.streamlit.app)**

## 📌 Features

- 📄 Q-Chat-10 questionnaire-based screening  
- 🧠 AI model trained on 7000+ toddler samples  
- 📊 99% validation accuracy  
- 💡 Behavioral + Demographic feature fusion  
- 🔄 PDF report generation  
- 📱 Responsive UI (Dark + Light mode friendly)  
- 🔁 SMOTEENN-balanced dataset  
- ⚙️ Hyperparameter tuning + feature importance  
- 💬 Real-time feedback form in sidebar  

## 🧠 Model Training Process

1. **Initial Training** on ~1000 entries → 100% accuracy due to overfitting  
2. **Combined with 6000 new entries** → dataset of ~7000 entries  
3. Applied **undersampling** → accuracy dropped to **83.4%**  
4. Implemented **SMOTEENN** to balance and clean data  
5. Performed **hyperparameter tuning + feature analysis**  
6. ✅ Final validation accuracy: **99%**

**Model Used**: RandomForestClassifier  
**Libraries**: `scikit-learn`, `pandas`, `joblib`

## 📁 Folder Structure

```
├── app.py                      # Streamlit app
├── autism_model.joblib         # Trained model
├── requirements.txt            # All dependencies
├── README.md                   # Project overview
├── assets/
│   └── aut_img.png             # Banner or illustration
```

## 🛠️ Tech Stack

- **Frontend**: Streamlit (with custom HTML/CSS)
- **Backend**: Scikit-learn (Random Forest)
- **ML Tools**: SMOTEENN, Feature Importance, Cross-validation
- **PDF Generation**: FPDF
- **Deployment**: [Streamlit Cloud](https://earlymindd.streamlit.app)

## 📦 Installation

```bash
git clone https://github.com/yourusername/earlymind.git
cd earlymind
pip install -r requirements.txt
streamlit run app.py
```

## ✅ Dependencies (`requirements.txt`)

```
streamlit
pandas
numpy
scikit-learn
joblib
fpdf
streamlit-lottie
requests
```

## 📄 PDF Report

- Summary of answers
- Q-Chat-10 score
- Estimated autism risk %
- Click-to-download format

## 💬 Feedback Support

The sidebar includes:
- ⭐ Rating slider (1 to 5)
- 📝 Feedback text input
- ✅ Real-time submission with confirmation


## 📈 Future Scope

- Multilingual support  
- Autism risk evolution tracking  
- Doctor recommendation integration  
- Option to store feedback securely

