n1={}
while True:
    n2=input()
    if n2=='стоп':
        break
    if n2=='добавить':
        print("введите слово")
        n3=input()
        print('напишите определение этого слова')
        n4=input()
        if n3 in n1:
            print('вы уже доббавили его в справочник')
        n1[n3]=n4
    if n2=='найти':
        print("введите слово")
        n5=input()
        if n5 in n1:
            print(n1[n5])
        else:
            print('его нету')