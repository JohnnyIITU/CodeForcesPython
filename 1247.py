numbers = list(map(int, input().split(" ")))
a = numbers[0]
b = numbers[1]

if(a == b) :
    print("%d00 %d01" % (a, b))
elif(a == b-int(1)) :
    print("%d99 %d00" % (a, b))
elif(a == int('9') and b == int('1')) :
    print("99 100")
else :
    print(-1)
