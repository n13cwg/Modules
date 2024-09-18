def send_email(message, recipient, *,sender = 'university.help@gmail.com'):

    # Проверка на корректность адресов отправителя
    # Метод endswith() возвращает True, если строка заканчивается указанным суффиксом. Если нет, возвращается False
    if '@' not in sender or not sender.endswith(('.com', '.ru', '.net')):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    # Проверка на корректность адресов получателя
    if '@' not in recipient or not recipient.endswith(('.com', '.ru', '.net')):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    # Проверка на отправку самому себе
    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return

    # Проверка на отправителя по умолчанию
    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        return

    # Нестандартный отправитель
    print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')