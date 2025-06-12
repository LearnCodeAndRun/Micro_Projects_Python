class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.question_list=question_list
    def check_answer(self,answer,question,score):
        if answer==question.answer:
                score+=1
                print(f"You got it right!")
        else:
             print("You got it wrong!")
        print(f"The correct answer was: {question.answer}")
        return score
    def next_question(self):
        score=0
        for question in self.question_list:
            answer=""
            while answer!="True" and answer!="False":   
              answer=input(f"Q{self.question_number+1} {question.text} (True/False): ").title()
              if answer!="True" and answer!="False":
                  print("Please enter either \"True\" or \"False\" only. No other answer in any other format will be accepted.")
            self.question_number+=1
            score=self.check_answer(answer,question,score)
            print(f"Current score: {score}/{self.question_number}")

