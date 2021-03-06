# Приветствие
# Вывести "Введите длину пароля"
# Получаем длину пароля
# Спрашиваем какие символы включаем в пароль
# Формируем строку, состоящую из возможных символов на основе ответов пользователя
# Сгенерировать рандомный пароль нужной длины из выбранных символов
import random

def ask_question(question):
    print(question, "Нажмите Да или Нет")
    answer = input()
    if answer == "Да":
        return True
    else:
        return False
    
def generate_password(lenght, chars):
    password = ""
    for i in range(length):
        random_index = random.randint(0, len(chars)-1)
        password += chars[random_index]
    
    return password


print("Привет, Я генератор паролей. \nЯ задам пару уточняющих вопросов, на основе которых сгенерирую пароль. \nДавай начнем!")

while True:
    print("Введите количство паролей")
    numb_pass = int(input())
    print("Введите длину пароля: ")
    length = int(input())
    
    digits_enabled = ask_question("Включать ли цифры?")
    
    latin_lowercase_enabled = ask_question("Включать ли строчные латинские буквы?")
    
    latin_uppercase_enabled = ask_question("Включать ли заглавные латинские буквы?")
    
    russian_lowercase_enabled = ask_question("Включать ли строчные русские буквы?")
    
    russian_uppercase_enabled = ask_question("Включать ли заглавные русские буквы?")
    
    punctuations_enabled = ask_question("Включать ли знаки пунктуации?")
    
    enabled_chars = ""
    digits = "0123456789"
    latin_lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    latin_uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    russian_lowercase_letters = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    russian_uppercase_letters = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    punctuations = "!#$%&*+-=?@^_"
    
    if digits_enabled:
        enabled_chars += digits
        
    if latin_lowercase_enabled:
        enabled_chars += latin_lowercase_letters
        
    if latin_uppercase_enabled:
        enabled_chars += latin_uppercase_letters
        
    if russian_lowercase_enabled:
        enabled_chars += russian_lowercase_letters
        
    if russian_uppercase_enabled:
        enabled_chars += russian_uppercase_letters
        
    if punctuations_enabled:
        enabled_chars += punctuations
        
    
    for i in range(numb_pass):
        password = generate_password(length, enabled_chars)
        print(password)
    
    print("Сгенерировать ещё пароль?")
    answer = input()
    
    if answer in "LflfДада":
        continue
    else:
        print("Спасибо, что воспользовались нашей услугой! \nВсего хорошего.")
        break