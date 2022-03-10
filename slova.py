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

l_to_d = {
    'р' : '1',
    'д' : '2',
    'т' : '3',
    'ч' : '4',
    'п' : '5',
    'ш' : '6',
    'с' : '7',
    'в' : '8',
    'к' : '9',
    'л' : '0',
    'б' : '5',
    'ж' : '6',
    'з' : '7',
    'ф' : '8',
    'г' : '9',
    'н' : '0',
    
}

def remove_vowels(s):
    return re.sub(r"а|и|е|ё|о|у|ы|э|ю|я|ь|ъ|\n", '', s)

def word_to_number(word):
    number = ''
    for c in remove_vowels(word):
        number += l_to_d[c]
    return number

words = open("russian_nouns.txt", "r", encoding="utf-8")
words = words.readlines()

word_to_number_d = {}
for w in words:
    if re.findall(r"й|ц|х|щ|м|-", w):
        continue
    word_to_number_d[w] = word_to_number(w)

number_to_word = {v:k for k,v in word_to_number_d.items()}

print(number_to_word['335'])