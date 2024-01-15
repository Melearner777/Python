# Define a dictionary named phone
phone = {
    "Jishan": 777778,
    "Shreyansh": 99645,
    "Vipin": 46765,
    "Archit": 46491,
}

# Printing the dictionary
print(phone)

# Accessing the phone number associated with the key "preetam"
print(phone["Jishan"])
print(phone["Vipin"])
print(phone.keys())

#uppdating dictionary
phone["Jishan"] = 978685
print(phone)
phone["Devanshu"]=59646
print(phone)


phone.popitem() #this removes last item of the dictionary
print(phone)

phone.clear() # this deleate all the elements
print(phone)

#printing element of dict
for x,y in phone.items():
    print(x,y)