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