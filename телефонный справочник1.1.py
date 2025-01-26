n1={}
while True:
    n2=input()
    if n2=='стоп':
        break
    if n2=='добавить':
        print("введите ФИ")
        n3=input()
        if n3 in n1:
            print('вы уже доббавили его в справочник')
        else:
            print('введите номер телефона')
            n4=input()
            n1[n3]=n4
    if n2=='найти':
        print("введите ФИ")
        n3=input()
        if n3 in n1:
            print(n1[n3])
        else:
            print('его нету')
    if n2=='редактировать':
        print('введите ФИ')
        n9=input()
        if n3 in n1:
            print('что вы хотите редактировать?')
            n3=input()
            if n3=='имя':
                print("введите новое имя")
                n6=input()
                телефон=n1[n9]
                del n1[n9]
                n1[n6]=телефон
            if n3=='телефон':
                print("введите новый телефон")
                n7=input()
                n1[n9]=n7