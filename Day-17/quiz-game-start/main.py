from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question["question"]
    ans = question["correct_answer"]
    QuestionObject = Question(text, ans)
    question_bank.append(QuestionObject)

quizBrainObject = QuizBrain(question_bank)

question_left = True
while question_left:
    quizBrainObject.next_question()
    question_left = quizBrainObject.still_has_questions()
print("you have completed the quiz!")
print(f"your final score was: {quizBrainObject.score}/{quizBrainObject.question_number + 1}")