year = int(input())
for i in range(year+1, 9013) :
    if(len(list(set(str(i)))) == int('4')) :
        print(i)
        break
