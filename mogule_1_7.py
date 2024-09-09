grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразовали в списое и отсортировали
students_list = list(sorted(students))
print(students_list)

# Вычисляем среднее для каждого вложенного списка
average_grades = [(sum(grades[0]) / len(grades[0])),(sum(grades[1]) / len(grades[1])),(sum(grades[2]) / len(
grades[2])),(sum(grades[3]) / len(grades[3])),(sum(grades[4]) / len(grades[4]))]
print(average_grades)

# Объеденяем списки в словарь
students_dict = dict(zip(students_list, average_grades))
print(students_dict)
