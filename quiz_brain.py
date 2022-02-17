class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        len_list = len(self.question_list)
        return self.question_number < len_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.scoreUser(user_input, current_question.answer)

    def scoreUser(self, ui, cA):
        if ui.lower() == cA.lower():
            print("you got that right")
            self.score += 1
            print(f"your score is {self.score}/{self.question_number}")
        else:
            print("you got that wrong")
            print(f"your score is {self.score}/{self.question_number}")
        print(f"The correct answer {cA}")
        print("\n")
