#A dictoionary is a type of collection like a list
#A list is a collection of items in a sequence, but a dictionary is different.
#Dictionaries store data in key-value pairs
#Which means that you can retrive data quickly by using a unique key
#instead of retrieving it by index (position)

#Example
#Lists use brackets, dictionaries use braces

Olivia = {
    "name": "Olivia",
    "age": 15,
    "city": "St"
    "pets": 2,
    "height": 5.8



}
#Each key must be unique

#Retreiving values from a dictionary

print(Olivia["age"])

#.get allows you to retrive a value without erroring
#When the key does not exist
#The second perameter is what is given if value is not found
print(Olivia.get["height"])
print(Olivia.get("Weight, "fortnite"))
                
        #You can add to / modify values
        print(Olivia)

        #Remove entries
        Olivia.pop("pets")

        #Iterate through a dictionary using a for loop


#Dictionary functions
print(osowski.keys())   #Returns all keys
print(osowski,values())   #Returns all values
print(osowski.items()) #Returns all pairs



