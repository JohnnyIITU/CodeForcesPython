a,b = list(map(int, input().split()))
houses = list(map(int, input().split()))
count = int(0)
current = int(1)
for i in houses :
    if(i > current) :
        count += (i - current)
    elif (i < current) :
        count += (i+a-current)
    current = i
print(count)
