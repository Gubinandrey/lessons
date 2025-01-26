n1={

}
n2=input()
n2=n2.lower()
n3='!*.,?'
for asd in n3:
    n2=n2.replace(asd, '')
for asd in n2.split():
    if asd in n1:
        pass
    else:
        n1[asd]=0
print(len(n1))