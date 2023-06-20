import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ambiguous_chars = 'il1Lo0O'

def get_yes_or_no(prompt):
    while True:
        answer = input(prompt).lower()
        if answer == 'да':
            return True
        elif answer == 'нет':
            return False
        else:
            print('Пожалуйста, введите "да" или "нет".')

def get_int_input(prompt):
    while True:
        answer = input(prompt).strip()
        if not answer.isdigit():
            print('Ввод не соответствует формату. Вы должны ввести целое число больше "0".')
        else:
            answer = int(answer)
            if answer <= 0:
                print('Если вам нужно "0" паролей зачем тогда его создавать?)', 'Давайте еще раз определимся. Cколько вам '
                                                                                'нужно паролей?', sep='\n')
            else:
                return answer

def long_password(prompt):
    while True:
        answer = input(prompt).strip()
        if not answer.isdigit():
            print('Ввод не соответствует формату. Вы должны ввести целое число.')
        else:
            answer = int(answer)
            if answer < 8:
                print('Если вам нужен надежный пароль он должен состять из 8 и больше символов.')
            else:
                return answer
def password():
    print('Привет! Я помогу тебе сгенерировать пароль.',
          'Давай определимся из чего будет состаять пароль и сколько тебе их нужно.',
          'Совет!!!', 'Для того чтобы пароль был достаточно надежным он должен состоять из:',
          '- строчных и заглавных букв латинского алфавита',
          '- содержать в себе числа и символы', '- его длина должна привышать 8 символов', sep='\n')
    print()

    num_passwords = get_int_input("Введите количество паролей для генерации: ")
    password_length = long_password("Введите длину пароля: ")
    use_digits = get_yes_or_no("Включать цифры (0123456789)? (да/нет): ")
    use_uppercase_letters = get_yes_or_no("Включать прописные буквы (ABCDEFGHIJKLMNOPQRSTUVWXYZ)? (да/нет): ")
    use_lowercase_letters = get_yes_or_no("Включать строчные буквы (abcdefghijklmnopqrstuvwxyz)? (да/нет): ")
    use_punctuation = get_yes_or_no("Включать символы (!#$%&*+-=?@^_.)? (да/нет): ")
    exclude_ambiguous_chars = get_yes_or_no("Исключать неоднозначные символы (il1Lo0O)? (да/нет): ")

    # создание списка возможных символов
    chars = ''
    if use_digits:
        chars += digits
    if use_uppercase_letters:
        chars += uppercase_letters
    if use_lowercase_letters:
        chars += lowercase_letters
    if use_punctuation:
        chars += punctuation
    if exclude_ambiguous_chars:
        for c in ambiguous_chars:
            chars = chars.replace(c, '')

    # генерация паролей
    for i in range(num_passwords):
        password = ''.join(random.choice(chars) for _ in range(password_length))
        print(password)

password()