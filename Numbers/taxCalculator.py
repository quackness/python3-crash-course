# Your task is to build an app that calculates how much tax someones owes.
#     Ask the user to input a subtotal. input()
#     Calculate the tax owed using some (hard-coded) tax rate. This can be whatever you want, like 0.25.
#     Print out a message with the amount of tax owed. print()
#     Print out another message with the total owed including tax. print()



subtotal = float(input("Insert subtotal in CAD dollars:"))
#input by default generates string, I had to turn it in to the float to allow multiplication 
print(type(subtotal)) 
taxOwed = 0.15 * subtotal
print("Tax owed", taxOwed)
totalOwed = taxOwed + subtotal
print("Your total is", totalOwed)




