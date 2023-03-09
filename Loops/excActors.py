actors = [
  "Nathan",
  "Gina",
  "Alan",
  "Morena",
  "Adam",
  "Jewel",
  "Sean",
  "Summer",
  "Ron"
]

roles = [
  "Captain",
  "Zoe",
  "Hoban",
  "Inara",
  "Jayne",
  "Kaylee",
  "Dr. Simon",
  "River",
  "Derrial"
]

#solution 1
for index in range(0, len(actors)):
  print(actors[index] + " as " + roles[index])

#solution 2: "Enumerate" is a function that gives us access to two variables
# on each iteration: The list item itself, and that item's index.
for index, actor in enumerate(actors):
  print(actor + " as " + roles[index])



