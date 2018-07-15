# string substitution
str_a = "This is a {var} string"
print(str_a)
str_b = str_a.format(var = "really really cool")
print(str_b)

# multiple string substitution
str_d = "These arguments are :{0} {1} {2}".format("one","two","three")
print(str_d)

# string type casting 
str_c = str(123)

# another string substition
print("Hi there %s !" %("Justin"))

# date substitution
import datetime
today = datetime.date.today()
print(today)

now = datetime.datetime.now()
print(now)
