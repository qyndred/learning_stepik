filename_in = r'C:\Users\Ririka1366\Downloads\dataset_3363_4.txt'
filename_out = r'C:\Users\Ririka1366\Downloads\dataset_3363_4_out.txt'


#Ф-ция чтения из файла
def readFile(filename):
    str_in = []
    with open(filename) as import_file:
        for line in import_file:
            str_in.append(line.strip().split(';'))
    return str_in


#Ф-ция записи в файл
def writeFile(filename, strings_of_file):
    with open(filename, "w") as export_file:
        for line in strings_of_file:
            export_file.write(str(line) + '\n')


#Ф-ция рассчета среднего значения(на вход подается список)
def average_counter(lst):
    res = 0
    l = len(lst)
    for i in range(l):
        res += int(lst[i])
    res /= l
    return res


#считываем данные из файла
list_of_strings = ''
list_of_strings = readFile(filename_in)


#Убираем из считанного списка все, что не связано с числами(столбец с фамилиями)
for lst in list_of_strings:
    for i in lst:
        if not i.isdigit():
            lst.remove(i)


#Считаем средее для каждого ученика
list_of_averages = []
for lst in list_of_strings:
    list_of_averages.append(str(average_counter(lst)))


#Считаем среднее по каждому предмету
list_of_subjects = []
result = ''
j = 0
while j < len(list_of_strings[0]):
    for lst in list_of_strings:
        list_of_subjects.append(lst[j])
    result += str(average_counter(list_of_subjects)) + ' '
    list_of_subjects.clear()
    j += 1


#добавляем среднее по предмету в список со средними баллами для каждого ученика
list_of_averages.append(str(result))


#пишем итоги рассчетов в файл
writeFile(filename_out, list_of_averages)

