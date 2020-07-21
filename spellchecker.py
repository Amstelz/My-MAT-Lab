#!/usr/bin/python3
# -*- coding: utf-8 -*-
################ Spelling Corrector 
import pylcs
import re
from collections import Counter

def words(text): return re.split(r'\s', text)

WORDS = Counter(words(open('big.txt').read()))

def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N

def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = " ู ุ ํ ็ ๋ ๊ ้ ่ ื ิ ั ีกขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮฯะัาำิีึืฺุู฿เแโใไๅๆ็่้๊๋์ํ๎๏๐๑๒๓๔๕๖๗๘๙๚"
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

if __name__ == '__main__':
    #print(unit_tests())
    #spelltest(Testset(open('spell-testset1.txt')))
    #spelltest(Testset(open('spell-testset2.txt')))
    io = ''
    while io != "end":
        io = input("อินพุท: ")
        print(correction(io))
    '''print('lcs of ปลาหมอ ,ปลาไหมลอ = {}'.format(pylcs.lcs('ปลาหมอ', 'ปลาไหมลอ')))
    print('lcs of ปลาไหล ,ปลาไหมลอ = {}'.format(pylcs.lcs('ปลาไหล', 'ปลาไหมลอ')))
    print('lcs of ปลาหมอ ,ปลาห = {}'.format(pylcs.lcs('ปลาหมอ', 'ปลาห')))
    print('lcs of ปลาไหล ,ปลาห = {}'.format(pylcs.lcs('ปลาไหล', 'ปลาห')))
    print(WORDS)'''
