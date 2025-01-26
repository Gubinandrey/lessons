alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text=input()
for asd in text:
    if asd in alphabet:
        idx=alphabet.index(asd)
        if asd=='я':
            next='а'
        else:
           next=alphabet[idx+1] 
        print(next, end='')
    else:
        print(asd, end='')