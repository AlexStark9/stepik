import unicodedata


def is_valid(n, abc):
    if not n.isdigit():
        return False
    else:
        n = int(n)
        if n < 1 or n > abc:
            return False
    return True


def restart():
    start_again = True
    while True:
        answer = input('Хотите зашифровать или дешифровать что-то еще? (да, нет): ')
        if answer.lower() == 'да':
            caesar()
        elif answer.lower() == 'нет':
            print('Спасибо за то что обратилсь ко мне! До свидания!')
            start_again = False
            break
        else:
            print('Введите "да" или "нет"')

    return start_again


def is_valid_str(text):
    while text == '' or text.isspace():
        text = input("Введите хоть какой-нибудь текст: ")
    text = unicodedata.normalize('NFKD', text).replace("Ё", "Е").replace("ё", "е")

    return text


def is_valid_language(text, language):
    while True:
        if language == 'русский':
            # Проверяем, что все символы текста принадлежат кириллице
            if all('А' <= char <= 'я' for char in text):
                return False
        elif language == 'английский':
            # Проверяем, что все символы текста являются буквами английского алфавита
            if all(char.isalpha() and char.isascii() for char in text):
                return False
        return False


def not_key(alphabet):
    rus_abc = 32
    eng_abc = 26
    print('Давайте попробуем разгадать этот текст! '
          'Я буду выводить текст до того моменет пока вы не напишите "да".')

    text = input("Введите текст для дешифрования: ")

    if not is_valid_language(text, alphabet):
        text = input('Вы ввели текст либо частично, либо полностью не на выбранном вами языке. '
                     'Введите текст заново: ')
    text = is_valid_str(text)
    alpha_ru = [chr(i) for i in range(1072, 1104)]
    alpha_en = [chr(i) for i in range(97, 123)]

    user_input = 'нет'
    while user_input != "да":
        if alphabet == 'русский':
            for i in range(1, rus_abc + 1):
                text_decrypt = ''
                for j in text:
                    if j.isalpha() and j.lower() in alpha_ru:
                        if j.islower():
                            text_decrypt += alpha_ru[(alpha_ru.index(j) - i) % 32]
                        elif j.isupper():
                            text_decrypt += alpha_ru[(alpha_ru.index(j.lower()) - i) % 32].upper()
                    else:
                        text_decrypt += j
                print(f'Дешифрованный текст (ключ {i}): {text_decrypt}')
                user_input = input('Данный текст похож на расшифровку введенных вами данных? Введите да или нет: ')
                while user_input != 'да' and user_input != 'нет':
                    user_input = input('Введите да или нет: ')
                if user_input == "нет":
                    continue
                else:
                    break
        elif alphabet == 'английский':
            for i in range(1, eng_abc + 1):
                text_decrypt = ''
                for j in text:
                    if j.isalpha() and j.lower() in alpha_en:
                        if j.islower():
                            text_decrypt += alpha_en[(alpha_en.index(j) - i) % 26]
                        elif j.isupper():
                            text_decrypt += alpha_en[(alpha_en.index(j.lower()) - i) % 26].upper()
                    else:
                        text_decrypt += j
                print(f'Дешифрованный текст (ключ {i}): {text_decrypt}')
                user_input = input('Данный текст похож на расшифровку введенных вами данных? Введите да или нет: ')
                while user_input != 'да' and user_input != 'нет':
                    user_input = input('Введите да или нет: ')
                if user_input == "нет":
                    continue
                else:
                    break


def encrypt(alphabet):
    rus_abc = 32
    eng_abc = 26
    text_encrypt = ''
    if alphabet == 'русский':
        key = input(f'Для того, чтобы зашифровать ваш текст, задайте ключ шифрования. '
                    f'Введите цифру от 1 до {rus_abc}: ')
        while not is_valid(key, rus_abc):
            key = input(f'Некорректный ввод данных! Введите цифру от 1 до {rus_abc}: ')
        key = int(key)

        text = input("Введите текст для шифрования: ")

        if not is_valid_language(text, alphabet):
            text = input('Вы ввели текст либо частично, либо полностью не на выбранном вами языке. '
                         'Введите текст заново: ')

        text = is_valid_str(text)
        alpha_ru = [chr(i) for i in range(1072, 1104)]

        for i in text:
            if i.isalpha() and i.lower() in alpha_ru:
                if i.islower():
                    text_encrypt += alpha_ru[(alpha_ru.index(i) + key) % 32]
                elif i.isupper():
                    text_encrypt += alpha_ru[(alpha_ru.index(i.lower()) + key) % 32].upper()
            else:
                text_encrypt += i

    elif alphabet == 'английский':
        key = input(f'Для того, чтобы зашифровать ваш текст, задайте ключ шифрования. '
                    f'Введите цифру от 1 до {eng_abc}: ')
        while not is_valid(key, eng_abc):
            key = input(f'Некорректный ввод данных! Введите цифру от 1 до {eng_abc}: ')
        key = int(key)

        text = input("Введите текст для шифрования: ")

        if not is_valid_language(text, alphabet):
            text = input('Вы ввели текст либо частично, либо полностью не на выбранном вами языке. '
                         'Введите текст заново: ')

        alpha_en = [chr(i) for i in range(97, 123)]

        for i in text:
            if i.isalpha() and i.lower() in alpha_en:
                if i.islower():
                    text_encrypt += alpha_en[(alpha_en.index(i) + key) % 26]
                elif i.isupper():
                    text_encrypt += alpha_en[(alpha_en.index(i.lower()) + key) % 26].upper()
            else:
                text_encrypt += i

    return print('Зашифрованный текст:', text_encrypt)  # Вывод зашифрованного текста


def decipher(alphabet):
    rus_abc = 32
    eng_abc = 26
    text_decrypt = ''

    if alphabet == 'русский':
        key_user = input('Для того, чтобы дешифровать текст нужно знять ключ шифрования. Вы знаете ключ? '
                         'Введите да или нет: ')
        while key_user != 'да' and key_user != 'нет':
            key_user = input('Некорректный ввод данных! Введите да или нет :')

        if key_user == 'да':
            key = input(f'Для того, чтобы дешифровать текст, введите ключ шифрования. '
                        f'Введите цифру от 1 до {eng_abc}: ')
            while not is_valid(key, rus_abc):
                key = input(f'Некорректный ввод данных! Введите цифру от 1 до {rus_abc}: ')
            key = int(key)

            text = input("Введите текст для дешифрования: ")

            if not is_valid_language(text, alphabet):
                text = input('Вы ввели текст либо частично, либо полностью не на выбранном вами языке. '
                             'Введите текст заново: ')

            text = is_valid_str(text)
            alpha_ru = [chr(i) for i in range(1072, 1104)]

            for i in text:
                if i.isalpha() and i.lower() in alpha_ru:
                    if i.islower():
                        text_decrypt += alpha_ru[(alpha_ru.index(i) - key) % 32]
                    elif i.isupper():
                        text_decrypt += alpha_ru[(alpha_ru.index(i.lower()) - key) % 32].upper()
                else:
                    text_decrypt += i

            print('Дешифрованный текст:', text_decrypt)

        elif key_user == 'нет':
            not_key(alphabet)

    elif alphabet == 'английский':
        key_user = input('Для того, чтобы дешифровать текст нужно знять ключ шифрования. Вы знаете ключ? '
                         'Введите да или нет: ')
        while key_user != 'да' and key_user != 'нет':
            key_user = input('Некорректный ввод данных! Введите да или нет :')

        if key_user == 'да':
            key = input(f'Для того, чтобы дешифровать текст, введите ключ шифрования. '
                        f'Введите цифру от 1 до {eng_abc}: ')
            while not is_valid(key, eng_abc):
                key = input(f'Некорректный ввод данных! Введите цифру от 1 до {eng_abc}: ')
            key = int(key)

            text = input("Введите текст для дешифрования: ")

            if not is_valid_language(text, alphabet):
                text = input('Вы ввели текст либо частично, либо полностью не на выбранном вами языке. '
                             'Введите текст заново: ')

            alpha_en = [chr(i) for i in range(97, 123)]

            for i in text:
                if i.isalpha() and i.lower() in alpha_en:
                    if i.islower():
                        text_decrypt += alpha_en[(alpha_en.index(i) - key) % 26]
                    elif i.isupper():
                        text_decrypt += alpha_en[(alpha_en.index(i.lower()) - key) % 26].upper()
                else:
                    text_decrypt += i

            print('Дешифрованный текст:', text_decrypt)

        elif key_user == 'нет':
            not_key(alphabet)


def caesar():
    start_again = True

    while start_again:
        what_do = input('Что нужно сделать: зашифровать ваш текст или дешифровать? '
                        'Введите зашифровать или дешифровать: ').lower()
        while what_do != 'зашифровать' and what_do != 'дешифровать':
            what_do = input('Некорректный ввод данных! Введите encrypt или decipher: ').lower()

        alphabet = input('На каком языке будет текст, английский или русский? Введите английский или русский: ').lower()

        while alphabet != 'английский' and alphabet != 'русский':
            alphabet = input('Некорректный ввод данных! Выберите язык из предложенных: '
                             'английский или русский: ').lower()

        if what_do == 'зашифровать':
            encrypt(alphabet)
        else:
            decipher(alphabet)

        start_again = restart()


print('Привет! Я программа, созданная для шифрования и дешифрования "Шифра Цезаря"')
caesar()
