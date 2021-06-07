n = int(input())
numbers = []
for i in range(n) :
    numbers.append(int(input()))

count = []
for number in numbers :
    temp = []
    print(len(str(number)) - str(number).count('0'))
    if(number % int(10) != int(0)) :
        temp.append(number % int(10))
    number=int(number / int(10))
    if(number % int(10) != int(0)) :
        temp.append(number % int(10) * int(10))
    number=int(number / int(10))
    if(number % int(10) != int(0)) :
        temp.append(number % int(10) * int(100))
    number=int(number / int(10))
    if(number % int(10) != int(0)) :
        temp.append(number % int(10) * int(1000))
    number=int(number / int(10))
    if(number % int(10) != int(0)) :
        temp.append(number % int(10) * int(10000))
        
    print(*temp, sep=" ")
