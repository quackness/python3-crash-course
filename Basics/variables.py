#comments are added with ###
name = "Thomas"
print("Hello," + name + ", it's very nice to meet you.")

# taxRate, subtotal, tax and total atre all variables that contain numbers 
taxRate = 0.14
subtotal = 20
tax = subtotal * taxRate
total = subtotal + tax
print("Your total bill is:")
print(total)

#travelDestinations is a var that has a list
#city is a variable --Its value changes a few times
travelDestinations = ["Almaty", "Moscow", "Buenos Aires", "Manila"]
for city in travelDestinations:
  print(city + " seems like a cool place to go.")
