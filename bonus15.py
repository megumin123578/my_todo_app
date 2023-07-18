import json

with open('question.json','r') as file:
    content =file.read()

data = json.loads(content)
score = 0
for question in data:
    print(question['question_text'])
    for index, alternative in enumerate(question['alternatives']):
        print(index + 1,'-',alternative)    
    user_choice = int(input('enter your answer: '))
    question["user_choice"] = user_choice  
    if question["user_choice"] == question["correct_answer"]:
        score = score +1

for index, question in enumerate(data):
    message = f"{index + 1} - Your answer: {question['user_choice']}, " \
    f"correct answer: {question['correct_answer']}"
    print(message)

print(score,'/',len(data))


