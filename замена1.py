word1=input()
word1.replace('.', '')#удалятся все точки
simbols=['!','.','?', ':', ',']
for asd in simbols:
    word1=word1.replace(asd, '')
print(word1)