people = [
  "Mal",
  "Zoe",
  "Wash",
  "Jayne",
  "Kaylee"
]

#read list

print(people[2])
print(people[0])
print(people[-1])

#accessing 

index = 0
groceries = [
  "lettuce",
  "beef",
  "coffee",
  "brie cheese",
  "milk",
  "bread",
  "flour",
  "avocado",
  "carrots"
]

print(groceries[0])
print(groceries[index])
print(groceries.index("coffee"))
lastItem = groceries[-1]
print(lastItem)

#slice a list, Taking a slice doesn't change the original list
print(groceries[0:3])
print(groceries[4:8])
print(groceries[5:])

print(groceries[:3])
print(groceries[4:8])
print(groceries[-3:])

