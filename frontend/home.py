if page == "Home":
    st.query_params.update(page="Home")
    st.markdown("""
        <style>
            .title-line {
                font-size: 38px;
                font-weight: bold;
                text-align: center;
                margin-bottom: 10px;
                letter-spacing: 1px;
                background: linear-gradient(90deg, #ff6ec4, #7873f5);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .subtitle {
                font-size: 20px;
                font-weight: 500;
                text-align: center;
                color: #bbbbbb;
                margin-bottom: 35px;
            }
            .section-heading {
                text-align: center;
                font-size: 24px;
                color: #ffffff;
                margin-top: 40px;
                margin-bottom: 15px;
                font-weight: 600;
            }
            .description {
                text-align: justify;
                font-size: 17px;
                line-height: 1.7;
                color: #dddddd;
                padding: 0 20px;
            }
            .divider {
                border-bottom: 1px solid #88888833;
                margin: 40px auto;
                width: 90%;
            }
            .feature-list {
                list-style: none;
                padding-left: 0;
                font-size: 17px;
                color: #dddddd;
                line-height: 1.8;
            }
            .feature-list li::before {
                content: "✅ ";
            }
            .faq-list li::before {
                content: "❓ ";
            }
            .cta-button {
                display: flex;
                justify-content: center;
                margin-top: 40px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Title & Tagline
    st.markdown("<div class='title-line'>🧠 EarlyMind</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Your AI Companion for Early Autism Awareness</div>", unsafe_allow_html=True)

    # About EarlyMind
    st.markdown("<div class='section-heading'>About EarlyMind</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class="description">
            <b>EarlyMind</b> is an AI-powered screening tool developed to help parents, caregivers, and educators recognize early signs of autism in toddlers.
            By answering a set of behavioral questions inspired by the Q-Chat-10 questionnaire, users receive instant, research-backed predictions. 
            Although not a substitute for a professional diagnosis, EarlyMind offers a supportive first step toward seeking timely intervention and expert help.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # What is Autism? (Fixed Layout)
    st.markdown("<div class='section-heading'>What is Autism?</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("aut_img.png", use_container_width=True)

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    st.markdown("""
        <div class="description">
            Autism, or Autism Spectrum Disorder (ASD), is a neurodevelopmental condition that affects communication, behavior, and social interaction.
            The signs of autism typically appear early in life and vary widely from child to child. Recognizing these signs as early as possible
            can make a significant difference. Early interventions and therapies have been shown to greatly improve outcomes and quality of life
            for individuals on the spectrum.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # How It Works
    st.markdown("<div class='section-heading'>How EarlyMind Works</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class="description">
            <b>Step 1 – Screening:</b> Answer a set of short behavioral and demographic questions.<br>
            <b>Step 2 – AI Prediction:</b> Our model evaluates the responses based on Q-Chat-10 scoring logic.<br>
            <b>Step 3 – Result:</b> You receive an autism likelihood score with next-step guidance.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # Explore EarlyMind – Title
    # Section Title
    st.markdown("<div class='section-heading'>Explore EarlyMind</div>", unsafe_allow_html=True)
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    # Centered container layout
    outer_left, center_col, outer_right = st.columns([1, 4, 1])

    with center_col:
        inner_col1, inner_col2 = st.columns(2)

        with inner_col1:
            st.markdown("""
                <h4 style='font-size: 22px; text-align: center;'>🔑 Key Features</h4>
                <ul style='font-size: 16px; line-height: 1.8; color: #dddddd; list-style: none; padding-left: 0;'>
                    <li>✅ AI-Powered Prediction</li>
                    <li>✅ Research-Backed Dataset</li>
                    <li>✅ Behavioral + Demographic Screening</li>
                    <li>✅ Simple Language & Mobile-Friendly UI</li>
                    <li>✅ No Data Stored – 100% Privacy</li>
                </ul>
            """, unsafe_allow_html=True)

        with inner_col2:
            st.markdown("""
                <h4 style='font-size: 22px; text-align: center;'>❓ FAQs</h4>
                <ul style='font-size: 16px; line-height: 1.8; color: #dddddd; list-style: none; padding-left: 0;'>
                    <li><b>❓ Is this a clinical diagnosis?</b><br>– No. This is a screening tool, not a substitute for medical evaluation.</li>
                    <li><b>❓ Is my data stored?</b><br>– No. We do not store any of your responses.</li>
                    <li><b>❓ Who can use EarlyMind?</b><br>– Parents, teachers, or caregivers looking to raise awareness.</li>
                </ul>
            """, unsafe_allow_html=True)


    # CTA Button
    st.markdown("<div class='section-heading'>Ready to Begin?</div>", unsafe_allow_html=True)
    # Center-align button using full-width container + native button logic
    st.markdown("""
        <style>
        .center-btn-wrapper {
            text-align: center;
            margin-top: 0px;
            margin-bottom: 10px;
        }
        .center-btn-wrapper button {
            background: linear-gradient(90deg, #a18cd1, #fbc2eb);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: 500;
            cursor: pointer;
        }
        .center-btn-wrapper button:hover {
            background: linear-gradient(90deg, #fbc2eb, #a18cd1);
        }
        </style>

        <div class="center-btn-wrapper">
            <form action="/" method="get">
                <input type="hidden" name="page" value="Screening Test">
                <button type="submit">🧠 Start Screening Now</button>
            </form>
        </div>
    """, unsafe_allow_html=True)
