n1=[]
n2=[]
n3=[]
for asd in range(5):
    n4=int(input())
    n1.append(n4)
for asd in range(5):
    n5=int(input())
    n2.append(n5)
for asd in range(5):
    n6=int(input())
    n3.append(n6)
n7=[]
for asd in n2:
    if asd in n3 and asd in n1 and asd in n2:
        n7.append(asd)
print(n7)