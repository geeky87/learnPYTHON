#######################################################################################################

#Set Data Types
#Sets
basket = ('Kiran','swathi','acharya')
print(basket)

# Frozen Sets
bucket =frozenset ('Kiran acharya')
print(bucket)
cities = frozenset(["Frankfurt", "Basel","Freiburg"])
print(cities)


#######################################################################################################
#List Data Type
list = ['kiran','Acharya','swathi','Prabhu']
print(list)
print(type(list))

#######################################################################################################
#Dictionary Data Type
my_dic = {"name":"acharya","age":10}
print(my_dic)
print(my_dic['name'])
print(my_dic.keys())

#######################################################################################################
#Tuple Data Type
tuple = (123,'hello')
print(tuple)

from collections import Counter
from sortedcontainers import sortedlist

c = Counter("Hello this is my first Counter")

print(c)
print(sorted(c))

print(c.most_common(1))

a = [1, 3, 1, 4, 2, 3, 5, 4]
k = sortedlist[a]
print(k)
