dollars = int(input())
count = int(0)
nominals = ([int(100), int(20), int(10), int(5), int(1)])
for nominal in nominals :
    count += int(dollars/nominal)
    dollars = dollars%nominal
print(count)
