class Question:
    #Method that is used to pass in the questions and answers from data.py
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer