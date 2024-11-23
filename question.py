
# Множество (исходник):

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print("Множество:",students, type(students))

# Преобразование множества в список:

list_of_students = list(students)
print("Преобразование множества в список:", list_of_students, type(list_of_students))     # Вывод: ...['Johnny', 'Aaron', 'Khendrik', 'Steve', 'Bilbo'] <class 'list'> (порядок может быть разным)


# Сортировка списка:

list_of_students = sorted(list(students))
print("Отсортированный список учеников по алфавиту:", list_of_students, type(list_of_students))

list_of_students = sorted(students)
print("Отсортированный список учеников по алфавиту:", list_of_students, type(list_of_students))

# Вопрос! Почему одинаковый результат на выводе в консоль, тип данных (<class 'list'>),
# если сортируется list(students) и просто students, ведь это Множество? Как правильно?