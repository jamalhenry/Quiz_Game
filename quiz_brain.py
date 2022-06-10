class QuizBrain:
    #Method that takes in a parameter for the list of questions
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.user_score = 0

    #Method that returns True if their are questions remaining and false otherwise
    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    #Method gets hold of the current question and tap into list to get the current question number
    def next_question(self):
        current_question = self.question_list[self.question_number]
        #Increase the question number every time this method is called
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        #call the check answer method and pass the users answer in
        self.check_answer(user_answer, current_question.answer)

    #Method that checks if the answer the user entered is correct
    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.user_score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_ans}")
        print(f"Your current score is: {self.user_score}/{self.question_number}")
        print("\n")







