# Орфоэпический тренажёр
#### v. 2.0 (от 02.05.21)  |  Сделал Vladimir T. (VovaOne) © 2021

![GIF-Demo](demonstration/orthoepic-trainer-2-0-0.gif)

## Новое в версии 2.0
- Добавлен графический интерфейс.
- Добавлена возможность настраивать работу тренажёра:
	- Количество слов по-умолчанию. Устанавливается при любом некорректном значении в поле ввода в главном меню, а также, если это поле пустое.
	- Количество повторений для слова. Введённое значение определяет то, сколько раз вам нужно правильно поставить ударение в словах, в которых вы допустили ошибку раннее, в режиме повторения.
	- Автоматический переход к следующему слову. Можно установить задержку в мсек, после которой произойдёт переход к следующему слову. Если отключено, то переход будет осуществляться вручную.
- Оформленное окно результатов. В нём можно перейти к режиму повторения, пройти тренировку с текущими настройками ещё раз, вернуться в меню или выйти из программы.

## Описание
Приложение позволяет тренировать постановку ударения в словах.

## Системные требования
**OS:** Windows 7/8/10 (x64)  
**Hard Drive:** ~200MB

## Особенности
- Бесплатно!
- Возможность добавления своих слов для тренировки.
- Можно выбрать, какое количество слов вы будете тренировать за сеанс.
- Возможность повторения тех слов, в которых вы допустили ошибку.
- Приятный и понятный визуальный стиль интерфейса.
- Поддержка слов с несколькими ударениями и поддержка примеров употребления для данного слова.
- Используется более чем 300 слов из орфоэпического словаря ФИПИ.
(https://fipi.ru/navigator-podgotovki/navigator-ege#ru)
- Допустимо модифицировать код для собственного удобства при знании Python.

## Добавление своих слов
1. Откройте words.txt
2. Оформите текстовый документ соотвествующим образом - просто соблюдайте следующие правила:
  - Одна строка - одно слово.
  - Ударная(-ые) гласная(-ые) в слове, должны быть заглавными. В слове хотя бы одна буква должна быть заглавное, иначе вы рискуете столкнуться с некорректным "правильным ответом" на вопрос.
  - Не оставляйте в конце файла пустую строку или строки, иначе вы рискуете столкнуться с пустым вопросом в тренажёре.
  - Чтобы добавить пример к слову, заключите пример в круглые скобки.
  - Рекомендуется не оставлять ненужных пробелов после слов.
3. Сохраните и закройте файл.

Так или иначе, предоставляемый изначально файл наглядно показывает вам, как его стоит оформлять.  
**ПРИ СОЗДАНИИ ФАЙЛА ИЛИ ЕГО ИЗМЕНЕНИИ, УБЕДИТЕСЬ, ЧТО КОДИРОВКОЙ ФАЙЛА ЯВЛЯЕТСЯ ANSI.** Откройте файл в стандартном блокноте Windows > "Сохранить как..." с выбранным параметром "Кодировка: ANSI".

## Запланированное
Автор подразумевает, что будет поддерживать разработку проекта. Вот список того, что может быть добавлено в будущем:
- [ ] **Автоматическое форматирование words.txt.** Пользователю придётся меньше заботиться о правильности оформления файла со словами. Например, будут автоматически убираться лишние символы, обнаруживаться и убираться дубликаты, пустые строки и т. д.
- [ ] **Умное предложение слов.** Программа будет чаще предлагать те слова, в которых у пользователя чаще всего возникали ошибки.
- [ ] **Адаптивный дизайн.** Чтобы можно было развернуть на весь экран.
- [ ] **Тёмная тема.**
- [ ] **Кнопка "В меню" во время сессии.**
- [ ] **Статистика верных/неверных ответов и сколько ещё вопросов осталось.**
- [ ] **Возможность намеренного добавления слова для повторения** даже если был дан верный ответ.
- [ ] **Оформление имени собственного.** Если указано имя собственное, то пользователю нужно будет поставить в файлу у этого слова пометку, которая даст алгоритму понять, что перед ним имя нарицательное и первая букву в нём не является ударной.
- [ ] **Досрочное завершение сессии.**
- [ ] **Поддержка английского языка.**

## Для тех, кто разработчик
*Мимопроходящий* и неравнодушный, конечно, может помочь мне с перечисленным в списке, но в остальном же этот список создан для меня самого.

- [ ] **Тестирование работоспособности кода.** Не то, чтобы я не слышал про юнит-тесты, просто они должны быть. Но их нет. А должны...
- [ ] **Большое количество букв в слове.** Следовало бы анализировать количество букв и задавать соответствующие стили элементам интерфейса.
- [ ] **Проблемы с кодировками.** У меня не было особого желания углубляться в это. Программа не в состоянии читать текстовые файлы в кодировке, отличной от ANSI. Нужно исправить.
- [ ] **Debug-режим.** Структура программы усложняется. Будет не лишним со временем добавить возможность выводить лог работы программы, чтобы было проще отлавливать ошибки при использовании программы другими пользователями.
- [ ] **Улучшенное взаимодействие с программой.** Можно будет полноценно использовать только клавиатуру. Также при запуске будет автоматически устанавливаться фокус на окно ввода количества слов, а при нажатии на Enter будет начата тренировка и так далее...
- [ ] **Скрытие кнопки "Повторение"** если всё было решено верно.
- [ ] **Скрытие кнопок после окончания повторения.**
- [ ] **English.** В том числе перевод комментариев на английский, а также перевод интерфейса программы. Да и всего репозитория короче...

### Как начать работу?
1. Установить Python 3.8 (3.8.7 в моём случае).
2. Установить PySide6 6.0.1. Установка производилась в соответствии с официальной инструкцией - https://doc.qt.io/qtforpython/quickstart.html
3. Клонировать репозиторий.

*Для редактирования .ui, использовать поставляемый вместе с PySide QtDesigner. Для конвертировывания .ui в .py использовать ui\convert.bat. Для .qrc -> .py использовать res_convert.bat*
