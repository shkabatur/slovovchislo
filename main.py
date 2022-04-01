import os
import re
import sys
import json


for k,v in os.environ.items():
    print(k,v)

def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    ) 

d_to_l = {
    '1' : r'[р]',
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

VOWELS_ = r'[аиеёоуыэюяьъй]*'

words = open(resource_path("russian_nouns.txt"), "r", encoding="utf-8")
words = words.read()

with open(resource_path("russian_nouns_with_definition.json"), "r", encoding="utf-8") as f:
    russian_nouns_with_definition = json.load(f)

def number_to_word(number: str) -> str:
    pat = []
    for d in number:
        pat.append(d_to_l[d])
    pat = r'\s'+VOWELS_  + VOWELS_.join(pat) +VOWELS_ + r'\s'
    #print(pat)
    return [re.sub(r'\n','',s) for s in re.findall(pat,words)]

def get_definition(word: str) -> str:
    return russian_nouns_with_definition[word]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(number_to_word(sys.argv[1]))
    else:
        print("Введите номер для перевода в слово")
