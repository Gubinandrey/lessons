print('Я чат бот VUO')
while True:
    n1=input()
    n2=n1.split()
    if 'привет' in n2:
        print('Здравствуйте')
    if ('времени' in n2) or ('время' in n2):
        import datetime
        print(datetime.datetime.now())