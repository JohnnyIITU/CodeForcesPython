count = int(input())
accepted = int('0')
for i in range(0,count) :
    summary = int('0')
    numbers = list(map(int,input().split(" ")))
    for j in numbers :
        summary += int(j)
    if(summary > 1) :
        accepted += 1
print(accepted)
