def driver(data):
    # Извлекаем данные о водителе
    first_name = data[0]
    middle_name = data[1] if len(data) > 1 else ""
    last_name = data[2]
    birth_date = data[3]
    gender = data[4]

    # Составляем номер водительского удостоверения
    driver_number = ""

    # 1-5 символы фамилии
    driver_number += last_name[:5].ljust(5, '9')

    # Цифра десятилетия от года рождения
    birth_year = int(birth_date[-4:])
    decade_digit = str(birth_year // 10)[-1]
    driver_number += decade_digit

    # Месяц рождения
    birth_month = birth_date[3:6]
    if gender == "F":
        birth_month_code = str(int(birth_month[:2]) + 50).zfill(2)
    else:
        birth_month_code = birth_month[:2]
    driver_number += birth_month_code

    # Дата в пределах месяца рождения
    birth_day = birth_date[:2]
    driver_number += birth_day.zfill(2)

    # Цифра года от года рождения
    birth_year_code = str(birth_year)[-1]
    driver_number += birth_year_code

    # Первые две инициалы имени и отчества
    initials = (first_name[0] + middle_name[0]).ljust(2, '9')
    driver_number += initials

    # Произвольная цифра
    driver_number += "9"

    # Две контрольные цифры компьютера
    driver_number += "AA"

    return driver_number
