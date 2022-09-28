dic = {}
palabra = input('please enter words in spanish with its english translation separated by : and separating translations with ,')
lista = palabra.split(',')
for translation in lista:
    values= translation.split(':')
    key_english = values[0]
    key_spanish = values[1]
    dic[key_english]= key_spanish

input_totranslate= input()