emp_name = ''
dates = ''


def setup_profile(name, vacation_dates):
    global emp_name, dates
    emp_name = name
    dates = vacation_dates


def print_application_for_leave():
    global emp_name, dates
    print('Заявление на отпуск в период', dates + '.', emp_name)


def print_holiday_money_claim(amount):
    global emp_name
    print('Прошу выплатить', amount, 'отпускных денег.', emp_name)


def print_attorney_letter(to_whom):
    global emp_name, dates
    print('На время отпуска в период', dates, 'моим заместителем назначается',
          to_whom + '.', emp_name)
