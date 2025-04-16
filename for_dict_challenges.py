# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
# ???
name_counts = {}
for student in students:
    name = student['first_name']
    if name in name_counts:
        name_counts[name] += 1
    else:
        name_counts[name] = 1

for name, count in name_counts.items():
    print(f"{name}: {count}")

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
# ???
name_counts = {}
for student in students:
    name = student['first_name']
    name_counts[name] = name_counts.get(name, 0) + 1

most_common = max(name_counts.items(), key=lambda x: x[1])
print(f"Самое частое имя среди учеников: {most_common[0]}")

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ], [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
# ???
for class_num, class_students in enumerate(school_students, 1):
    name_counts = {}
    for student in class_students:
        name = student['first_name']
        name_counts[name] = name_counts.get(name, 0) + 1
    most_common = max(name_counts.items(), key=lambda x: x[1])
    print(f"Самое частое имя в классе {class_num}: {most_common[0]}")

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [
        {'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [
        {'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {
        'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# ???
for class_info in school:
    class_name = class_info['class']
    boys = 0
    girls = 0
    for student in class_info['students']:
        name = student['first_name']
        if is_male[name]:
            boys += 1
        else:
            girls += 1
    print(f"Класс {class_name}: девочки {girls}, мальчики {boys}")

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [
        {'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [
        {'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???
class_stats = []
for class_info in school:
    boys = sum(
        1 for student in class_info['students'] if is_male[student['first_name']])
    girls = len(class_info['students']) - boys
    class_stats.append({
        'class': class_info['class'],
        'boys': boys,
        'girls': girls
    })

max_boys_class = max(class_stats, key=lambda x: x['boys'])
max_girls_class = max(class_stats, key=lambda x: x['girls'])

print(f"Больше всего мальчиков в классе {max_boys_class['class']}")
print(f"Больше всего девочек в классе {max_girls_class['class']}")
