
import re

d_to_l = {
    '1' : 'р',
    '2' : 'д',
    '3' : 'т',
    '4' : 'ч',
    '5' : 'п',
    '6' : 'ш',
    '7' : 'с',
    '8' : 'в',
    '9' : 'к',
    '0' : 'л',
}

VOWELS = r'[аиеёоуыэюяьъ]'
VOWELS_ = r'[аиеёоуыэюяьъ]*'

words = open("russian_nouns.txt", "r", encoding="utf-8")
words = words.read()

def number_to_word(number: str) -> str:
    pat = ''
    for d in number:
        pat += d_to_l[d]
    pat = r'\s'+VOWELS_  + VOWELS_.join(pat) +VOWELS_ + r'\s'
    print(pat)
    return [re.sub(r'\n','',s) for s in re.findall(pat,words)]
    
print(number_to_word('1963'))