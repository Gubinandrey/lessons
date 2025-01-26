spam=['розыгрыш', 'приз', 'распродажа']
n1=input()
woor=n1.split()
is_spam=False
for asd in woor:
    if asd in spam:
        is_spam=True
        break
if is_spam==True:
    print('спам')
if is_spam!=True:
    print('не спам')