import random
n1=random.randint(1,50)
for asd in range(4):
    n2=int(input())
    if n2==n1:
        print('you won')
    if n2<n1:
        print('too little')
    if n2>n1:
        print('too big')
print(n1)