questions = [
    "Сколько будет два плюс два умноженное на два?",
    "Бревно нужно распилить на 10 частей, сколько надо сделать распилов?",
    "На двух руках 10 пальцев. Сколько пальцев на 5 руках",
    "Укол делают каждые полчаса, сколько нужно минут для трёх уколов?",
    "Пять свечей горело, две потухли. Сколько свечей осталось?"
]

answers = [6, 9, 25, 60, 2]

while True:
    
    count_right_answers = 0
    
    for i in range(len(questions)):
        
        print(questions[i])
        
        user_answer = int(input())
        
        right_answer = answers[i]
        if user_answer == right_answer:
            count_right_answers += 1
            
    print("Количество правильных ответов ", count_right_answers)
    
    print("Нажмите ДА для перепрохождения теста")
    answer = input()
    
    if answer in "ДАДадАдаLFLflFlf":
        continue
    else:
        break