# Implementing quiz project
from Question_Data import question_data
from Questions import Questions
from quiz_brain import QuizBrain
question_bank=[]
for i in question_data:
    question_bank.append(Questions(i["text"],i["answer"]))
quiz_ob=QuizBrain(question_bank)
quiz_ob.next_question()
