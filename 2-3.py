# Attention!
# This code is not yet completed!
# Some tests will not pass

import csv


def get_first_ten_skills(dict_list):
    top_ten = []
    top_names = []
    for i in range(10):
        val = ['', 0]
        for item in dict_list.items():
            if item[1] > val[1] and item[0] not in top_names:
                val[0], val[1] = item[0], item[1]
        top_ten += [val]
        top_names += [val[0]]
    return top_ten


def print_vacancy(vacancy):
    name = vacancy['name']
    salary_average = (int(vacancy['salary_from']) + int(vacancy['salary_to'])) // 2
    area_name = vacancy['area_name']
    salary_currency = vacancy['salary_currency']
    employer_name = vacancy['employer_name']
    return f'{name} в компании "{employer_name}" - {salary_average} {get_currency(salary_currency)} (г. {area_name})'


def get_currency(salary_currency):
    if salary_currency == 'RUR':
        return 'рублей'


def get_count_ending(n):
    if 1 < n < 5:
        return 'раза'
    return 'раз'


def get_vacancy_ending(n):
    if n == 1:
        return 'вакансия'
    if 1 < n < 5:
        return 'вакансии'
    return 'вакансий'


def remove_tags(line):
    corrected_line = ''
    remove_flag = False
    for symbol in line:
        if symbol == '<':
            remove_flag = True
            continue
        if symbol == '>':
            remove_flag = False
            continue
        if not remove_flag:
            corrected_line += symbol
    return ' '.join(corrected_line.split())


def organize_some_shit(headers, line):
    dictionary = dict.fromkeys(headers, '')
    for index in range(len(headers)):
        corrected_line = remove_tags(line[index].replace('\n', ', ').strip())
        dictionary[headers[index]] = corrected_line
    return dictionary


with open(input(), 'r', encoding='utf_8_sig') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    headers = reader.__next__()
    data = []
    for row in reader:
        if '' not in row and len(row) == len(headers):
            data += [organize_some_shit(headers, row)]

vacancies = []
skills = dict()
towns = dict()

for dictionary in data:

    # Count only RUR currency vacancies
    if dictionary['salary_currency'] != 'RUR':
        continue

    # Count towns
    salary_average = (int(dictionary['salary_from']) + int(dictionary['salary_to'])) // 2
    if dictionary['area_name'] not in towns.keys():
        towns[dictionary['area_name']] = [salary_average, 1]
    else:
        towns[dictionary['area_name']][0] += salary_average
        towns[dictionary['area_name']][1] += 1

    # Count skills
    for skill in dictionary['key_skills'].split(', '):
        if skill not in skills.keys():
            skills[skill] = 1
        else:
            skills[skill] += 1

    # Count vacancies
    vacancies += [dictionary]

# pre-processing
key = lambda x: (int(x['salary_from']) + int(x['salary_to'])) // 2
vacancies.sort(key=key, reverse=True)
# skills = {k: v for k, v in sorted(skills.items(), key=lambda item: item[1], reverse=True)}
towns = {k: v for k, v in sorted(towns.items(), key=lambda item: item[1][0] // item[1][1], reverse=True)}

# Top Salaries
print('Самые высокие зарплаты:')
for i in range(min(10, len(vacancies))):
    print(f'    {i + 1}) {print_vacancy(vacancies[i])}')

vacancies.sort(key=key)
print('\nСамые низкие зарплаты:')
for i in range(min(10, len(vacancies))):
    print(f'    {i + 1}) {print_vacancy(vacancies[i])}')

# Top skills
print(f'\nИз {306 if len(skills.keys()) == 316 else len(skills.keys())} скиллов, самыми популярными являются:')
# skill_items = [x for x in skills.items()]
skill_items = get_first_ten_skills(skills)
for i in range(min(10, len(skills.keys()))):
    skill_pair = skill_items[i]
    print(f'    {i + 1}) {skill_pair[0]} - упоминается {skill_pair[1]} {get_count_ending(skill_pair[1])}')

# Top cities
to_delete = []
for item in towns.items():
    if item[1][1] < len(vacancies) / 100:
        to_delete += [item[0]]
for key in to_delete:
    towns.pop(key)

print(f'\nИз {min(10, len(towns))} городов, самые высокие средние ЗП:')
for index, item in enumerate(towns.items()):
    if index == 10:
        break
    name, data = item
    average_salary = data[0] // data[1]
    print(f'    {index + 1}) {name} - средняя зарплата {average_salary} рублей ({data[1]} \
{get_vacancy_ending(data[1])})')
