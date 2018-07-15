items = ["Mic", "Phone", "Annen", "Justin", "Trump"]
items.sort()
print(items)

# bir dizinin sıralanabilmesi için aynı tip değişkenlerden oluşması gerekmektedir

items = [3,7,1,9,2]
items.sort()
print(items)


words = ["JM","ED","Abc","AD","bb","aaa"]
words.sort() # büyük harfle başlayanları küçük harfle başlayanları ayrı ayrı sıraladı
print(words) 
words.sort(key=str.lower) # bu parametre ile büyük-küçük farketmeksizin sıralar
print(words)
words.sort(reverse=True) # sıralamayı tersine çevirir
print(words)

# sıralama için başka bir yöntem
str_items = ["AA","CCC", "def","ab","bb","De"]
print(str_items)
new_items = sorted(str_items, key=str.lower, reverse=True)
print(new_items) 