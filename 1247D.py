line = list(map(int, input().split(" ")))
n= line[0]
k= line[1]
count=int(0)
numbers = list(map(int, input().split(" ")))
for i in range(0,n) :
    for j in range(i+1,n) :
        sum = numbers[i]*numbers[j]
        print((sum ** (int(1)/k).is_integer, int))
        if((sum ** (int(1)/k).is_integer())) :
            count+=1
        else :
            count +=1
print(count)
