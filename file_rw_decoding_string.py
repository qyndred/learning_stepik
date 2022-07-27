file = r"C:\Users\Ririka1366\Downloads\dataset_3363_2.txt"
with open(file, 'r') as f:
    s = f.read().lower().strip()

s2 = ''
for c in range(len(s)):
    if s[c].isalpha():
        if c + 3 < len(s) and s[c + 1].isdigit() and s[c + 2].isdigit() and s[c + 3].isdigit():
            print(s[c], int(s[c + 1:c + 4]))
            s2 += s[c] * int(s[c + 1:c + 4])
        elif c + 2 < len(s) and s[c + 1].isdigit() and s[c + 2].isdigit():
            print(s[c], int(s[c + 1:c + 3]))
            s2 += s[c] * int(s[c + 1:c + 3])
        elif c + 1 < len(s) and s[c + 1].isdigit():
            print(s[c], int(s[c + 1:c + 2]))
            s2 += s[c] * int(s[c + 1])

with open(file, 'w') as f:
    s = f.write(s2)
