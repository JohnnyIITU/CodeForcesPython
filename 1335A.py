n = int(input())
numbers = []
result = []
for i in range(n) :
    numbers.append(int(input()))
for number in numbers :
    if(number % int(2) == int(0)) :
        result.append(int(number/int(2)-int(1)))
    else :
        result.append(int(number/int(2)))
print(*result, sep = '\n')
    
