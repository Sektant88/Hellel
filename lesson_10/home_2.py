# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные (4 функции input()).
# Создать файл и записать в него первые 2 строки и закрыть файл.
# Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
# В итоговом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.

line_1 = input("Введите первую строку: ")
line_2 = input("Введите вторую строку: ")
line_3 = input("Введите третью строку: ")
line_4 = input("Введите четвёртую строку: ")
with open('hw_02.txt', 'w') as f:
	f.writelines([line_1 + '\n', line_2])
with open('hw_02.txt', 'a') as f:
	f.write('\n' + line_3 + '\n' + line_4)
