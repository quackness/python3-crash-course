foosballers = [
  "Mia",
  "Retta",
  "Augustine",
  "Jin",
  "Waylon",
  "Alphonso",
  "Sage",
  "Hubert",
  "Raymon",
  "Rebecca",
  "Monty",
  "Glen",
  "Christi",
  "Patrice",
  "Craig",
  "Dexter",
  "Wally",
  "Ian",
  "Pat"
]

#1) Get the median player
print(len(foosballers)//2)
print(foosballers[9])
#2) Get the five players in 
# the middle of the league
print(foosballers[7:12])
# 3) Add a fake player, called "Average Player," 
# to the exact middle of the list
foosballers.insert(9, "Average player")
print(foosballers)
#4 Find "Average Player," and change 
#their name to uppercase
foosballers[9] = "AVERAGE PLAYER"
print(foosballers)
#5 Add five more players to the bottom 
#of the list
addFoosballers = ["Jorge", "Rita", "Bruce", "Kate", "Tom"]
foosballers = foosballers + addFoosballers
print(foosballers)
#6 "AVERAGE PLAYER" is no longer in the middle! Find a way to fix this. 
print(len(foosballers)//2) #12
print(foosballers.index("AVERAGE PLAYER"))
del foosballers[9]
print(foosballers)
print(len(foosballers)//2) #12
foosballers.insert(12, "AVERAGE PLAYER")
print(foosballers)
# 7) Five more players show up, but they are 
# ranked. Insert them at the appropriate location:
# - Lacy is one spot ahead of Hubert
# - Omar is one spot behind Rebecca
# - Otto is 8th best in the league
# - Chauncey is 10 spots from the bottom 
# of the league
foosballers.insert(7, "Lacy")
foosballers.insert(11, "Omar")
foosballers.insert(7, "Otto")
foosballers.insert(-9, "Chauncey")
print(foosballers[-10])
print(foosballers)


