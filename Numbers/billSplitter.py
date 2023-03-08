# Your task is to build an app that takes a bill total, tip amount, 
# and number of people as input; and outputs how much each person should pay. 
#     Ask for a total dollar amount
#     Ask for the percentage tip
#     Ask for the number of people splitting the bill
#     Use those numbers to calculate the amount that each person owes, 
#printing it out to the terminal, along with the overall total

billTotal = float(input("Total bill is:"))
print(billTotal)
percTip = float(input("Tip %:"))
print(percTip)
tipPercentage = percTip / 100
tipDollars = tipPercentage * billTotal
billAfterTip = tipDollars + billTotal
sumPeople = int(input("Amount of people splitting the bill:"))
print(type(sumPeople)) 

final = billAfterTip/sumPeople
print(final)
