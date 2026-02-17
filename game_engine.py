import pandas as pd
import random

class GameSession:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.current = 0

        # Load messy Kaggle CSV
        data = pd.read_csv(
            "dataset/phishing_dataset.csv",
            encoding='latin1',
            quotechar='"',
            engine='python',
            on_bad_lines='skip'
        )

        # Clean columns
        data.columns = data.columns.str.strip()

        # Keep only domain and label
        data = data[['domain','label']]
        data = data.rename(columns={'domain':'url'})

        # Pick 10 random questions
        self.questions = data.sample(10).to_dict(orient="records")

    def get_current_question(self):
        return self.questions[self.current]["url"]

    def check_answer(self, user_answer):
        correct = self.questions[self.current]["label"]
        if int(user_answer) == int(correct):
            self.score += 1
            result = True
        else:
            result = False
        self.current += 1
        return result

    def finished(self):
        return self.current >= 10

    def accuracy(self):
        return round((self.score/10)*100,2)
