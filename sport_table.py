game_count = int(input())
lst = []
for i in range(game_count):
    lst.append(input().split(';'))

r_tab = {}
r_team = []
for line in lst:
    for item in line:
        if not item.isdigit():
            r_team.append(item)
            r_tab.update({item: [r_team.count(item), 0, 0, 0, 0]})
r_team.clear()

for line in lst:
    if int(line[1]) < int(line[3]):
        r_tab[line[0]][3] += 1
        r_tab[line[2]][1] += 1
    elif int(line[1]) > int(line[3]):
        r_tab[line[0]][1] += 1
        r_tab[line[2]][3] += 1
    else:
        r_tab[line[0]][2] += 1
        r_tab[line[2]][2] += 1

for key in r_tab:
    r_tab[key][4] = r_tab[key][1] * 3 + r_tab[key][2]

for key, value in r_tab.items():
    print((key+':'), *value, end='\n')