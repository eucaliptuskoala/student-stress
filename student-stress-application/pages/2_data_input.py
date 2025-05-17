import streamlit as st

st.title("Data Input")
with st.form("user_input_form"):
    st.write("### General questions:")
    part_time_job = st.radio(
        "Do you currently have a job?",
        ["Yes", "No"],
        index=None)
    time_sleep = st.number_input("How much time do you sleep per day?", min_value=0, max_value=24, step=1)

    st.write("### PSS (Perceived Stress Scale):")
    upset_academic_affairs = st.radio(
        "How often have you felt upset due to something that happened in your academic affairs?",
        ["Never", "Almost never", "Sometimes", "Fairly often", "Very often"],
        index=None)
    nervous_academic_pressure = st.radio(
        "How often you felt nervous and stressed because of academic pressure?",
        ["Never", "Almost never", "Sometimes", "Fairly often", "Very often"],
        index=None)
    unable_cope_academic_activities = st.radio(
        "How often you felt as if you could not cope with all the mandatory academic activities? (assignments, project requirements, etc.)",
        ["Never", "Almost never", "Sometimes", "Fairly often", "Very often"],
        index=None)
    things_going_on_way = st.radio(
        "How often you felt as if things in your academic life is going on your way?",
        ["Never", "Almost never", "Sometimes", "Fairly often", "Very often"],
        index=None)
    academic_performance_top = st.radio(
        "How often you felt as if your academic performance was on top?",
        ["Never", "Almost never", "Sometimes", "Fairly often", "Very often"],
        index=None)
    angered_bad_performance = st.radio(
        "How often you got angered due to bad performance or low grades that is beyond your control?",
        ["Never", "Almost never", "Sometimes", "Fairly often", "Very often"],
        index=None)
    academic_difficulties_piling_up = st.radio(
        "How often you felt as if academic difficulties are piling up so high that you could not overcome them?",
        ["Never", "Almost never", "Sometimes", "Fairly often", "Very often"],
        index=None)
    
    st.write("### Stress resistance test:")
    never_satisfied_achievements = st.radio(
        "I am never completely satisfied with my achievements",
        ["Never", "Sometimes", "Often", "Always"],
        index=None)
    quickly_irritated_people = st.radio(
        "I am quickly irritated by other people",
        ["Never", "Sometimes", "Often", "Always"],
        index=None)
    future_gloomy = st.radio(
        "The future seems gloomy to me",
        ["Never", "Sometimes", "Often", "Always"],
        index=None)
    quickly_impatient = st.radio(
        "I quickly become impatient",
        ["Never", "Sometimes", "Often", "Always"],
        index=None)
    smoke_too_much = st.radio(
        "I smoke too much",
        ["Never", "Sometimes", "Often", "Always"],
        index=None)
    often_rushed_work = st.radio(
        "I often feel rushed in my work",
        ["Never", "Sometimes", "Often", "Always"],
        index=None)
    not_sleeping_well = st.radio(
        "I am not sleeping well",
        ["Never", "Sometimes", "Often", "Always"],
        index=None)
    find_criticism_difficult = st.radio(
        "I find criticism difficult and I don't deal with it well",
        ["Never", "Sometimes", "Often", "Always"],
        index=None)
    panic_attacks = st.radio(
        "I often have panic attacks",
        ["Never", "Sometimes", "Often", "Always"],
        index=None)
    
    st.write("### Life events:")
    changes_lifestyle = st.radio(
        "Have you had any changes in your lifestyle recently?",
        ["No", "Yes"],
        index=None)
    financial_problems = st.radio(
        "Have you had any financial problems lately?",
        ["No", "Yes"],
        index=None)
    experienced_injury = st.radio(
        "Have you experienced any injury or sickness lately?",
        ["No", "Yes"],
        index=None)
    separated_family = st.radio(
        "Have you been separated from your family/partner?",
        ["No", "Yes"],
        index=None)
    st.divider()

    submitted = st.form_submit_button("Submit")

    if submitted:
        st.session_state.user_input = {
                'part_time_job': part_time_job,
                'time_sleep': time_sleep,
                'upset_academic_affairs': upset_academic_affairs,
                'nervous_academic_pressure': nervous_academic_pressure,
                'unable_cope_academic_activities': unable_cope_academic_activities,
                'things_going_on_way': things_going_on_way,
                'academic_performance_top': academic_performance_top,
                'angered_bad_performance': angered_bad_performance,
                'academic_difficulties_piling_up': academic_difficulties_piling_up,
                'never_satisfied_achievements': never_satisfied_achievements,
                'quickly_irritated_people': quickly_irritated_people,
                'future_gloomy': future_gloomy,
                'quickly_impatient': quickly_impatient,
                'smoke_too_much': smoke_too_much,
                'often_rushed_work': often_rushed_work,
                'not_sleeping_well': not_sleeping_well,
                'find_criticism_difficult': find_criticism_difficult,
                'panic_attacks': panic_attacks,
                'changes_lifestyle': changes_lifestyle,
                'financial_problems': financial_problems,
                'experienced_injury': experienced_injury,
                'separated_family': separated_family
        }
        st.success("Data submitted! Go to the 'Results' page.")

if "user_input" in st.session_state:
    st.switch_page("pages/3_results.py")
