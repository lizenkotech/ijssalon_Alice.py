'''fruit = [ "druif", "kesinaasappel","perzik","kiwi", "druif",]

print("Voor remove()", fruit)
fruit.remove("druif")
print("Na remove()", fruit)
---------------------------------------------------------------------------------
mijn_dictionary = {
    "product" : "softijs",
    "aantal" : 101,
    "smaak" : "vanille"
}
print (mijn_dictionary["aantal"])
keys = mijn_dictionary.keys()
print (keys)

values = mijn_dictionary.values()

mijn_dictionary = {
    "product" : "softijs",
    "aantal" : 101,
    "smaak" : "vanille"
}
keys = mijn_dictionary.keys()
Values = mijn_dictionary.values()
print ("keys", keys)
print("Values", Values)

print(mijn_dictionary)

for item in mijn_dictionary:
    print(item)
------------------------------------------------------------------------------

mijn_dictionary = {
    "Voornaam" : "Harry",
    "Geboortedatum" : "31-maart-1939",
    "registratienummer" : "AA18891"
}
mijn_dictionary["Achternaam"] = "de Vries"
print()
for K, V in mijn_dictionary.items():
    print (K, V)

mijn_dictionary.pop("Geboortedatum")
print()
for K, V in mijn_dictionary.items():
    print (K, V)
mijn_dictionary.clear()
print()
for K, V in mijn_dictionary.items():
    print (K, V)
del mijn_dictionary
'''

mijn_dictionary = {
    "product" : "softijs",
    "aantal" : 101,
    "smaak" : "vanille"
}
mijn_dictionary["aantal"] = 150
mijn_dictionary.update({"aantal":250})
print(mijn_dictionary["aantal"])