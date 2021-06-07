def checkPrime(num) :
    if num > 1:
        if(num == int(4)) :
            return True
        for i in range(2, num//2): 
            if (num % i) == 0: 
                return True
                break
        else: 
           return False
    else: 
        return True
num = int(input())
for i in range(3, num) :
    if(checkPrime(i)) :
        if(checkPrime(num-i)) :
            print("%d %d" %(i, num-i))
            break
