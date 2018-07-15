list_a = [1,2,3]
list_b = [1,2,3]
list_c = [4,5,6]

print(list_a == list_b) #True
print(list_a == list_c) #False
print(list_a != list_c) #True

obj_a = True
# print(!obj)  # değişkenin değilini böyle alamazsın, bu hata verir
print(not obj_a) # değişkenin değilini böyle alabilirsin

obj_b = False
print(not obj_a == obj_b) # a'nın değili b'ye eşitse
print(not obj_a is obj_b) # a'nın değili b'ye eşitse, aynısı


list_d = ["Justin", "Apple", "Food", 3131, 3.0, "Another", True]
for i in list_d:
	print(type(i))

# isinstance methodu
print(isinstance(3, int)) # 3 integer mıdır ?
