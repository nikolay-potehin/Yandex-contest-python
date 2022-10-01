def get_average_salary(low_border_str, high_border_str):
    low_border = int(low_border_str)
    high_border = int(high_border_str)
    average = int((low_border + high_border) / 2)
    return str(average) + ' ' + get_rubles_case(average)


def get_rubles_case(number):
    if number == 1:
        return 'рубль'
    if 1 < number < 5:
        return 'рубля'
    return 'рублей'


def get_years_case(years):
    if years == 1:
        return 'год'
    if 1 < years < 5:
        return 'года'
    return 'лет'


def is_number(string):
    try:
        int(string)
        return 1
    except ValueError:
        return 0


def is_bool(string):
    if string == 'да' or string == 'нет':
        return 1
    return 0


def smart_asking(question, expected_answer_type):
    answer = input(question)
    if is_number(answer):
        if expected_answer_type == int:
            return answer
    elif is_bool(answer):
        if expected_answer_type == bool:
            return answer
    elif expected_answer_type == str:
        if answer != '':
            return answer
    print('Данные некорректны, повторите ввод')
    return smart_asking(question, expected_answer_type)


job_name = smart_asking('Введите название вакансии: ', str)
job_description = smart_asking('Введите описание вакансии: ', str)
required_experience = smart_asking('Введите требуемый опыт работы (лет): ', int)
salary_low_border = smart_asking('Введите нижнюю границу оклада вакансии: ', int)
salary_high_border = smart_asking('Введите верхнюю границу оклада вакансии: ', int)
free_schedule = smart_asking('Есть ли свободный график (да / нет): ', bool)
is_job_premium = smart_asking('Является ли данная вакансия премиум-вакансией (да / нет): ', bool)

print(job_name)
print('Описание: ' + job_description)
print('Требуемый опыт работы: ' + required_experience + ' ' + get_years_case(int(required_experience)))
print('Средний оклад: ' + get_average_salary(salary_low_border, salary_high_border))
print('Свободный график: ' + free_schedule)
print('Премиум-вакансия: ' + is_job_premium)
