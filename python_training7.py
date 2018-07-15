import datetime

default_names = ["Justin", "John", "Emilee", "Jim", "Ron"]
default_prices = [123.456, 95.95, 100.000, 150, 43.350]
unformatted_message = '''Hi {name}!

Thank you for the purchase on {date}.
We hope you are exicted about using it. Just as a
reminder the purchase total was ${total}.
Have a great one!

Sicrely
'''

def make_messages(names, amounts):
	message = []
	i = 0
	some_date = '{today.month}/{today.day}/{today.year}'.format(today=datetime.date.today())
	for name in names:
		new_amount = "%.2f" %(amounts[i])
		new_msg = unformatted_message.format(
				name = name,
				date = some_date,
				total = new_amount)
		i += 1
		print(new_msg)

make_messages(default_names, default_prices)