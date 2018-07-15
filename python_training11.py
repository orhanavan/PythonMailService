def dumb_sentence(name='bucky', action='ate', item='tuna'):
	print(name, action, item)

dumb_sentence()
dumb_sentence('Sally', 'farts', 'gently') # positional argument
dumb_sentence(item='awesome')
dumb_sentence(item='awesome', action='is')# keyword argument


def key(a,b,c):
	first = "a is {}".format(a)
	second = "b is {}".format(b)
	third = "c is {}".format(c)
	return first, second, third

print(key(1,2,3))    # hepsi positional argument - sorun yok
print(key(1,2,c=5))  # sondaki keyword argument - sorun yok
print(key(a=1,b=2,5))# positional argument sonda olamaz !
