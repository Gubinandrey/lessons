n1=input()
n2=input()
n3=input()
for asd in n1.split():
    if asd==n2:
        print(n3, end=' ')
    if asd==n3:
        print(n2, end=' ')
    if asd!=n2 and asd !=n3:
        print(asd, end=' ')