n1=[]
n2=[]
for asd in range(5):
    n3=input()
    n1.append(n3)
for asd in range(5):
    n4=input()
    n2.append(n4)
n5=[]
for asd in n1:
    if asd in n2:
        n5.append(asd)
print(n5)