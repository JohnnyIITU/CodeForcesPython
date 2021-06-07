count = int(input())
numbers = list(map(int, input().split(" ")))
numbers.sort(reverse = True)
sum = sum(numbers)
sumTwin = int('0')
cnt = int('0')
for i in numbers :
    if(sumTwin > sum/2) :
        break
    else :
        cnt+=1
        sumTwin += i
print (cnt)
