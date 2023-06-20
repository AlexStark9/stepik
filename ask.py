import random
from math import log2, ceil

# Пользователь выбирает правую границу
def right_border():
    flag = True
    while flag:
        user_input = input()
        if not user_input.isdigit():
            print('Ввод не соответствует формату. Вы должны ввести целое число. Попробуйте еще раз.')
            continue
        x = int(user_input)
        if x <= 1:
            print(f'Вы ввели {x}. Введите целое число больше 1: ')
            continue
        flag = False
        break
    return x

# Определяем количество попыток на основании выбранной правой границы
def attempt(n):
    max_attempts = ceil(log2(n))
    return max_attempts

# Проверка корректности ввода данных пользователем
def is_valid(n, right):
    if not n.isdigit():
        return False
    else:
        n = int(n)
        if n < 1 or n > right:
            return False
    return True

# Функция для перезапуска игры
def restart_game():
    while True:
        answer = input('Хотите начать новую игру? (да, нет): ')
        if answer.lower() == 'да':
            game()
        elif answer.lower() == 'нет':
            print('Спасибо за игру! До свидания!')
            break
        else:
            print('Введите "да" или "нет"')

# Сама игра. В соответствии с выбранной правой границей выставляется количество попыток
# для того чтобы угадать закаданное число
# Если пользователь не угадывает число то игра заканчивается
def game():
    print('Привет!', 'Это игра числовая угадайка.', 'Я загадываю число от 1 до n и вы патаетесь его отгадать.',
          'Давайте зададим правую границу. Введите целое число, больше 1: ', sep='\n')

    right = right_border() # определяем правую границу
    max_attempt = attempt(right) # количество попыток
    num = random.randint(1, right) # генерим число
    print(f'Отлично! Хорошее число. Я загадал число от 1 до {right} попробуйте его отгадать.')
    print(f'У вас есть {max_attempt} попыток.')
    counter = 0
    play_again = True # флаг для цикла
    # Запускаем цикл до того момента пока флаг == True, и цикл пока счетчик не превышает max_attempt
    while play_again:
        while counter < max_attempt:
            # считываем ввод пользователя и проверяем его правильность
            user_input = input()
            if not is_valid(user_input, right):
                print(f'Ввод не соответствует формату. Вы должны ввести целое число в диапазоне от 1 до {right}')
                continue
            user_input = int(user_input)
            # даем подсказки пользователю
            if user_input > num:
                print('Слишком много, попробуй еще раз')
            elif user_input < num:
                print('Слишком мало, попробуй еще раз')
            else:
                print(f'Вы угадали, поздравляю! Вы угадали с {counter + 1}-й попытки.')
                # вызываем функцию restart_game() и если да то запускаем игру заново если нет то останавливаем игру
                play_again = restart_game()
                counter = 0
                if play_again:
                    right = right_border()
                    max_attempt = attempt(right)
                    num = random.randint(1, right)
                    print(f'Отлично! Хорошее число. Я загадал число от 1 до {right}, попробуйте его отгадать.')
                    print(f'У вас есть {max_attempt} попыток.')
                    break
                else:
                    break
            counter += 1 # добавляем к счетчику +1 каждый раз когда пользоваетль не угадал загаданное число
        # вызываем функцию restart_game() когда кончились попытки
        # и если да то запускаем игру заново если нет то останавливаем игру
        else:
            print(f'Тупой человечек возомнил себя умнее компьютера. Загаданное число было: {num}.')
            play_again = restart_game()
            counter = 0
            if play_again:
                right = right_border()
                max_attempt = attempt(right)
                num = random.randint(1, right)
                print(f'Отлично! Хорошее число. Я загадал число от 1 до {right}, попробуйте его отгадать.')
                print(f'У вас есть {max_attempt} попыток.')
            else:
                break

game()
