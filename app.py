import streamlit as st
import joblib
import numpy as np
from datetime import datetime
import pandas as pd
from io import BytesIO
import base64
from fpdf import FPDF
from streamlit_lottie import st_lottie
import requests

# Load Lottie animation

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# lottie_formal = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_2szgjU.json")
# Load model
model = joblib.load("autism_model.joblib")

# Page Config
st.set_page_config(page_title="Autism Detection Tool", page_icon="🧠", layout="wide")

# Read page from query param
page = st.query_params.get("page", "Home")

# Centered sidebar navigation using HTML
st.sidebar.markdown(
    """
    <style>
    .sidebar-center {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-top: 50px;
    }
    .sidebar-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .nav-item {
        font-size: 18px;
        margin: 10px 0;
    }
    .nav-item a {
        text-decoration: none;
        color: white;
    }
    </style>

    <div class="sidebar-center">
        <div class="sidebar-title">📍 Navigation</div>
        <div class="nav-item">🏠 <a href="?page=Home" target="_self">Home</a></div>
        <div class="nav-item">🧪 <a href="?page=Screening+Test" target="_self">Screening Test</a></div>
        <div class="nav-item">📊 <a href="?page=About+the+Model" target="_self">About the Model</a></div>
    </div>
    """,
    unsafe_allow_html=True
)

# CSS Styling
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .reportview-container .markdown-text-container {
        font-family: 'Segoe UI', sans-serif;
        padding: 20px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px 24px;
        border-radius: 8px;
    }
    .title-line {
        font-size: 2.5em;
        font-weight: 700;
        text-align: center;
    }
    .description {
        max-width: 800px;
        font-size: 1.1rem;
        line-height: 1.6;
        text-align: justify;
        padding: 0 10px;
        margin: auto;
    }
    </style>
""", unsafe_allow_html=True)

# Home Page
if page == "Home":
    st.markdown("<div class='title-line'>🧠 Early Autism Detection Tool</div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("aut_img.png", use_container_width=True)

    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    st.markdown('<h3 style="text-align: center;">What is Autism?</h3>', unsafe_allow_html=True)
    st.markdown("""
        <div class="description">
        Autism, or Autism Spectrum Disorder (ASD), is a developmental disorder that affects communication, behavior,
        and social interactions. Early detection plays a crucial role in providing effective care and support. Recognizing
        the signs early can help families seek interventions and therapies that improve developmental outcomes.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    st.markdown('<h3 style="text-align: center;">About This App</h3>', unsafe_allow_html=True)
    st.markdown("""
        <div class="description">
        This screening tool is designed for parents, caregivers, and educators to identify early signs of autism in toddlers.
        By answering a set of behavioral questions, users can receive an AI-powered prediction based on trained data. While
        this is not a clinical diagnosis, it can be a valuable first step in seeking professional support.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    st.image("autism_awareness.png", use_container_width=True)

elif page == "Screening Test":
    st.markdown("""
        <style>
        div[data-baseweb="select"] > div {
            text-align: center;
        }
        div[data-baseweb="radio"] label {
            justify-content: center !important;
        }
        .stSlider > div {
            padding-left: 1rem;
            padding-right: 1rem;
        }
        .stButton > button {
            margin: auto;
            display: block;
        }
        .centered-section {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'>📝 Autism Screening Questionnaire</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Please answer the following questions sincerely:</h4>", unsafe_allow_html=True)

    with st.form("autism_form"):
        options = ["Always", "Usually", "Sometimes", "Rarely", "Never"]
        col1, col2 = st.columns(2)

        with col1:
            A1 = st.selectbox("Does your child respond when their name is called?", options)
            A2 = st.selectbox("Does your child maintain eye contact during interactions?", options)
            A3 = st.selectbox("Does your child point to objects to express interest or needs?", options)
            A4 = st.selectbox("Does your child attempt to share objects or experiences with you?", options)
            A5 = st.selectbox("Does your child engage in pretend or imaginative play (e.g., using a toy phone)?", options)

        with col2:
            A6 = st.selectbox("Does your child follow your gaze or look where you point?", options)
            A7 = st.selectbox("Does your child try to comfort others when they are upset?", options)
            A8 = st.selectbox("Does your child enjoy physical affection, such as cuddles or hugs?", options)
            A9 = st.selectbox("Does your child use simple gestures (e.g., waving goodbye, nodding)?", options)
            A10 = st.selectbox("Does your child often stare into space without clear purpose?", options)

        # Title for the section
        st.markdown("<h4 style='text-align: center;'>📋 Additional Information</h4>", unsafe_allow_html=True)

        c_slider = st.columns([1, 9, 1])
        with c_slider[1]:
            Age = st.slider("Child's Age (in months)", 1, 60, 24)

        col_sex, col_jaundice, col_family = st.columns(3)
        with col_sex:
            st.markdown("<div style='text-align: center; margin-bottom: -10px;'><b>Child's Sex</b></div>", unsafe_allow_html=True)
            Sex = st.selectbox("", ["Male", "Female"], key="sex_box")

        with col_jaundice:
            st.markdown("<div style='text-align: center; margin-bottom: -10px;'><b>Had jaundice at birth?</b></div>", unsafe_allow_html=True)
            Jaundice = st.selectbox("", ["Yes", "No"], key="jaundice_box")

        with col_family:
            st.markdown("<div style='text-align: center; margin-bottom: -5px;'><b>Family history of Autism?</b></div>", unsafe_allow_html=True)
            Family_ASD = st.selectbox("", ["Yes", "No"], key="asd_box")

        c1, c2, c3 = st.columns([2, 1, 2])
        with c2:
            submitted = st.form_submit_button("🔍 Get Prediction")

    if submitted:
        def score_qchat(response, is_q10=False):
            if is_q10:
                return 1 if response in ["Always", "Usually", "Sometimes"] else 0
            return 1 if response in ["Sometimes", "Rarely", "Never"] else 0

        qchat_inputs = [A1, A2, A3, A4, A5, A6, A7, A8, A9]
        qchat_scores = [score_qchat(ans) for ans in qchat_inputs]
        qchat_scores.append(score_qchat(A10, is_q10=True))
        qchat_total = sum(qchat_scores)

        binary_map = {"Yes": 1, "No": 0}
        sex_map = {"Male": 1, "Female": 0}

        input_data = qchat_scores + [
            int(Age),
            sex_map[Sex],
            binary_map[Jaundice],
            binary_map[Family_ASD]
        ]

        input_array = np.array(input_data).reshape(1, -1)
        prediction = model.predict(input_array)[0]
        probability = model.predict_proba(input_array)[0][1]
        percent = round(probability * 100, 2)

        st.markdown("<h3 style='text-align: center;'>📢 Prediction Result</h3>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='text-align: center;'>🧠 Estimated Autism Risk: <span style='color:orange;'>{percent}%</span></h4>", unsafe_allow_html=True)
        st.markdown(f"<h5 style='text-align: center;'>🧾 Q-Chat-10 Score: <span style='color:#00BFFF;'>{qchat_total}/10</span></h5>", unsafe_allow_html=True)

        # if lottie_formal:
        #     st_lottie(lottie_formal, speed=1, reverse=False, loop=False, height=250, key="formal_lottie")

        if prediction == 1:
            # st.snow()
            st.markdown("""
            <div style="text-align:center; margin:20px 0;">
                <span style="font-size: 36px; animation: pulse 1s infinite; color: red;">🚨⚠️🚨</span>
            </div>
            <style>
            @keyframes pulse {
              0% { transform: scale(1); }
              50% { transform: scale(1.3); }
              100% { transform: scale(1); }
            </style>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style="text-align: center; padding: 15px; background-color: #5c1a1a; color: white; border-radius: 10px; font-size: 18px;">
                ⚠️ <b>High Risk of Autism Detected</b><br>
                Please consult a pediatric specialist as soon as possible.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="text-align: center; padding: 15px; background-color: #1b4332; color: white; border-radius: 10px; font-size: 18px;">
                ✅ <b>Low Risk of Autism Detected.</b><br>No immediate concerns.
            </div>
            """, unsafe_allow_html=True)
            # st.balloons()

        report_data = {
            "Question": [
                "Responds when name is called", "Maintains eye contact", "Points to objects", "Shares experiences",
                "Engages in pretend play", "Follows your gaze", "Comforts others", "Likes cuddles",
                "Uses gestures", "Stares into space", "Age (months)", "Sex", "Jaundice at birth", "Family history"
            ],
            "Answer": [
                A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, Age, Sex, Jaundice, Family_ASD
            ]
        }

        # Initialize PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="Autism Screening Report", ln=True, align='C')
        pdf.ln(10)

        pdf.set_font("Arial", '', 12)
        for q, a in zip(report_data["Question"], report_data["Answer"]):
            pdf.multi_cell(0, 10, txt=f"{q}: {a}")

        pdf.ln(5)
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, txt=f"Q-Chat-10 Score: {qchat_total}/10", ln=True)
        pdf.cell(0, 10, txt=f"Estimated Autism Risk %: {percent}%", ln=True)

        pdf_output = pdf.output(dest='S').encode('latin1')  # get PDF as bytes
        pdf_buffer = BytesIO(pdf_output)
        pdf_buffer.seek(0)

        # Encode to base64 for download
        b64_pdf = base64.b64encode(pdf_buffer.read()).decode()
        href = f"""
        <div style='text-align: center; margin-top: 20px;'>
            📄 <a href="data:application/pdf;base64,{b64_pdf}" download="autism_report.pdf" 
            style="font-size:16px; font-weight:600; color:#1E90FF;">Download PDF Report</a>
        </div>
        """
        st.markdown(href, unsafe_allow_html=True)

elif page == "About the Model":
    st.markdown("""
        <style>
            .section {
                margin-bottom: 40px;
                padding: 0 10px;
            }
            h2 {
                text-align: center;
                font-size: 28px;
                margin-bottom: 10px;
                color: #ffffff;
            }
            .section-text {
                font-size: 17px;
                line-height: 1.7;
                text-align: justify;
                color: #dddddd;
                padding: 0 20px;
            }
            .divider {
                border-bottom: 1px solid #88888833;
                margin: 30px auto;
                width: 90%;
            }
        </style>
    """, unsafe_allow_html=True)

    # Model Overview
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown("<h2>🧠 Model Overview</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class="section-text">
            Our machine learning model is designed to assist in the <b>early detection of autism</b> in toddlers using a combination of <b>behavioral screening</b> and <b>demographic inputs</b>. 
            It utilizes the responses from the <b>Q-Chat-10</b> questionnaire, along with four additional demographic factors, to predict the likelihood of autism in toddlers with high reliability.
        </div>
    </div>
    <div class="divider"></div>
    """, unsafe_allow_html=True)

    # Dataset
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown("<h2>📂 Dataset</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class="section-text">
            The model is trained on the <b>Autism Screening for Toddlers</b> dataset from Kaggle. This dataset comprises ten behavioral questions based on the Q-Chat-10 format and includes additional demographic information such as the child's age in months, biological sex, whether the child had jaundice at birth, and any known family history of autism. These combined features help create a robust foundation for predictive screening.
        </div>
    </div>
    <div class="divider"></div>
    """, unsafe_allow_html=True)

    # Model Training & Improvements
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown("<h2>🛠️ Model Training & Improvements</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class="section-text">
            Initially, the model exhibited <b>overfitting</b> and yielded an accuracy of just <b>83.4%</b> on validation data. To enhance performance, we implemented several optimizations including hyperparameter tuning for model refinement, noise reduction through thorough feature analysis, and SMOTE-based class balancing to address data imbalance. These steps resulted in a significant improvement, achieving a final validation accuracy of <b>99%</b>.
        </div>
    </div>
    <div class="divider"></div>
    """, unsafe_allow_html=True)

    # Features Used
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown("<h2>📌 Features Used</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class="section-text">
            The model leverages a mix of behavioral and demographic indicators to make predictions. The behavioral data comes from ten Q-Chat-10 questions labeled A1 through A10, while the demographic factors include the child's age in months, biological sex, presence of jaundice at birth, and any reported family history of autism. This multi-dimensional input ensures a well-rounded prediction strategy.
        </div>
    </div>
    <div class="divider"></div>
    """, unsafe_allow_html=True)

    # Model Used
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown("<h2>⚙️ Model Used</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class="section-text">
            We selected the <b>Random Forest Classifier</b> due to its superior ability to handle complex and diverse data types while reducing overfitting. It combines the results of multiple decision trees to make accurate predictions and offers valuable insights through feature importance scores. This made it an excellent choice for our goal of reliable and interpretable autism risk prediction.
        </div>
    </div>
    """, unsafe_allow_html=True)



