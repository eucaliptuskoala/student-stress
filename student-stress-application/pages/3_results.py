import streamlit as st
import pandas as pd
from ordinalregressionmodel import OrdinalRegressionModel
from inferencetransform import InferenceTransform
from preprocessing import Preprocessing
from ipreprocessing import IPreprocessing 
from idata import IData
from data import Data
from decisiontreeclassifiermodel import DecisionTreeClassifierModel  

st.title("Prediction Result")

if "user_input" not in st.session_state:
    st.warning("No user input found. Please complete the survey/form first.")
    st.stop()

data_source : IData = Data()
preprocessor: IPreprocessing = Preprocessing(data_source)
transformer = InferenceTransform()

transformed_input = transformer.transform()
ordinal_model = OrdinalRegressionModel(preprocessor, transformer)

with st.spinner("Predicting stress level..."):
    st.markdown('## Ordinal Regression Model: ')
    prediction_label, prediction_prob, full_probs = ordinal_model.predict(transformed_input.iloc[0])

    st.success("Prediction complete!")

    st.subheader("Predicted Stress Level")
    st.markdown(f"**{prediction_label}** with probability **{prediction_prob:.2%}**")

    st.subheader("Probability Breakdown")
    st.dataframe(full_probs.rename(columns={0: "Probability (%)"}).style.format("{:.2%}"))

    st.divider()

dt_model = DecisionTreeClassifierModel(preprocessor, transformer)

with st.spinner("Predicting stress level with Decision Tree Model..."):
    st.markdown('## Decision Tree Model: ')

    # Pass the new data as a dict or Series to the predict method, depending on your method's expected input
    # Your DecisionTreeClassifierModel.predict expects a dict or Series with feature names matching training
    dt_prediction_label, dt_prediction_prob, dt_full_probs, dt_feedback_msgs, score = dt_model.predict(transformed_input.iloc[0])

    st.success("Decision Tree prediction complete!")

    st.subheader(f"Model Accuracy while testing: {score:.2%}")

    st.subheader("Predicted Stress Level")
    st.markdown(f"**{dt_prediction_label}** with probability **{dt_prediction_prob:.2%}**")

    st.subheader("Probability Breakdown")
    st.dataframe(dt_full_probs.style.format({"Probability": "{:.2%}"}))

    st.subheader("Feedback")
    if dt_feedback_msgs:
        for msg in dt_feedback_msgs:
            st.markdown(f"- {msg}")

    st.divider()

    if st.button("Rerun Prediction"):
        st.switch_page("app.py")
