def sumRange(L,a,b):                                                                                                                                                                                                
    sum = 0                                                                                                                                                                                                         
    for i in range(a,b+1,1):                                                                                                                                                                                        
        sum += int(L[i])                                                                                                                                                                                                  
    return sum  

players = input()
isDanger = 'NO'
if(len(players) > 7 ) : 
    for i in range(0, len(players)-6) :
        if((sumRange(players, i, i+6) % 7) == int('0')) :
            isDanger = 'YES'
            break
print(isDanger)
