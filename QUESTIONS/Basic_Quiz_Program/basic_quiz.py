import json
FILEPATH = "QUESTIONS/Basic_Quiz_Program/question_for_quiz.json"

def user_input_checker():
    track = False
    while(track != True):    
            try:
                user_choice = int(input("Choose your Answer: "))
            except ValueError:
                print("Error, Please enter option in the form of integer\n")
                track = False
            if user_choice > 0 and user_choice < 5:
                 return user_choice
            else:
                print("Error, Please enter option in the form of integer between 1 to 4\n")
                track = False

score = 0
with open(FILEPATH, 'r', encoding='utf-8') as file:
    question_file = json.load(file)
    for i, questions in enumerate(question_file, 1):  # Type of questions is dict
        print(f"\nQuestion {i} -> {questions['question']}") # Type of each question key is string
        for i, options in enumerate(questions['options'], 1):
            print(f"Option {i} -> {options}")
        questions['user_choice'] = user_input_checker()
        print(f"-> Your Answer: {questions['user_choice']}, Correct Answer: {questions['answer']}")
        if questions['user_choice'] == questions['answer']:
            print("Your answer is correct.\n") 
            score += 1
        else:
             print("Your answer was incorrect.\n")

print(f"{score} out of {len(question_file)} questions are correct.")
        