# Home Page
if page == "Home":
    st.markdown(
        """
        <style>
        .center {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .title-line {
            font-size: 2.5em;
            font-weight: 700;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .description {
            max-width: 800px;
            font-size: 1.1rem;
            line-height: 1.6;
            text-align: justify;
            padding: 0 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="center">', unsafe_allow_html=True)
    st.markdown('<div class="title-line">🧠 Early Autism Detection Tool</div>', unsafe_allow_html=True)
    st.image("happy_family.png", use_container_width=True)

    st.markdown('<h3 style="margin-top: 2rem; text-align: center;">What is Autism?</h3>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="description">
        Autism, or Autism Spectrum Disorder (ASD), is a developmental disorder that affects communication, behavior,
        and social interactions. Early detection plays a crucial role in providing effective care and support. Recognizing
        the signs early can help families seek interventions and therapies that improve developmental outcomes.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h3 style="margin-top: 2rem; text-align: center;">About This App</h3>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="description">
        This screening tool is designed for parents, caregivers, and educators to identify early signs of autism in toddlers.
        By answering a set of behavioral questions, users can receive an AI-powered prediction based on trained data. While
        this is not a clinical diagnosis, it can be a valuable first step in seeking professional support.
        </div>
        """,
        unsafe_allow_html=True
    )


    st.image("autism_awareness.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
