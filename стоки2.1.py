text=input()
print('напишите слово которое заменить')
word1=input()
print('напишите слово на которое нужно заменить')
newword=input()
for asd in text.split():
    if word1==asd:
        print(newword, end=' ')
    if word1!=asd:
        print(asd, end=' ')