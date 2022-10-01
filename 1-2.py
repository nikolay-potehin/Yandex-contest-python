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


job_name = input('Введите название вакансии: ')
job_description = input('Введите описание вакансии: ')
required_experience = input('Введите требуемый опыт работы (лет): ')
salary_low_border = input('Введите нижнюю границу оклада вакансии: ')
salary_high_border = input('Введите верхнюю границу оклада вакансии: ')
free_schedule = input('Есть ли свободный график (да / нет): ')
is_job_premium = input('Является ли данная вакансия премиум-вакансией (да / нет): ')

print(job_name)
print('Описание: ' + job_description)
print('Требуемый опыт работы: ' + required_experience + ' ' + get_years_case(int(required_experience)))
print('Средний оклад: ' + get_average_salary(salary_low_border, salary_high_border))
print('Свободный график: ' + free_schedule)
print('Премиум-вакансия: ' + is_job_premium)
