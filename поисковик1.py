internet=[]
while True:
    text=input()
    if text=='стоп':
        break
    else:
        internet.append(text)
while True:
    text2=input()
    for asd in internet:
        c=0
        for awsd in text2.split():
            if awsd in asd:
                c=c+1
                