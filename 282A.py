n = int(input())
sum = int('0')
for i in range(0 , n) :
    operation = input()
    if(operation == "++X" or operation == "X++") :
        sum += 1
    else :
        sum -= 1
print(sum)
