#Задание строки
# Напишите 4 переменных которые буду обозначать следующие данные:
# Количество выполненных ДЗ (запишите значение 12)
# Количество затраченных часов (запишите значение 1.5)
# Название курса (запишите значение 'Python')
# Время на одно задание (вычислить используя 1 и 2 переменные)
# Выведите на экран(в консоль), используя переменные, следующую строку:
# Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.

# Пример написанного кода:
# first_name = 'Vasya'
# apple_count = 10
# second_name = 'Petya'
# orange_count = 15
# print(first_name, 'дал', second_name, apple_count, 'яблок и', orange_count, 'апельсинов')

# Результат выполнения кода:
# Vasya дал Petya 10 яблок и 15 апельсинов

quantity_homework = 12
quantity_of_hours = 1.5
name_cours = 'Python'
time_of_one_thing = (quantity_of_hours/quantity_homework)
print("Время на выполнение одного задания",time_of_one_thing,"часа")
print("Курс: ",name_cours+", всего задач: ",quantity_homework,", затрачено часов: " ,quantity_of_hours, ", среднее время выполнения: ",time_of_one_thing, " часа", sep="")