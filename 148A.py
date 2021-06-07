k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
cnt = int('0')
if(k == int('1') or l == int('1') or m == int('1') or n == int('1')) :
    print(d)
else :
    for i in range(1,d+1) :
        if(i%k == int('0') or i%l == int('0') or i%m == int('0') or i%n == int('0')) :
            cnt+=1
    print(cnt)
