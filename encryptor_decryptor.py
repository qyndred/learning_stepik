str_input = 'abcd'
str_encrypted = '*d%#'
str_to_encrypt = 'abacabadaba'
str_to_decrypt = '#*%*d*%'

dic = {}
reversed_dic = {}
r_enc = ''
r_dec = ''

for i in range(len(str_input)):
    dic[str_input[i]] = str_encrypted[i]
    reversed_dic[str_encrypted[i]] = str_input[i]
print(dic)
print(reversed_dic)

for i in str_to_encrypt:
    if i in dic.keys():
        r_enc += str(dic.get(i))
print(r_enc)

for i in str_to_decrypt:
    if i in reversed_dic.keys():
        r_dec += str(reversed_dic.get(i))
print(r_dec)