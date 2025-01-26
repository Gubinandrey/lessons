alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text=input()
for asd in text:
    if asd in alphabet:
        idx=alphabet.index(asd)
        if asd=='а':
            next='я'
        else:
           next=alphabet[idx-1] 
        print(next, end='')
    else:
        print(asd, end='')