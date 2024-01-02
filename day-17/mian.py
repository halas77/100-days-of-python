from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    my_question = Question(text, answer)
    question_bank.append(my_question)
    
quiz = QuizBrain(question_bank)


while quiz.stiil_has_question():
    quiz.next_question()
    
print("You have completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

     


