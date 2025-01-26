n1=[]
while True:
    n2=input()
    if n2!='конец':
        n1.append(n2)
    if n2=='конец':
        print('введите ещё одну страну')
        n3=input()
        if n3 in n1:
            print('была')
            break
        if n3 not in n1:
            print('не была')
            break
        print(n2)