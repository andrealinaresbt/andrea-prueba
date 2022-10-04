dic = {}
palabra = input('please enter words in spanish with its english translation separated by : and separating translations with ,')
lista = palabra.split(',')
for translation in lista:
    values= translation.split(':')
    key_english = values[0]
    key_spanish = values[1]
    dic[key_english]= key_spanish

input_totranslate = input('please enter a phrase to translate: ')
word_list = input_totranslate.split(' ')
word_results = ''

for word in word_list:
    word_results = ''
for word in word_list:
    word_results += dic.get(word,word)
    word_results += ""