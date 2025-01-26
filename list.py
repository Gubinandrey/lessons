n2=[]
while True:
    n1=int(input())
    if n1!=0:
        n2.append(n1)
    if n1==0:
        break
print(n2[-1])