count = int(input())
presents = list(map(int, input().split(" ")))
res = []
for i in range(0,count) :
    for j in range(0, count) :
        if(presents[j] == i+1) :
            res.append(str(j+1))
print(' '.join(res))
