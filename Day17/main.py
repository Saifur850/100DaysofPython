from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
    question_text= question['text']
    question_answer= question['answer']
    question_object= Question(question_text, question_answer)
    question_bank.append(question_object)
    # print(question_text)
# print(question_bank[0].text)

quiz= QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

quiz.final_statement()





