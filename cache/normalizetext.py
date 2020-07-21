f = open("sample.txt", "r")
str = f.read()
f.close()
res = ''
for i in range(len(str)):
    if str[i] == 'เ' and  i != len(str):
        if str[i+1] == 'เ':
            res += 'แ'
    else:
        res += str[i]

text_file = open("result.txt", "w")
text_file.write(res)
text_file.close()

