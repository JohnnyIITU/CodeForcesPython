count = int(input())
numbers = []
sum = []
ok = int('1')
for i in range(0,count) :
    numbers.append(list(map(int, input().split(" "))))
for j in range(0,3) :
    sum.append(int('0'))
    for i in range(0,count) :
        sum[j] += numbers[i][j]
    if(sum[j] != int('0')) : 
        ok = int('0')
if(ok == int('1')) :
    print ("YES")
else :
    print ("NO")
