vector1= [1 , 2 , 3]
vector= [ -1 , 0 , 2]
sum= 0

for index in range(len(vector1)):
    sum+= (vector1[index]*vector[index])

print(sum)