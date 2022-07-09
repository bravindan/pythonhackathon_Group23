import random
careers =['Developer', 'Data Scientist', 'SW Engineer']
career_advice = ['You should be a developer', 'You should be a data scientist', 'You should be an engineer']
QUESTIONS = [
    ("What is your dream job", "developer"),
    ("Which career do you think pays well", "sw engineer"),
    ("What is your passion?", "coding"),
]

for question, correct_answer in QUESTIONS:
    answer = input(f"{question}? ")
    if answer == correct_answer:
        print("Answered!")
        
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
career = random.choice(careers)
print(f"You should be a {career}")