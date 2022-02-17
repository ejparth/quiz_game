from data import question_data
from question_model import Questions
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    ques_text = question["question"]
    ques_ans = question["correct_answer"]
    # even creating an object simply will need an argument if the class has arguments
    new_create = Questions(ques_text, ques_ans)
    question_bank.append(new_create)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()


