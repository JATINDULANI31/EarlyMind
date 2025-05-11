if page == "About the Model":
    st.query_params.update(page="About the Model")
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
            Initially, the model was trained on a small dataset of around <b>1,000 entries</b> and achieved <b>100% accuracy</b>, which clearly indicated <b>overfitting</b>. 
            To address this, we combined the dataset with <b>6,000 additional entries</b> and applied basic <b>undersampling</b> to balance the classes. 
            This brought the validation accuracy down to a more realistic <b>83.4%</b>. 
            To further improve generalization, we implemented <b>SMOTEENN</b> (a hybrid of oversampling and noise reduction), along with <b>hyperparameter tuning</b> and <b>feature importance analysis</b>. 
            These enhancements significantly improved performance, resulting in a final validation accuracy of <b>99%</b>.
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
    



