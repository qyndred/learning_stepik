word_number = int(input())
dic = {}
for i in range(word_number):
    dic.update({i : input().lower()})
print(dic)

string_number = int(input())
mistakes = []

for i in range(string_number):
    s = input().lower().split()
    for word in s:
        if word not in dic.values():
            mistakes.append(word)

mistakes = set(mistakes)

for word in mistakes:
    print(str(word))

