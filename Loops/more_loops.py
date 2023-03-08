#making new data

instructionSteps = [
  "turn left",
  "go straight for two blocks",
  "turn right",
  "keep going until you see the dog statue",
  "turn right",
  "turn right again",
  "park right on the sidewalk"
]

#1
# instructions = "First, "

# for nextInstruction in instructionSteps:

#   instructions = instructions + nextInstruction + ", then "

# print(instructions + "you're there!")

#2
instructionStepsButScreamed = []
for nextInstruction in instructionSteps:
  
  upperInstruction = nextInstruction.upper()
  instructionStepsButScreamed.append(upperInstruction)
print(instructionStepsButScreamed)




