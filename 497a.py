a = int(input())
b = int(input())
c = int(input())
if(a == int('1')) :
    if(b == int('1')) :
        if(c == int('1')) :
            print(a+b+c)
        else:
            print((a+b)*c)
    elif(c == int('1')) :
        print(a+b+c)
    else :
        print((a+b)*c)
else :
    if(b == int('1')) :
        if(c == int('1')) :
            print(a*(b+c))
        else :
            if(a > c) :
                print(a*(b+c))
            else :
                print((a+b)*c)
    else :
        if(c == int('1')) :
            print(a*(b+1))
        else :
            print(a*b*c)
