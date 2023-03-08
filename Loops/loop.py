#loop template(pay attention to indentation)

# for item in collection:
  #do

clothing = [
  "Shirt",
  "Pants",
  "Socks"
]

for item in clothing:
  foldedItem = "Folded " + item
  print(foldedItem)
print("This line is not a part of the loop")