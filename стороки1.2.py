bad_words=['дурак','идиот']
n1=input()
words=n1.split()
for asd in words:
    if asd in bad_words:
        print('***', end=' ')
    else:
        print(asd, end=' ')