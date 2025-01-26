n4=[]
n2=[]
while True:
    n1=int(input())
    if n1!=0:
        n2.append(n1)
    if n1==0:
        print('введите ещё 1 число')
        n3=int(input())
        print(n2[-n3:])
        break