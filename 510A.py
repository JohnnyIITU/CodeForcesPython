n,m = map(int, input().split())
res = []
left = True
for i in range(n) :
    snake = ""
    if (i % int(2) == int(0)) : 
        for j in range(m) :
            snake+="#"
    else :
        if(not left) :
            snake += "#"
        for j in range(m-int(1)) :
            snake+="."
        if(left) :
            snake += "#"
        left = not left
    res.append(snake)
print(*res, sep="\n")
