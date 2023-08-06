# A dictionary that stores questions and answers
# Have a variable that tracks the score of the player
# loop through that dictionary using the key value pairs
# Display each question to the user and allow them to answer
# Tell them if they are right or wrong
# Show the final result when quiz is completed

quiz = {
    "question1": {
        "question":"what is the capital of France?",
        "answer": "Paris" 

    },
    "question2" : {
        "question" : "what is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3" : {
        "question" : "what is the capital of Italy?",
        "answer": "Rome"
    },
    "question4" : {
        "question" : "what is the capital of Bangladesh?",
        "answer": "Dhaka"
   },
    "question5" : {
        "question" : "what is the capital of India?",
        "answer": "Delhi"

    },
    "question6" : {
        "question" : "what is the capital of USA?",
        "answer": "Washington"
   },
    "question7" : {
        "question" : "what is the capital of England?",
        "answer": "London"

    },
}

score = 0

for key,value in quiz.items():
    print(value["question"])
    answer = input("Answer: ")

    if answer.lower() == value["answer"].lower():
        print("correct")
        score += 1

    else:
        print("Wrong answer!")
        print("The answer is : " + value["answer"])

print("You scored: " + str(score) + " out of 7")