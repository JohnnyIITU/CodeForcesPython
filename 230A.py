s,n = map(int,input().split())
dragons = []
lost = False
for i in range(n) :
    dragons.append(list(map(int, input().split())))
dragons.sort(key=lambda x: x[0])
for i in dragons :
    if(i[0] < s) :
        s += i[1]
    else :
        lost = True
if(lost) :
    print('NO')
else :
    print('YES')
