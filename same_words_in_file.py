filename_in = r'C:\Users\Ririka1366\Downloads\dataset_3363_3 (1).txt'
filename_out = r'C:\Users\Ririka1366\Downloads\dataset_3363_3_out.txt'


# Функция чтения файла построчно в список
def ReadFile(filename):
    str_in = []
    with open(filename) as import_file:
        for line in import_file:
            str_in.append(line.strip())
    return str_in


# Функция сохранения списка построчно
def SaveFile(filename, strings_of_file):
    with open(filename, "w") as export_file:
        for line in strings_of_file:
            export_file.write(line + "\n")


# Функция декомперссии (a1b8)
def UncompressString(s):
    nom = 0
    new_str = ""
    while nom < len(s):
        ch1 = str(s[nom])
        ch2 = ""
        while nom + 1 < len(s) and s[nom + 1].isdigit():
            ch2 += str(s[nom + 1])
            nom += 1
        new_str += str(ch1 * int(ch2))
        nom += 1
    return new_str


# Функция словарь пословно с количеством ('aaa': 8)
def WordCountInDict(list_in):
    dict = {}
    for line in list_in:
        list_words = line.split()
        for word in list_words:
            if word not in dict:
                dict[word] = 1
            else:
                dict[word] = dict[word] + 1
    return dict


# Функция поиск максимума по значению в словаре
def MaxInDict(dict_in):
    max_key = ""
    max_value = 0
    for key, val in dict_in.items():
        if max_value < val:
            max_value = val
            max_key = key
    return max_key


# Словарик
dic = {}
strings_of_file = ""

# Получить список
strings_of_file = ReadFile(filename_in)

# Список в словарь
dic = WordCountInDict(strings_of_file)

# Максимальное значение в словаре
max_dic = MaxInDict(dic)

# Максимум в список
strings_of_file.clear()
strings_of_file.append(max_dic + " " + str(dic[max_dic]))

# Список в файл
SaveFile(filename_out, strings_of_file)
