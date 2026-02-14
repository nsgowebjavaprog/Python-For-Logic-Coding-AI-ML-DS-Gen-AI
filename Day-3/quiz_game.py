# Quiz

questions = ("Queestion-A",
             "Queestion-B",
             "Queestion-C",
             "Queestion-D",
             "Queestion-E")

options = (("A. 1","B. 2","C. 3","D. 4"),
           ("A. 10","B. 20","C. 30","D. 40"), 
           ("A. 100","B. 200","C. 300","D. 400"), 
           ("A. 1000","B. 2000","C. 3000","D. 4000"), 
           ("A. 10000","B. 20000","C. 30000","D. 40000"))

answers = ("A", "B", "C", "D", "A")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("__________________________________")
    print(question)
    
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (A, B, C, D): ").upper()    
    guesses.append(guess)
    
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
        print(f"{answers[question_num]} is the correct answer.")    
    
    question_num += 1    
print("__________________________________")
print("RESULTS")


print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()  


print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print() 


print(f"Your score is: {score}/{len(questions)}")