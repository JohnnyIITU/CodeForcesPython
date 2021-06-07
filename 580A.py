count = int(input())
numbers = list(map(int, input().split(" ")))
temp = int('1')
max = int('1')
for i in range(0, count-1) :
    if(numbers[i] <= numbers[i+1]) :
        temp+=1
    else :
        temp=int('1')
    if(temp > max ):
        max = temp
print(max)
