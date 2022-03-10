import re

d_to_l = {
    '1' : r'[рй]',
    '2' : r'[дх]',
    '3' : r'[тм]',
    '4' : r'[чц]',
    '5' : r'[пб]',
    '6' : r'[шжщ]',
    '7' : r'[сз]',
    '8' : r'[вф]',
    '9' : r'[кг]',
    '0' : r'[лн]',
}

VOWELS = r'[аиеёоуыэюяьъ]'
VOWELS_ = r'[аиеёоуыэюяьъ]*'

words = open("russian_nouns.txt", "r", encoding="utf-8")
words = words.read()

def number_to_word(number: str) -> str:
    pat = []
    for d in number:
        pat.append(d_to_l[d])
    pat = r'\s'+VOWELS_  + VOWELS_.join(pat) +VOWELS_ + r'\s'
    print(pat)
    return [re.sub(r'\n','',s) for s in re.findall(pat,words)]

print(number_to_word('1989'))