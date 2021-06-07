n = int(input())
numbers = []
result = []
for i in range(n) :
    line = list(map(int, input().split(" ")))
    numbers.append(line)
for i in numbers :
    real = int(i[0]/i[1])
    res = i[1]*(real+int(1)) - i[0]
    if(i[1] == res) :
        result.append(0)
    else :
        result.append(res)
print(*result, sep = "\n") 
    
