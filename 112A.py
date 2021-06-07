a = input().lower()
b = input().lower()
result = int('0')
for i in range(0 , len(a)) :
    if(result == int('0')) :
        if(a[i] > b[i]) :
            result = int(1)
        elif(a[i] < b[i]) :
            result = int(-1)
        else :
            result = int(0)
print(result)
