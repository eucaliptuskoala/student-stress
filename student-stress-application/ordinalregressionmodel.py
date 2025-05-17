import pandas as pd
from ipreprocessing import IPreprocessing
from inferencetransform import InferenceTransform
from statsmodels.miscmodels.ordinal_model import OrderedModel

class OrdinalRegressionModel:

    def __init__(self, preprocessor: IPreprocessing, inference: InferenceTransform):
        self.student_stress = preprocessor.drop_columns()
        self.new_data = inference.transform()

    def preprocess_data(self):
        student_stress = self.student_stress
        ordinal_df = student_stress.copy()

        ordinal_df["level"] = pd.Categorical(ordinal_df["stress_level"].map({0: 'Low stress', 1: 'Moderate stress', 2: 'High stress'}), categories=['Low stress', 'Moderate stress', 'High stress'], ordered=True)

        X_ordinal = ordinal_df[['time_sleep', 'upset_academic_affairs', 'nervous_academic_pressure', 'unable_cope_academic_activities', 'things_going_on_way', 'academic_performance_top', 'angered_bad_performance', 'academic_difficulties_piling_up', 'never_satisfied_achievements', 'quickly_irritated_people', 'future_gloomy', 'quickly_impatient', 'smoke_too_much', 'often_rushed_work', 'not_sleeping_well', 'find_criticism_difficult', 'panic_attacks', 'changes_lifestyle']]
        y_ordinal = ordinal_df['level']
        return X_ordinal, y_ordinal
    
    def train_model(self):
        X_ordinal, y_ordinal = self.preprocess_data()
        mod_prob = OrderedModel(y_ordinal, X_ordinal, distr='logit')

        res_prob = mod_prob.fit(method='bfgs')
        return res_prob

    def predict(self, new_data):
        model = self.train_model()
        X_ordinal, y_ordinal = self.preprocess_data()
        X_inference = pd.DataFrame([new_data], columns=X_ordinal.columns)

        probabilities = model.model.predict(model.params, exog=X_inference)

        stress_levels = y_ordinal.cat.categories
        probs_df = pd.DataFrame(probabilities, columns=stress_levels)

        predicted_label = probs_df.iloc[0].idxmax()
        predicted_prob = probs_df.iloc[0].max()
        return predicted_label, predicted_prob, probs_df.T  