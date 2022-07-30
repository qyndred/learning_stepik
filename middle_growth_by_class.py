filename_in = r'C:\Users\Ririka1366\Downloads\dataset_3380_5.txt'
growth = []

with open(filename_in, 'r', encoding='utf-8') as import_file:
    for line in import_file:
        growth.append(line.strip().split(sep='\t'))

dic = dict.fromkeys([i for i in range(1, 12)], '-')
for i in range(1, 12):
    cnt = 0
    class_growth = 0
    for line in growth:
        if i == int(line[0]):
            class_growth += int(line[2])
            cnt += 1
            dic.update({i: class_growth / cnt})

for key, value in dic.items():
    print(key, value, sep=' ', end='\n')