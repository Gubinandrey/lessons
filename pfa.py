import utils

print('введите пароль')
n1=input()
n2=utils.check_password(n1)
if n2==True:
    print('correct')
else:
    print('incorrect')