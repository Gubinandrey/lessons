import os


n1=os.listdir('C:/Users/andre/программирование пайтон/lessons_2025/animation2/temp')
for asd in n1:
    asd1='C:/Users/andre/программирование пайтон/lessons_2025/animation2/temp/'+asd
    f=open(asd1, 'r')
    data=f.read()
    f.close()
    if len(data)==0:
        os.remove(asd1)
        print('файл', asd, 'удалён')