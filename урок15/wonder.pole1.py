# Заводим слово, котоое нужно угадать
# Заводим слово пользователя
# Пока слово пользователя не равно загаданному:
       # Вывести букву
       # Проверка что это одна бука
       # Обновление слова пользователя!
       # Если после обновления слово не поменялось, то выводим пользователю, что такой буквы нет
       # Иначе выводим, что есть такая буква
       # Новое слово пользователя становится словом пользователя
       # Печетаем слово пользователя
       
# Поздравления

def update_user_word(secret_word, user_word, char):
    new_user_word = ""
    for i in range(len(secret_word)):
        if secret_word[i] == char:
            new_user_word += char
        else:
            new_user_word += user_word[i]
    return new_user_word


while True:
    
    secret_word = "академия"
    user_word = "********"
    print(user_word)

    
    while user_word != secret_word:
        print("Введите букву")
        user_char = input()
        if len(user_char) != 1:
            continue
        
        new_user_word = update_user_word(secret_word, user_word, user_char)
        
        if user_word == new_user_word:
            print("К сожалению, такой буквы нет в слове")
        else:
            print("Поздравляме, такая буква есть в слове")
            
        user_word = new_user_word
        
        print(user_word)
        
    print("Ура, вы угадали загаданное слово")
    
    print("Ещё раз сыграть?")
    answer = input()
    
    if answer in "LFLflFlfДАДадАда":
        continue
    else:
        break