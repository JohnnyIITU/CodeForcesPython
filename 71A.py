count = int(input())
words = []
for i in range(0, count) :
    fullString = input()
    if(len(fullString) > 10) : 
        length = len(fullString) - 2
        words.append(fullString[0:1] + str(length) + fullString[len(fullString)-1:len(fullString)])
    else :
        words.append(fullString)
for i in (range(0, count)) :
    print(words[i])
    
