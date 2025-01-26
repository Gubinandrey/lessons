n2=[]
while True:
    n1=input()
    if n1=='добавить':
        print('введите фамилию')
        n4=input()
        n2.append(n4)
    if n1=='количество':
        print(len(n2))
    if n1=='текущий':
        print(n2[0])
    if n1=='следующий':           
       n2=n2[1: ]
    if n1=='найти':
        print('введите фамилию')
        n3=input()
        if n3 in n2:
            print(n2.index(n3))
        if n3 not in n2:
            print('нету') 
    if n1=='стоп':
        break
print(n2)