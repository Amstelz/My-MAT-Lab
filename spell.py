from pythainlp import word_tokenize
from pythainlp import spell
from pythainlp.util import normalize
from pythainlp.corpus import ttc
from pythainlp.spell import NorvigSpellChecker

text = open("result/testresult.txt", "r")

res = ''
new_word = []
for word in text:
    res += word
print(res)
print("***************************************************************************************************************************")
result = word_tokenize(res,keep_whitespace=False)
#print(result)
#checker = NorvigSpellChecker(custom_dict=ttc.word_freqs())
#result = normalize(result)

#new_word.append(spell(result[17])[0])
                
for word in result:
    new_word.append(spell(word)[0])

for word in new_word:
    print(word,end='')

print(spell("ก"))
