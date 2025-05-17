import streamlit as st
import pandas as pd
from idata import IData
from data import Data

def main():
    st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

    st.title("Student Stress Classification")
    st.image('img/stress.png')
    st.markdown("""
    This application which uses Artificial Intelligence to classify student stress levels based on various features. " \
    "All used models were trained on the set of data, collected from students of Fontys University of Applied Sciences."
    "The models will classify your stress level, and provide useful feedback on how to improve your mental health.
    """)
    st.divider()

    if st.button("Start Stress Check"):
        st.switch_page("pages/2_data_input.py")

if __name__ == "__main__":
    main()




