list_var = ['c','b',123,'a']
list_var.pop() #listenin sonundaki elemanı siler
print(list_var)
print(list_var[0])
print(list_var[1])
print(list_var[2])

print(len(list_var)) #len, listenin büyüklüğünü söyler
print(len("random string"))

list_var.pop(0) #0 index'indeki elemanı atar

dict = {} #bir veri tipi olan dictionary'nin tanımı
dict["abc"] = "new string"
#abc key'ine "new string" value'su atandı
#python2'de key değeri integer olabilir ama python3'te string
#value değeri bir list olabilir
dict["a list"] = [1,2,3]
#value değeri bir dict de olabilir

#başka bir veri tipi olan tuple'ı inceleyelim
tup = () #böyle tanımlanır
tup = ( ("another", "another"), ("more", "more"))
print(tup[0]) #'another', 'another') yazdıracaktır
print(tup[0][0])#another yazdıracaktır

tup += (("elemean", "ekleme")) #tuple'a böyle eleman eklenebilir

#hadi list içinde list yapalım ve ne kadar uzun olduğunu görelim
the_list = []
abc = ["another", "another"]
the_list.append(abc)
print(the_list)
# böyle uzun sürdü ama tuple veya dict'te oluşturmak çok daha kolaydı

# for loop
bag = [1,2,3,4,5,6]
for item in bag:
	print item
	if item == 5:
		print("yeah !")

# while loop
i = 10
while i < 11:
	print("yup")
	i += 1

# boolean değerleri 
True 
False

