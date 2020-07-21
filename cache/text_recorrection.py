#text_recorrection
#!/usr/bin/python3
# -*- coding: utf-8 -*-
def ae_to_air_s1(list_of_word):
    for word_sequence in range(len(list_of_word)):
        if list_of_word[word_sequence] == 'เ':
            proword = list(list_of_word[word_sequence+1])
            proword[0] = "แ"
            resword = ""
            for spell in proword:
                resword = resword + spell
            list_of_word[word_sequence+1] = resword
    remove_ae_time = list_of_word.count("เ")
    for time in range(remove_ae_time):
        list_of_word.remove("เ")
    return ae_to_air_s2(list_of_word)

def ae_to_air_s2(list_of_word):
    for word_seq in range(len(list_of_word)):
        pro_word_list = list(list_of_word[word_seq])
        remove_pmark = []
        for spell_seq in range(len(pro_word_list)):
            if pro_word_list[spell_seq] == 'เ' and pro_word_list[spell_seq+1] == 'เ':
                pro_word_list[spell_seq] = "แ"
                remove_pmark.append(spell_seq+1)
        new_word = ""
        for spell_seq in range(len(pro_word_list)):
            if spell_seq not in remove_pmark:
                new_word = new_word + pro_word_list[spell_seq]
        list_of_word[word_seq] = new_word
    return list_of_word
test = ["เ","เละ","ไม่","สหภาพเเรงงาน","กระทรวงเเรงงาน"]
ae_to_air_s1(test)
print(test)
