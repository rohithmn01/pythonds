person={'name':'rohith', 'age':30, 'gender':'male'}
for i in person.items():
    print(i)
print("#################")

for key,value in person.items():
    print(f"{key}, {value}")
print("#################")

for i in person:
    print(i)
print("#################")

for v in person.values():
    print(v)
print("#################")


#Dictionary comprehension
# {key,value for (key,value) in dict.items() if condition}