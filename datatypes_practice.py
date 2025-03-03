#int
age = 11
#float
gpa = 3.5
#string
name = "Jagdish"
#list
name_list = ["Raju", "Hari", "Ram"]
for name in name_list:
    print(name)

name_list.append("Jagdish")

#tuple -same like list but immutable
pin_codes = (123,443,542,112)
for pin in pin_codes:
    print(pin)
#can't append

ranges = range(11)
for i in ranges:
    print(i)
    

#set - UNIQUE - Mutable

unique_nums = {12,32,12,56}
unique_nums.add(32)
print(unique_nums)

#frozen set - mutable
unique_const_nums = frozenset({12,43,23,123,22,43})
#can't add

#our fav - dictionary

person = {"name":"MayBe Jagdish", "age":11}
print(person.get("Hari")) #no error
#print(person["haru"]) #error

print(person.get("name"))
print(person["age"])