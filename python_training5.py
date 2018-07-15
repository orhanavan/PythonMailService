# This program can seperate numbers and strings
items = ["Mic", "Phone", 323.12, 3123.123, "Justin", "Bag", "Cliff Bars", 134]

def parse_lists(some_list):
	str_list_items = []
	num_list_items = []
	for i in items:
		if isinstance(i, float) or isinstance(i, int):
			num_list_items.append(i)
		elif isinstance(i, str):
			str_list_items.append(i)
		else:
			pass
	return str_list_items, num_list_items

str_items, num_items = parse_lists(items)
print(str_items)
print(num_items)