line = list(map(int, input().split(" ")))
n = line[0]
t = line[1]
line = input()
tempLine = line
if(n < 2) :
    print(line)
else : 
    for i in range(0, t) :
        if(line[len(line)-2]+line[len(line)-1] == "BG") :
            tempLine = tempLine[0:n-2] + "GB"
        if(line[0]+line[1]=="BG") :
            tempLine = "GB"+tempLine[2:]
        for j in range(1 , n-2) :
            if(line[j]+line[j+1] == "BG") :
                tempLine = tempLine[0:j] + "GB" + tempLine[j+2:]
        line = tempLine
    print(line)
