numbers = list(map(int, input().split(" ")))
price = numbers[0]
summa = numbers[1]
count = numbers[2]
coeff = int(count)
for i in range(0,count) :
    coeff += i
result = int(coeff*price-summa)
if(result >= 0) :
    print(result)
else :
    print('0')
