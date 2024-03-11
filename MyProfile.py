# MyProfile app
SEPARATOR = '------------------------------------------'

# user profile
name_user, years_user, phone_number_user, e_mail_user, additional_info_user = '-', 0, '-', '-', '-'
#social links
vk_url_user, telegram_user, tiktok_user = '-', '-', '-'
#business_data
ogrnip_user, inn_user, payment_account_user, name_bank_user, bik_user, correspondent_account_user = 0, 0, 0, '-', 0, 0

def personal_info_user(name, years, phone_number, e_mail, additional_info, vk, tg, tktk):
    print(SEPARATOR)
    print('Имя:    ', name)
    years_parameter = ''
    if years == 0:
        years = '-'
    elif 11 <= years % 100 <= 19:
        years_parameter = 'лет'
    elif years % 10 == 1:
        years_parameter = 'год'
    elif 2 <= years % 10 <= 4:
        years_parameter = 'года'
    elif years != '-':
        years_parameter = 'лет'

    print('Возраст:', years, years_parameter)
    print('Телефон:', phone_number)
    print('E-mail: ', e_mail)

    print('\nСоциальные сети и мессенджеры:')
    print('Вконтакте:', vk)
    print('Telegram: ', tg)
    print('Tiktok:   ', tktk)

    if additional_info_user:
        print('\nДополнительная информация:')
        print(additional_info)

def print_info_business_data(strin, data):
    if data == 0:
        print(strin, '-')
    else:
        print(strin, data)

def print_business_data(ogrnip, inn, payment_account, name_bank, bik, correspondent_account):
    print(SEPARATOR)
    print('Данные предпринимателя:')

    print_info_business_data('ОГРНИП: ', ogrnip)
    print_info_business_data('ИНН: ', inn)
    print_info_business_data('Рассчетный счет: ', payment_account)
    print('Название банка: ', name_bank)
    print_info_business_data('БИК: ', bik)
    print_info_business_data('Корреспондентский счет: ', correspondent_account)

def change_info():
    global name_user, years_user, phone_number_user, e_mail_user, additional_info_user, \
        vk_url_user, telegram_user, tiktok_user, ogrnip_user, inn_user, payment_account_user, \
        name_bank_user, bik_user, correspondent_account_user
    while True:
        print(SEPARATOR)
        print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
        print('1 - Личная информация')
        print('2 - Информация о предпринимателе')
        print('0 - Назад')

        option2 = int(input('Введите номер пункта меню: '))
        if option2 == 0:
            break
        if option2 == 1:
            # input general info
            name_user = input('Введите имя: ')
            while 1:
                # validate user age
                years_user = int(input('Введите возраст: '))
                if years_user > 0:
                    break
                print('Возраст должен быть положительным')

            new_phone_number = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
            phone_number_user = ''
            for ch in new_phone_number:
                if ch == '+' or ('0' <= ch <= '9'):
                    phone_number_user += ch

            e_mail_user = input('Введите адрес электронной почты: ')

            vk_url_user = input('Введите адрес профиля Вконтакте: ')
            telegram_user = input('Введите логин Telegram: ')
            tiktok_user = input('Введите логин Tiktok: ')

            additional_info_user = input('Введите дополнительную информацию:\n')

        elif option2 == 2:
            while 1:
                ogrnip_user = input('Введите ваш ОГРНИП: ')
                if len(ogrnip_user) == 15:
                    ogrnip_user = int(ogrnip_user)
                    break
                print('Номер ОГРНИП должен содержать 15 цифр')
            inn_user = int(input('Введите ваш ИНН: '))
            while 1:
                payment_account_user = input('Введите ваш расчетный счет: ')
                if len(payment_account_user) == 20:
                    payment_account_user = int(payment_account_user)
                    break
                print('Номер расчетного счета должен содержать 20 цифр')
            name_bank_user = input('Введите название банка: ')
            bik_user = int(input('Введите БИК: '))
            correspondent_account_user = int(input('Введите корреспондентский счет: '))
        else:
            print('Введите корректный пункт меню')

def print_all_info():
    while True:
        print(SEPARATOR)
        print('ВЫВЕСТИ ИНФОРМАЦИЮ')
        print('1 - Личная информация')
        print('2 - Вся информация')
        print('0 - Назад')

        option2 = int(input('Введите номер пункта меню: '))
        if option2 == 0:
            break
        if option2 == 1:
            personal_info_user(name_user, years_user, phone_number_user, e_mail_user, additional_info_user, vk_url_user,
                               telegram_user, tiktok_user)

        elif option2 == 2:
            personal_info_user(name_user, years_user, phone_number_user, e_mail_user, additional_info_user, vk_url_user,
                               telegram_user, tiktok_user)
            print_business_data(ogrnip_user, inn_user, payment_account_user, name_bank_user, bik_user,
                                correspondent_account_user)
        else:
            print('Введите корректный пункт меню')




print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        change_info()

    elif option == 2:
        # submenu 2: print info
        print_all_info()
    else:
        print('Введите корректный пункт меню')