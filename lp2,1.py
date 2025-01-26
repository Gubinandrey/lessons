n4=[]
n2=[]
while True:
    n1=input()
    if n1!='стоп':
        n2.append(n1)
    if n1=='стоп':
        print('введите ещё 3 животных')
        for awsd in range(3):     
            n3=input()
            if n3 in n2:
                n4.append(n3)
        break
print(n4)