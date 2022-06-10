from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#Create an empty list that will hold the list of questions from data.py
question_bank = []

#For loop that loops through the questions in data.py, save the questions & answers to the Question class, and
#add each question to the question_bank as a list
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

#Created a variable and set it to the Quizbrain class passing in the question list (question_bank)
quiz = QuizBrain(question_bank)

#Checks if quiz still has questions remaining
while quiz.still_has_questions():
    #Call the next_question method 
    quiz.next_question()

print("You've complete the quiz")
print(f"Your final score was: {quiz.user_score}/{quiz.question_number}")

