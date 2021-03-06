# Создать поле
# Запомнить символ хода
# Пока не конец игры
     # Показать поле
     # Сказать пользователю, чтобы ходил
     # Получить от игрока ход
     # Сделать ход
     # Поменять символ хода на другой
# Поздравить победителя

def create_field():
     field = []
     for i in range(3):
          field.append(["*"] * 3)
     return field

def print_field(field):
     for i in range(3):
          for j in range(3):
               print(field[i][j], end="")
          print()

def win(field):
     for i in range(3):
          if field [i][0] != "*" and field[i][0] == field[i][1] == field[i][2]:
               return True
          
     for i in range(3):
          if field [0][i] != "*" and field[0][i] == field[1][i] == field[2][i]:
               return True

     if field [0][0] != "*" and field[0][0] == field[1][1] == field[2][2]:
          return True
     
     if field [0][2] != "*" and field[0][2] == field[1][1] == field[2][0]:
          return True
     return False


def end_game(field):
     if win(field):
          return True
     
     for i in range(3):
          for j in range(3):
               if field[i][j] == "*":
                    return False
     return True

while True:
     
     field = create_field()
     
     current_symbol = "X"
     
     while not end_game(field):
          print_field(field)
          print("Введите номер строки и номер столбца")
          row = int(input())
          column = int(input())
          field[row - 1][column -1] = current_symbol
          
          if current_symbol == "X":
               current_symbol = "0"
          else:
               current_symbol = "X"
     
     print_field(field)
     if current_symbol == "X":
          print("Ура! Победил 0")
     else:
          print("Ура! Победил Х")
          
     print("Жми Да, если хочешь сыграть ещё раз")
     answer = input()
     
     if answer in "LFLflFlfДАдаДадА":
          continue
     else:
          print("Ждём Вашего возвращения")
          break