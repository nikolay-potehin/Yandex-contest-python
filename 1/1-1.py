def get_type(x):
    try:
        int(x)
        return x + ' (int)'
    except ValueError:
        if x == 'да':
            return 'True (bool)'
        elif x == 'нет':
            return 'False (bool)'
        else:
            return x + ' (str)'


job_name = input('Введите название вакансии: ')
job_description = input('Введите описание вакансии: ')
required_experience = input('Введите требуемый опыт работы (лет): ')
salary_low_border = input('Введите нижнюю границу оклада вакансии: ')
salary_high_border = input('Введите верхнюю границу оклада вакансии: ')
free_schedule = input('Есть ли свободный график (да / нет): ')
is_job_premium = input('Является ли данная вакансия премиум-вакансией (да / нет): ')

for i in ([job_name, job_description, required_experience, salary_low_border, salary_high_border,
           free_schedule, is_job_premium]):
    print(get_type(i))
