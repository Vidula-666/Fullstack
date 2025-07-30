def new_game():
    guesses=[]
    correct_guesses=0
    question_num=1

    for key in questions:
        print("-------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        quess=input("Enter (A,B,C,or D):") 
        guesses.append(guesses)
        correct_guesses+=check_answer(questions.get(key),guesses)
        question_num+=1

    display_score()
#--------------
def check_answer(answer,guess):
    if answer==guess:
        return 1
    else:
        print("wrong:")
        return 0
#-------------
def display_score(correct_guesses,guesses):
    print("---------------")
    print("RESULTS")
    print("--------------")
    print("Answers:",end="")
    for i in questions:
        print(questions.get(i),end="")
        print()
        print("Guesses:",end="")
        for i in guesses:
            print(i,end=" ")
            print()

        score=int((correct_guesses/len(questions))*100)
        print("Your score is:"+str(score)+"%")
#-------------------
def play_again():
    pass
#---------------
questions={
    "who created python?:":"A",
    "what year was python created?:":"B",
    "python is tributed to which comedy group?:":"C",
    "Is the earth round?:" :"A"
}
options=[["A.Guido","B.adc","C.dfg","D.fnkk"],["A.1965","B.1991","C.7894","D.7894"],
         ["A.sdff","B.fght","C.jhj","D.jugn"],
         ["A.fggh","B.jjgh","C.jjjn","D.mnckn"]]

new_game()

