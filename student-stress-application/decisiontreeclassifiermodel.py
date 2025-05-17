import pandas as pd
from ipreprocessing import IPreprocessing
from inferencetransform import InferenceTransform
from imblearn.over_sampling import RandomOverSampler
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import _tree

class DecisionTreeClassifierModel:

    def __init__(self, preprocessor: IPreprocessing, inference: InferenceTransform):
        self.student_stress = preprocessor.drop_columns()
        self.new_data = inference.transform()

    def preprocess_data(self):
        student_stress = self.student_stress
        ros = RandomOverSampler(sampling_strategy='not majority')

        X_resampled, y_resampled = ros.fit_resample(student_stress.drop(columns=['stress_level']), student_stress['stress_level'])

        balanced_df = pd.DataFrame(X_resampled, columns=student_stress.columns[:-1])
        balanced_df['stress_level'] = y_resampled

        X_balanced = balanced_df[['part_time_job', 'time_sleep', 'upset_academic_affairs', 'nervous_academic_pressure', 'unable_cope_academic_activities', 'things_going_on_way', 'academic_performance_top', 'angered_bad_performance', 'academic_difficulties_piling_up', 'never_satisfied_achievements', 'quickly_irritated_people', 'future_gloomy', 'quickly_impatient', 'smoke_too_much', 'often_rushed_work', 'not_sleeping_well', 'find_criticism_difficult', 'panic_attacks', 'changes_lifestyle', 'financial_problems', 'experienced_injury', 'separated_family']]
        y_balanced = y_resampled

        X_balanced_train, X_balanced_test, y_balanced_train, y_balanced_test = train_test_split(X_balanced, y_balanced, test_size=.2, stratify=y_balanced)
        return X_balanced_train, X_balanced_test, y_balanced_train, y_balanced_test
    
    def train_model(self):
        X_balanced_train, X_balanced_test, y_balanced_train, y_balanced_test = self.preprocess_data()
        dtc = DecisionTreeClassifier(max_depth=None, min_samples_split=4)
        dtc.fit(X_balanced_train, y_balanced_train)
        score = dtc.score(X_balanced_test, y_balanced_test)
        return dtc, score, X_balanced_train, y_balanced_train

    def predict(self, new_data):    
        model, score, X_train, y_train = self.train_model()

        X_inference = pd.DataFrame([new_data], columns=X_train.columns)

        proba = model.predict_proba(X_inference)[0]
        classes = model.classes_  

        stress_level_map = {
            0: "Low stress",
            1: "Moderate Stress",
            2: "High stress"
        }

        # Map classes numeric labels to names
        class_names = [stress_level_map[c] for c in classes]

        sorted_indices = sorted(range(len(classes)), key=lambda i: classes[i])
        sorted_class_names = [class_names[i] for i in sorted_indices]
        sorted_proba = [proba[i] for i in sorted_indices]

        result_df = pd.DataFrame({
            "Outcome": sorted_class_names,
            "Probability": sorted_proba
        })

        feedback_map = {
            "part_time_job": "Managing a part-time job while studying can lead to stress. Try to ensure your workload remains manageable and doesn't affect your health or academics.",
            "time_sleep": "Getting enough quality sleep helps improve memory, focus, and emotional regulation. Aim for 7–9 hours of consistent rest.",
            "upset_academic_affairs": "Feeling upset about academic issues is normal. Reflect on the root causes and consider talking to a tutor or advisor.",
            "nervous_academic_pressure": "Academic pressure can trigger anxiety. Try breaking down tasks, practicing mindfulness, or speaking to a counselor if it feels overwhelming.",
            "unable_cope_academic_activities": "If you're finding it difficult to keep up, consider reassessing your commitments or speaking with your academic advisor for support.",
            "things_going_on_way": "When things are progressing well, take a moment to acknowledge your effort—it can boost confidence and motivation.",
            "academic_performance_top": "Maintaining top performance is impressive, but be careful not to burn out. Take breaks and celebrate small wins.",
            "angered_bad_performance": "It’s okay to feel frustrated. Use setbacks as learning opportunities and consider seeking academic support if needed.",
            "academic_difficulties_piling_up": "When challenges build up, it helps to prioritize and tackle tasks one step at a time. Don’t hesitate to ask for help.",
            "never_satisfied_achievements": "Striving for more is good, but it's also important to recognize your progress and give yourself credit.",
            "quickly_irritated_people": "If you're feeling irritable often, it may be a sign of stress or fatigue. Consider self-care strategies or relaxation exercises.",
            "future_gloomy": "Uncertainty about the future is common. Setting small, achievable goals can help you regain a sense of direction and control.",
            "quickly_impatient": "If you’re easily impatient, try breathing exercises or short breaks to stay centered when things feel frustrating.",
            "smoke_too_much": "Increased smoking may be a stress response. Exploring healthier outlets like exercise or hobbies might help reduce dependency.",
            "often_rushed_work": "Consistently rushing through work may affect quality. Try time-blocking your schedule to stay organized and reduce last-minute pressure.",
            "not_sleeping_well": "Poor sleep quality impacts concentration and mood. Establish a calming bedtime routine and limit screen use before bed.",
            "find_criticism_difficult": "Criticism can be tough, but it’s often a chance to grow. Try to see feedback as constructive, not personal.",
            "panic_attacks": "Experiencing panic attacks can be serious. Consider speaking with a counselor or healthcare professional for support.",
            "changes_lifestyle": "Lifestyle changes (diet, activity, routine) can significantly affect stress levels. Try to keep healthy habits consistent.",
            "financial_problems": "Financial worries are stressful. Look into student budgeting tools or speak with financial aid offices for guidance.",
            "experienced_injury": "Injuries can affect mental and physical well-being. Prioritize recovery and don’t hesitate to ask for academic accommodations.",
            "separated_family": "Being away from family can be emotionally hard. Regular communication or joining support communities can help ease feelings of isolation."
        }

        tree = model.tree_
        features = X_inference.columns

        node_path = model.decision_path(X_inference).indices

        used_feats = {
            features[tree.feature[n]]
            for n in node_path
            if tree.feature[n] != _tree.TREE_UNDEFINED
        }

        feedback_msgs = [feedback_map[f] for f in used_feats if f in feedback_map]

        predicted_index = proba.argmax()
        predicted_label = classes[predicted_index]
        predicted_prob = proba[predicted_index]

        return predicted_label, predicted_prob, result_df, feedback_msgs, score