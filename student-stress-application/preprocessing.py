from idata import IData
from data import Data
from ipreprocessing import IPreprocessing
import pandas as pd

class Preprocessing(IPreprocessing):
    
    def __init__(self, data_source: IData):
        self.data_source = data_source

    def rename(self):
        student_stress = self.data_source.get_data()

        student_stress.drop(['Позначка часу'], axis=1, inplace=True)
        student_stress.rename(columns={"How much time do you spend on studying daily? (in hours)" : "time_studying"}, inplace=True)
        student_stress.rename(columns={"Would you like to pursue a career based on your profile/specialization?" : "career_pursue"}, inplace=True)
        student_stress.rename(columns={"Do you have a part time job?" : "part_time_job"}, inplace=True)
        student_stress.rename(columns={"How many hours do you usually sleep?" : "time_sleep"}, inplace=True)
        student_stress.rename(columns={"How would you describe your diet?" : "diet"}, inplace=True)
        student_stress.rename(columns={"How much time do you spend on physical activities daily (general exercises, any sport counts)?" : "time_physical_activities"}, inplace=True)
        student_stress.rename(columns={"How often have you felt upset due to something that happened in your academic affairs?" : "upset_academic_affairs"}, inplace=True)
        student_stress.rename(columns={"How often you felt as if you were unable to control important things in your academic affairs?" : "unable_control_academic_affairs"}, inplace=True)
        student_stress.rename(columns={"How often you felt nervous and stressed because of academic pressure?" : "nervous_academic_pressure"}, inplace=True)
        student_stress.rename(columns={"How often you felt as if you could not cope with all the mandatory academic activities? (assignments, project requirements, etc.)" : "unable_cope_academic_activities"}, inplace=True)
        student_stress.rename(columns={"How often you felt confident about your ability to handle your academic / university problems?" : "confident_handle_academic_problems"}, inplace=True)
        student_stress.rename(columns={"How often you felt as if things in your academic life is going on your way?" : "things_going_on_way"}, inplace=True)
        student_stress.rename(columns={"How often are you able to control irritations in your academic / university affairs?" : "control_irritations_academic_affairs"}, inplace=True)
        student_stress.rename(columns={"How often you felt as if your academic performance was on top?" : "academic_performance_top"}, inplace=True)
        student_stress.rename(columns={"How often you got angered due to bad performance or low grades that is beyond your control?" : "angered_bad_performance"}, inplace=True)
        student_stress.rename(columns={"How often you felt as if academic difficulties are piling up so high that you could not overcome them?" : "academic_difficulties_piling_up"}, inplace=True)
        student_stress.rename(columns={"I am never completely satisfied with my achievements" : "never_satisfied_achievements"}, inplace=True)
        student_stress.rename(columns={"I am quickly irritated by other people" : "quickly_irritated_people"}, inplace=True)
        student_stress.rename(columns={"The future seems gloomy to me" : "future_gloomy"}, inplace=True)
        student_stress.rename(columns={"I quickly become impatient" : "quickly_impatient"}, inplace=True)
        student_stress.rename(columns={"I smoke too much" : "smoke_too_much"}, inplace=True)
        student_stress.rename(columns={"I find it hard to think clearly when I am in a difficult situation" : "hard_think_clearly"}, inplace=True)
        student_stress.rename(columns={"I often feel rushed in my work " : "often_rushed_work"}, inplace=True)
        student_stress.rename(columns={"I am not sleeping well" : "not_sleeping_well"}, inplace=True)
        student_stress.rename(columns={"I am sensitive to noise" : "sensitive_noise"}, inplace=True)
        student_stress.rename(columns={"I find criticism difficult and I don't deal with it well" : "find_criticism_difficult"}, inplace=True)
        student_stress.rename(columns={"I often have panic attacks " : "panic_attacks"}, inplace=True)
        student_stress.rename(columns={"I have stomachaches and/or intestinal problems" : "stomachaches"}, inplace=True)
        student_stress.rename(columns={"Have you moved your house in the past 6 month?" : "moved_house"}, inplace=True)
        student_stress.rename(columns={"Have you had any changes in your lifestyle recently?" : "changes_lifestyle"}, inplace=True)
        student_stress.rename(columns={"Have you had any financial problems lately?" : "financial_problems"}, inplace=True)
        student_stress.rename(columns={"Have you had any sexual problems lately?" : "sexual_problems"}, inplace=True)
        student_stress.rename(columns={"Have any of your fellow people been sick (family member or relative) lately?" : "fellow_people_sick"}, inplace=True)
        student_stress.rename(columns={"Have you experienced any injury or sickness lately?" : "experienced_injury"}, inplace=True)
        student_stress.rename(columns={"Have you been separated from your family/partner?" : "separated_family"}, inplace=True)
        student_stress.rename(columns={"Have you experienced a death of a fellow person (close relative, partner, friend)?" : "experienced_death"}, inplace=True)
        student_stress.rename(columns={"Overall, how would you describe your stress level?" : "stress_level"}, inplace=True)

        return student_stress

    def convert_to_numeric(self):

        student_stress = self.rename()

        student_stress["career_pursue"] = student_stress["career_pursue"].str.replace("%","")
        student_stress["part_time_job"] = student_stress["part_time_job"].map({'No': 0, 'Yes': 1}).astype(int)
        student_stress["diet"] = student_stress["diet"].map({'Unhealthy': 0, 'Average': 1, 'Healthy': 2}).astype(int)

        student_stress["upset_academic_affairs"] = student_stress["upset_academic_affairs"].map({'Never': 0, 'Almost never': 1, 'Sometimes': 2, 'Fairly often': 3, 'Very often': 4}).astype(int)
        student_stress["unable_control_academic_affairs"] = student_stress["unable_control_academic_affairs"].map({'Never': 0, 'Almost never': 1, 'Sometimes': 2, 'Fairly often': 3, 'Very often': 4}).astype(int)
        student_stress["nervous_academic_pressure"] = student_stress["nervous_academic_pressure"].map({'Never': 0, 'Almost never': 1, 'Sometimes': 2, 'Fairly often': 3, 'Very often': 4}).astype(int)
        student_stress["unable_cope_academic_activities"] = student_stress["unable_cope_academic_activities"].map({'Never': 0, 'Almost never': 1, 'Sometimes': 2, 'Fairly often': 3, 'Very often': 4}).astype(int)
        student_stress["confident_handle_academic_problems"] = student_stress["confident_handle_academic_problems"].map({'Never': 0, 'Almost never': 1, 'Sometimes': 2, 'Fairly often': 3, 'Very often': 4}).astype(int)
        student_stress["things_going_on_way"] = student_stress["things_going_on_way"].map({'Never': 0, 'Almost never': 1, 'Sometimes': 2, 'Fairly often': 3, 'Very often': 4}).astype(int)
        student_stress["control_irritations_academic_affairs"] = student_stress["control_irritations_academic_affairs"].map({'Never': 0, 'Almost never': 1, 'Sometimes': 2, 'Fairly often': 3, 'Very often': 4}).astype(int)
        student_stress["academic_performance_top"] = student_stress["academic_performance_top"].map({'Never': 0, 'Almost never': 1, 'Sometimes': 2, 'Fairly often': 3, 'Very often': 4}).astype(int)
        student_stress["angered_bad_performance"] = student_stress["angered_bad_performance"].map({'Never': 0, 'Almost never': 1, 'Sometimes': 2, 'Fairly often': 3, 'Very often': 4}).astype(int)
        student_stress["academic_difficulties_piling_up"] = student_stress["academic_difficulties_piling_up"].map({'Never': 0, 'Almost never': 1, 'Sometimes': 2, 'Fairly often': 3, 'Very often': 4}).astype(int)

        student_stress["never_satisfied_achievements"] = student_stress["never_satisfied_achievements"].map({'Never': 0, 'Sometimes': 1, 'Often': 2, 'Always': 3}).astype(int)
        student_stress["quickly_irritated_people"] = student_stress["quickly_irritated_people"].map({'Never': 0, 'Sometimes': 1, 'Often': 2, 'Always': 3}).astype(int)
        student_stress["future_gloomy"] = student_stress["future_gloomy"].map({'Never': 0, 'Sometimes': 1, 'Often': 2, 'Always': 3}).astype(int)
        student_stress["quickly_impatient"] = student_stress["quickly_impatient"].map({'Never': 0, 'Sometimes': 1, 'Often': 2, 'Always': 3}).astype(int)
        student_stress["smoke_too_much"] = student_stress["smoke_too_much"].map({'Never': 0, 'Sometimes': 1, 'Often': 2, 'Always': 3}).astype(int)
        student_stress["hard_think_clearly"] = student_stress["hard_think_clearly"].map({'Never': 0, 'Sometimes': 1, 'Often': 2, 'Always': 3}).astype(int)
        student_stress["often_rushed_work"] = student_stress["often_rushed_work"].map({'Never': 0, 'Sometimes': 1, 'Often': 2, 'Always': 3}).astype(int)
        student_stress["not_sleeping_well"] = student_stress["not_sleeping_well"].map({'Never': 0, 'Sometimes': 1, 'Often': 2, 'Always': 3}).astype(int)
        student_stress["sensitive_noise"] = student_stress["sensitive_noise"].map({'Never': 0, 'Sometimes': 1, 'Often': 2, 'Always': 3}).astype(int)
        student_stress["find_criticism_difficult"] = student_stress["find_criticism_difficult"].map({'Never': 0, 'Sometimes': 1, 'Often': 2, 'Always': 3}).astype(int)
        student_stress["panic_attacks"] = student_stress["panic_attacks"].map({'Never': 0, 'Sometimes': 1, 'Often': 2, 'Always': 3}).astype(int)
        student_stress["stomachaches"] = student_stress["stomachaches"].map({'Never': 0, 'Sometimes': 1, 'Often': 2, 'Always': 3}).astype(int)

        student_stress["moved_house"] = student_stress["moved_house"].map({'No': 0, 'Yes': 1}).astype(int)
        student_stress["changes_lifestyle"] = student_stress["changes_lifestyle"].map({'No': 0, 'Yes': 1}).astype(int)
        student_stress["financial_problems"] = student_stress["financial_problems"].map({'No': 0, 'Yes': 1}).astype(int)
        student_stress["sexual_problems"] = student_stress["sexual_problems"].map({'No': 0, 'Yes': 1}).astype(int)
        student_stress["fellow_people_sick"] = student_stress["fellow_people_sick"].map({'No': 0, 'Yes': 1}).astype(int)
        student_stress["experienced_injury"] = student_stress["experienced_injury"].map({'No': 0, 'Yes': 1}).astype(int)
        student_stress["separated_family"] = student_stress["separated_family"].map({'No': 0, 'Yes': 1}).astype(int)
        student_stress["experienced_death"] = student_stress["experienced_death"].map({'No': 0, 'Yes': 1}).astype(int)
        student_stress["stress_level"] = student_stress["stress_level"].map({'Low stress': 0, 'Moderate stress': 1, 'High stress': 2}).astype(int)

        return student_stress

    def drop_columns(self):
        student_stress = self.convert_to_numeric()
        student_stress = student_stress.drop(columns=["time_studying", "career_pursue", "diet", "unable_control_academic_affairs", "confident_handle_academic_problems", 
                                                      "control_irritations_academic_affairs", "hard_think_clearly", "sensitive_noise", "stomachaches", "sexual_problems",
                                                        "experienced_death", "time_physical_activities", "moved_house", "fellow_people_sick"])
        
        return student_stress

