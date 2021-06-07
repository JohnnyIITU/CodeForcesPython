line = list(map(int, input().split(" ")))
n = line[0]
m = line[1]
numbers = list(map(int, input().split(" ")))
numbers.sort()
first = True
max = int('1000000')
for i in range(0, m-n+1) :
    if(first) :
        first = False
        max = numbers[i+n-1] - numbers[i]
    else :
        if(max > numbers[i+n-1] - numbers[i]) :
            max = numbers[i+n-1] - numbers[i]
print(max)
