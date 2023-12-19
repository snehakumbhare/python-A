#Ways to sort list of dictionaries by values in Python – Using itemgetter

# Python code demonstrate the working of sorted()
# and itemgetter
 
# importing "operator" for implementing itemgetter
from operator import itemgetter
 
# Initializing list of dictionaries
list = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
 
# using sorted and itemgetter to print list sorted by age
print("The list printed sorting by age: ")
print(sorted(list, key=itemgetter('age')))
 
print("\r")
 
# using sorted and itemgetter to print
# list sorted by both age and name
# notice that "Manjeet" now comes before "Nandini"
print("The list printed sorting by age and name: ")
print(sorted(list, key=itemgetter('age', 'name')))
 
print("\r")
 
# using sorted and itemgetter to print list
# sorted by age in descending order
print("The list printed sorting by age in descending order: ")
print(sorted(list, key=itemgetter('age'), reverse=True))
