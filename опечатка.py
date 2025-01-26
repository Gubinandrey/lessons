words=['магазин', 'яблоко', 'молоко', 'молочный']
word=input()
cmax=0
wordmax=0
for asd in words:
    n3=len(asd)
    c=0
    for a,b in  zip(word, asd):
        if a==b:
            c=c+1
    if cmax<c:
        cmax=c
        wordmax=asd
print(wordmax)