divisa ={'euro': '€' , 'dollar': '$', 'yen':'¥'}
answer= input('please enter a currency name ')
print(divisa.get(answer.lower(), 'currency not found'))