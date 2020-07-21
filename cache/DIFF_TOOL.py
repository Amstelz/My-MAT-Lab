#DIFF_TOOL
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import difflib as diff
import io
import text_recorrection
from pythainlp import word_tokenize as word_tok

def text_diff(original_text,canidate_text):
    with io.open("{}.txt".format(original_text), "r", encoding="utf8") as origin_f:
        origin_txt = origin_f.read()
    with io.open("{}.txt".format(canidate_text), "r", encoding="utf8") as canid_f:
        canid_txt = canid_f.read()
    #print(origin_txt)
    #print(canid_txt)
    origin_word = word_tok(origin_txt, engine="newmm")
    canid_word = word_tok(canid_txt, engine="newmm")
    canids_word = text_recorrection.ae_to_air_s1(canid_word)
    print(f"original : {origin_word}")
    print(f"canidate : {canids_word}")
text_diff("page7","sample")