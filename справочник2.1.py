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
        print("введите предложение")
        n5=input()
        for asd in n5.split():
            if asd in n1:
                print(n1[asd])