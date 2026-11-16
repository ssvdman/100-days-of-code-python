class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        t_len = len(self.question_list)
        if self.question_number < t_len - 1:
            self.question_number += 1
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_ans = input(f"Q{self.question_number + 1}: {current_question.text} (True/False): ")
        self.check_answer(user_ans, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got it right!")
            self.score += 1
        else:
            print("that's wrong.")
            print(f"the correct answer was: {correct_answer}")
        print(f"your current score is {self.score}/{self.question_number + 1}")
        print()