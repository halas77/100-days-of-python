class QuizBrain:
    
    def __init__(self, questionlist):
        self.question_number = 0
        self.questionlist = questionlist
        
    def next_question(self):
        current_question = self.questionlist[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        