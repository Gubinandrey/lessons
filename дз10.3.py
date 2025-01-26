c=0
spam=['розыгрыш', 'приз', 'распродажа']
n1=input()
woor=n1.split()
for asd in woor:
    if asd in spam:
        c=c+1        
c=c/len(spam)*100
print(c)