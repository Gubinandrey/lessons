n1=[]
while True:
    n2=input()
    if n2!='стоп':
        n1.append(n2)
    if n2=='стоп':
        break
while True:
    n3=input()
    if n3=='add':
        n4=input()
        n1.append(n4)
    if n3=='next':
        n1=n1[1:]
    if n3=='stop':
        print(n1)
        break