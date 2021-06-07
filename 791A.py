line = list(map(int, input().split(" ")))
a = line[0]
b = line[1]
cnt = int('0')
while(a <= b) : 
    b*=2
    a*=3
    cnt+=1
print(cnt)
