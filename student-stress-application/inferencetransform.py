import pandas as pd
import streamlit as st

class InferenceTransform:
    def transform(self):
        user_input = st.session_state.get("user_input")
        new_data = pd.DataFrame([user_input])

        new_data["part_time_job"] = new_data["part_time_job"].map({'No': 0, 'Yes': 1}).astype(int)
        new_data["upset_academic_affairs"] = new_data["upset_academic_affairs"].map({'Never': 0, 'Almost never': 1, 'Sometimes': 2, 'Fairly often': 3, 'Very often': 4}).astype(int)
        new_data["nervous_academic_pressure"] = new_data["nervous_academic_pressure"].map({'Never': 0, 'Almost never': 1, 'Sometimes': 2, 'Fairly often': 3, 'Very often': 4}).astype(int)
        new_data["unable_cope_academic_activities"] = new_data["unable_cope_academic_activities"].map({'Never': 0, 'Almost never': 1, 'Sometimes': 2, 'Fairly often': 3, 'Very often': 4}).astype(int)
        new_data["things_going_on_way"] = new_data["things_going_on_way"].map({'Never': 0, 'Almost never': 1, 'Sometimes': 2, 'Fairly often': 3, 'Very often': 4}).astype(int)
        new_data["academic_performance_top"] = new_data["academic_performance_top"].map({'Never': 0, 'Almost never': 1, 'Sometimes': 2, 'Fairly often': 3, 'Very often': 4}).astype(int)
        new_data["angered_bad_performance"] = new_data["angered_bad_performance"].map({'Never': 0, 'Almost never': 1, 'Sometimes': 2, 'Fairly often': 3, 'Very often': 4}).astype(int)
        new_data["academic_difficulties_piling_up"] = new_data["academic_difficulties_piling_up"].map({'Never': 0, 'Almost never': 1, 'Sometimes': 2, 'Fairly often': 3, 'Very often': 4}).astype(int)

        new_data["never_satisfied_achievements"] = new_data["never_satisfied_achievements"].map({'Never': 0, 'Sometimes': 1, 'Often': 2, 'Always': 3}).astype(int)
        new_data["quickly_irritated_people"] = new_data["quickly_irritated_people"].map({'Never': 0, 'Sometimes': 1, 'Often': 2, 'Always': 3}).astype(int)
        new_data["future_gloomy"] = new_data["future_gloomy"].map({'Never': 0, 'Sometimes': 1, 'Often': 2, 'Always': 3}).astype(int)
        new_data["quickly_impatient"] = new_data["quickly_impatient"].map({'Never': 0, 'Sometimes': 1, 'Often': 2, 'Always': 3}).astype(int)
        new_data["smoke_too_much"] = new_data["smoke_too_much"].map({'Never': 0, 'Sometimes': 1, 'Often': 2, 'Always': 3}).astype(int)
        new_data["often_rushed_work"] = new_data["often_rushed_work"].map({'Never': 0, 'Sometimes': 1, 'Often': 2, 'Always': 3}).astype(int)
        new_data["not_sleeping_well"] = new_data["not_sleeping_well"].map({'Never': 0, 'Sometimes': 1, 'Often': 2, 'Always': 3}).astype(int)
        new_data["find_criticism_difficult"] = new_data["find_criticism_difficult"].map({'Never': 0, 'Sometimes': 1, 'Often': 2, 'Always': 3}).astype(int)
        new_data["panic_attacks"] = new_data["panic_attacks"].map({'Never': 0, 'Sometimes': 1, 'Often': 2, 'Always': 3}).astype(int)

        new_data["changes_lifestyle"] = new_data["changes_lifestyle"].map({'No': 0, 'Yes': 1}).astype(int)
        new_data["financial_problems"] = new_data["financial_problems"].map({'No': 0, 'Yes': 1}).astype(int)
        new_data["experienced_injury"] = new_data["experienced_injury"].map({'No': 0, 'Yes': 1}).astype(int)
        new_data["separated_family"] = new_data["separated_family"].map({'No': 0, 'Yes': 1}).astype(int)

        return new_data