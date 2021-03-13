import random
import os

# Кортежи хранят заглавные и строчные гласные.
# В первую очередь служат для нахождения ответов в словах из файла "words.txt"
lower_vowels = ("а", "у", "о", "и", "э", "ы", "я", "ю", "е", "ё")
upper_vowels = ("А", "У", "О", "И", "Э", "Ы", "Я", "Ю", "Е", "Ё")


def define_random_word(completed_words):
    """Определяет и возвращает случайное слово для вопроса, если это слово ещё не использовалось."""

    f = open("words.txt", "r")

    # Узнаём количество строк в words.txt
    amount_of_lines = len(f.readlines())
    while True:
        # Генерируем число, которое равносильно номеру строки в файле words.txt
        a_number = random.randint(1, amount_of_lines)
        if a_number not in completed_words:
            break

    f.close()

    return a_number


def define_answer(number):
    """Ищет в answer.txt ответ на вопрос и возвращает его."""

    t = open("answers")
    x = 1
    # Пока не дошли до ответа для загаданного слова...
    while x <= number:
        # Читаем строки и увеличиваем счётчик
        the_answer = t.readline()
        x += 1

    # Отрезаем перевод строки
    the_answer = the_answer.rstrip("\n")

    # Переменная отвечает за то, множественный ли ответ для слова или нет
    multiple_answer = False
    # Определяем, множественный ли ответ, по наличию "/" в нём
    for y in the_answer:
        if y == "/":
            multiple_answer = True
            break

    # Если ответ множественный...
    if multiple_answer:
        # Ищем все числа-ответы, перебирая строку с ответом исключая "/"
        the_multiple_answer = []
        for y in the_answer:
            if y != "/":
                # Записываем возможные ответы в переменную-список в типе int
                the_multiple_answer.append(int(y))
        t.close()
        # Возвращаем список
        return the_multiple_answer

    t.close()
    # Если ответ единственный, просто возвращаем число
    return the_answer


def define_word(line):
    """Ищет слово в words.txt, которое нужно загадать, на основе переданного числа (line)."""

    f = open("words.txt")

    x = 1
    while x <= line:
        the_word = f.readline()
        x += 1

    f.close()
    return the_word


def define_order_of_vowels(target):
    """Составляет строку, являющуюся визуальной подсказкой для определения номера гласной в слове. """

    # Переменная с целевой строкой, которую потом вернём
    the_label = ""
    # Переменная, служащая для добавления и указания номера гласной
    a_vowel_order = 0

    # Отрезаем перевод строки и делаем буквы строчными
    target = target.rstrip("\n")
    target = target.lower()

    # Посредством цикла обрабатываем целевое слово
    for x in target:
        # Делаем так, чтобы не определялись гласные для примера к слову, который
        # заключён в скобки
        if x == "(":
            break
        # Если буква в слове - гласная...
        if x in lower_vowels:
            # Добавляем порядковый номер гласной в строку
            a_vowel_order += 1
            the_label += str(a_vowel_order)
        else:
            # В ином случае добавляем пробел в строку
            the_label += " "

    # Возвращаем выводимую строку и максимальное количество гласных
    return the_label, a_vowel_order


def correct(word):
    """Сообщает пользователю, что он ответил на вопрос правильно."""

    os.system("cls")
    print("\n\n\t --- ВЕРНО! ---")
    print("\n\n\t" + word)

    os.system("pause")
    os.system("cls")


def incorrect(word, answer):
    """Сообщает пользователю, что он ответил на вопрос неправильно; показывает как правильно."""

    # Целевое слово преобразуем в нижний регистр
    l_word = word.lower()
    # Счётчик гласных в слове
    count_of_vowels = 0
    # Строковая переменная для составления и вывода (оформленного)
    # пользовательского ответа на вопрос
    user_word = ""

    # По буквенно смотрим целевое слово
    for x in l_word:
        # Если рассматриваемая буква - гласная...
        if x in lower_vowels:
            # Сначала обязательно увеличиваем счётчик гласных
            count_of_vowels += 1
            # Затем, если эта гласная - это ответ пользователя...
            if count_of_vowels == int(answer):
                # Записываем эту букву в печатном виде
                user_word += x.capitalize()
            else:
                # Иначе записываем строчную гласную
                user_word += x
        else:
            # В ином случае записываем согласную
            user_word += x

    # Избавляемся от переводов строк
    word = word.rstrip("\n")
    user_word = user_word.rstrip("\n")

    # Выводим текст на экран
    os.system("cls")
    print("\n\n\t --- НЕВЕРНО! ---")
    print("\n\t" + user_word + " - ваш ответ")
    print("\t" + word + " - правильно\n")

    os.system("pause")
    os.system("cls")


# TODO: Объединить question() и repeat_question()
def question(number, word, amount):
    """Печатает вопрос на экран."""

    # Вначале оформляем визуальную подсказку для порядковых номеров гласных
    display_vowels_order, amount_of_vowels = define_order_of_vowels(word)

    # Печатаем на экран
    print("\n\n\t--- ВОПРОС #" + str(number) + " из " + str(amount) + " ---")
    print("\n\t" + display_vowels_order)
    print("\t" + word.lower())

    # Возвращаем полученное макс. количество гласных в слове
    return amount_of_vowels


def repeat_question(word):
    # Вначале оформляем визуальную подсказку для порядковых номеров гласных
    display_vowels_order, amount_of_vowels = define_order_of_vowels(word)
    # Печатаем на экран
    print("\n\n\t--- ПОВТОРЕНИЕ ---")
    print("\n\t" + display_vowels_order)
    print("\t" + word.lower())
    # Возвращаем полученное макс. количество гласных в слове
    return amount_of_vowels


def results(score, amount_of_questions):
    """Отображает результат тренировки и даёт соответствующий комментарий."""

    one_percent = amount_of_questions / 100  # Определили один процент от общего числа вопросов

    first_grade = amount_of_questions  # Ответили на все вопросы
    second_grade = int(one_percent * 75)  # Ответили на 75% вопросов
    third_grade = int(one_percent * 50)  # Ответили на 50% вопросов
    fourth_grade = int(one_percent * 25)  # Ответили на 25% вопросов
    fifth_grade = 0  # Не ответили ни на один вопрос

    # После получения результата отображаем его и даём соответствующий комментарий.
    print("\n\n\t--- РЕЗУЛЬТАТ ---")
    print("\n\t" + str(score) + " правильных ответов из " + str(amount_of_questions) + ".\n")

    # Ответили на все вопросы
    if score >= first_grade:
        print("\tПрекрасный результат! Вы великолепны!\n")

    # Ответили на 99%-75% вопросов
    elif first_grade > score >= second_grade:
        print("\tВы весьма неплохо справляетесь! В следующий раз у вас получится \
набрать 100%, будьте уверены в этом.\n")

    # Ответили на 74%-50%
    elif second_grade > score >= third_grade:
        print("\tХорошо потрудились! Продолжайте в том же духе!\n")

    # На 49%-25%
    elif third_grade > score >= fourth_grade:
        print("\tВ целом - неплохо, но есть куда стремиться!\n")

    # 24%-0%
    elif fourth_grade > score >= fifth_grade:
        print("\tРезультат не впечатляет... Не расстраивайтесь! Отдохните и \
попробуйте ещё раз!\n")

    os.system("pause")
    os.system("cls")


# TODO: Объединить функции repeat() и training() так как они очень похожи.
def repeat(word_list):
    """Повторяем слова, в которых была допущена ошибка."""

    # Массив, хранящий количество успешных повторений для каждого из ошибочных слов.
    # Число три означает, сколько раз будем повторять каждое из слов.
    word_progress = [3] * len(word_list)

    print("\n\n\t--- ПОВТОРЕНИЕ ---")
    print("\n\tСейчас вы ещё раз будете практиковать те слова, в которых ошиблись во \
время сеанса. Чтобы закончить тренировку, правильно ответьте три раза на каждое из слов.\n")
    os.system("pause")
    os.system("cls")

    # Устанавливаем, все ли слова были повторены?
    is_all_words_repeated = False
    while not is_all_words_repeated:
        # Смотрим текущее слово...
        current_word = 0
        # Пока не прошли все слова из списка по-очереди...
        while current_word < len(word_list):
            # Проверяем, если текущее слово уже повторено достаточное количество раз,
            # то пропускаем его
            if word_progress[current_word] == 0:
                current_word += 1
                continue

            # Определяем слово из words.txt и ответ к нему
            q_word = define_word(word_list[current_word])
            true_answer = define_answer(word_list[current_word])

            # Если ответ единичный, то преобразуем его в тип списка для дальнейшей обработки
            # Правда мне кажется, что можно просто добавить переменную в созданный
            # список и назвать его потом true_answer, но я пока не хочу ничего
            # мудрить с этим. Потом как-нибудь. А может этого и вовсе не надо делать.
            if isinstance(true_answer, str):
                true_answer = true_answer.rstrip("\n")  # Отрезаем перевод строки
                true_answer = map(int, true_answer)  # Переводим в промежуточное состояние
                true_answer = list(true_answer)  # Из промежуточного - в тип-список

            # Используем отдельную функцию для отображения вопроса
            amount_of_vowels = repeat_question(q_word)

            # В цикле дожидаемся, пока пользователь введёт корректный ответ (число)
            while True:
                answer = input("Какая гласная по счёту является ударной? (0 - нет ответа)\n")
                try:
                    int(answer)
                except ValueError:
                    print("Вводи число, соответствующее порядковому НОМЕРУ ГЛАСНОЙ в слове!")
                else:
                    # Если введённый ответ больше количества гласных или меньше 0, то говорим об этом
                    if int(answer) > amount_of_vowels or int(answer) < 0:
                        print("Вводи число, которое не больше и не меньше количества гласных в слове!")
                    else:
                        break

            # Сверяем ответ пользователя с настоящим ответом и сообщаем ему о результате
            # выбранного решения. Если правильно - изменяем значение прогресса повторения
            # для данного слова. Иначе - сообщаем о неправильном ответе.
            if int(answer) in true_answer:
                correct(q_word)
                word_progress[current_word] -= 1
            else:
                incorrect(q_word, answer)

            current_word += 1

        # После того, как прошли все слова по порядку, смотрим, повторили ли мы их все
        if word_progress.count(0) >= len(word_progress):
            is_all_words_repeated = True

    print("\n\n\tПовторение закончено! Вы молодец!\n")
    os.system("pause")
    os.system("cls")


def training(*, amount_of_questions=10):
    """Начинаем тренировку."""

    # Задаём номер вопроса
    question_number = 1
    # Указываем текущий счёт тестирования
    score = 0
    # Создаём пустой список, в который потом будем записывать все те слова, которые уже были
    completed_words = []
    # Создаём список, в котором будут храниться слова, в которых была сделана ошибка
    bad_words = []

    # Определяем количество строк в words.txt
    f = open("words.txt", )
    amount_of_lines = len(f.readlines())
    f.close()

    # Предостерегаем от того, чтобы мы не смотрели больше слов, чем есть на самом деле
    if amount_of_lines < amount_of_questions:
        amount_of_questions = amount_of_lines

    # Если был введён ноль или менее него - проверяем все слова
    if amount_of_questions <= 0:
        amount_of_questions = amount_of_lines

    # Начинаем процесс тестирования до тех пор, пока не спросим десять слов
    while question_number <= amount_of_questions:
        # Определяем номер слова, которое будем загадывать и постараемся учесть,
        # что его ещё не было
        number_of_word = define_random_word(completed_words)
        # Если такого слова (числа) ещё не было - добавляем его в список.
        completed_words.append(number_of_word)

        # Исходя из полученного числа определяем строку со словом в words.txt
        q_word = define_word(number_of_word)

        # Ищем соответствующий правильный ответ для загаданного слова
        true_answer = define_answer(number_of_word)

        # Если ответ единичный, то преобразуем его в тип списка для дальнейшей обработки
        if isinstance(true_answer, str):
            true_answer = true_answer.rstrip("\n")  # Отрезаем перевод строки
            true_answer = map(int, true_answer)  # Переводим в промежуточное состояние
            true_answer = list(true_answer)  # Из промежуточного - в тип-список

        # Выводим на экран оформленный вопрос
        amount_of_vowels = question(question_number, q_word, amount_of_questions)

        # В цикле дожидаемся, пока пользователь введёт корректный ответ (число)
        while True:
            answer = input("Какая гласная по счёту является ударной? (0 - нет ответа)\n")
            try:
                int(answer)
            except ValueError:
                print("Вводи число, соответствующее порядковому НОМЕРУ ГЛАСНОЙ в слове!")
            else:
                # Если введённый ответ больше количества гласных или меньше 0, то говорим об этом
                if int(answer) > amount_of_vowels or int(answer) < 0:
                    print("Вводи число, которое не больше и не меньше количества гласных в слове!")
                else:
                    break

        # Сверяем ответ пользователя с настоящим ответом и сообщаем ему о результате
        # выбранного решения. Если правильно - добавляем очко в счёт
        if int(answer) in true_answer:
            correct(q_word)
            score += 1
        else:
            incorrect(q_word, answer)
            bad_words.append(number_of_word)

        # Увеличиваем номер вопроса
        question_number += 1

    # Отображаем результат тренировки
    results(score, amount_of_questions)

    # Проводим повторное заучивание ошибочных слов, если они есть
    if len(bad_words) > 0:
        repeat(bad_words)


def find_answers():
    """Вызывается при всяком запуске тренажёра и нажатии кнопки "Ввод".
    Просматривает файл words.txt и на основе заглавных букв в словах составляет
    файл с ответами - answers."""

    # Если не был обнаружен words.txt, то создаём его и заполняем несколькими словами
    # и сообщаем о ненахождении
    if not os.path.isfile("words.txt"):
        print("Файл \"words.txt\" не был обнаружен в директории с исполняемым файлом. \
Он будет заполнен несколькими словами.\nПожалуйста, установите исходный прилагаемый файл \
\"words.txt\" или настройте его самостоятельно в соответствии с инструкцией в \"README.txt\".")
        os.system("pause")
        os.system("cls")
        filler = "бАнты\nтОрты\nшАрфы\nпОрты\nсрЕдства\nИксы\nкрАны\nкОнусы\nлЕкторы\nпОручни"
        f = open("words.txt", "w")
        f.write(filler)
        f.close()

    # Открываем соответствующие файлы
    f = open("words.txt")
    t = open("answers", "w")

    while True:
        # Читаем строку в файле
        a_line = f.readline()
        # Отрезаем окончание
        a_line = a_line.rstrip("\n")

        # Прерываем цикл, если встречается пустая строка - это значит весь файл уже прочитан
        if not a_line:
            break

        # Иначе исследуем каждый символ в прочитанной строке, ведь строка - это одно слово.
        amount_of_vowels = 0
        # Переменная отвечает за то, была ли уже найдена заглавная буква или ещё нет
        found_percussive_vowel = False

        for x in a_line:
            # Если это строчная гласная, то просто увеличиваем количество гласных для этого слова.
            if x in lower_vowels:
                amount_of_vowels += 1

            # Если заглавная (ударная) гласная, то не только увеличиваем их количество, но
            # и записываем эту гласную как ответ к слову в файл answers,
            # а если есть и другие ударные гласные, то через "/" записываем и их
            elif x in upper_vowels:
                amount_of_vowels += 1
                if not found_percussive_vowel:
                    found_percussive_vowel = True
                    t.write(str(amount_of_vowels))
                elif found_percussive_vowel:
                    t.write("/")
                    t.write(str(amount_of_vowels))

        t.write("\n")  # Перевод строки после записи ответа для слова

    f.close()
    t.close()


# НАЧАЛО ПРОГРАММЫ
# Оно находится в цикле, для того, чтобы после завершения сеанса начать ещё один
while True:
    print("""\n\n\t\tОРФОЭПИЧЕСКИЙ ТРЕНАЖЁР v. 1.0.
        \t\t-------VovaOne (C) 2021-------\n
        Вам по очереди будут показаны слова без ударений.\n
        Ваша задача - ввести число, которое соответствует номеру ударной гласной в представленном слове.\n""")
    selected = input("Введите количество слов, которое вы хотите тренировать и нажмите \"Ввод\", чтобы начать.\
    \nВведя 0, вы будете тренировать все слова.\
    \nОставив ввод пустым, вы будете тренировать количество слов по-умолчанию.\n")
    # Выводим приветственный экран и получаем введённое пользователем значение
    os.system("cls")

    # Проверяем, число ли это, и если так, то оно будет являться количеством
    # вопросов в сеансе
    try:
        selected = int(selected)
    except ValueError:
        is_a_number = False
    else:
        is_a_number = True

    # Автоматически составляем файл с ответами при запуске.
    find_answers()

    # Начинаем тренировку в зависимости от того, что ввёл пользователь
    if is_a_number:
        training(amount_of_questions=selected)
    else:
        training()

    os.system("cls")