# The developer (you) will prepare a number of addition questions, and then ask the player 
# (also you, probably) to answer them. The game tells the player if their answer was correct
#  or incorrect, and then at the end, tells them their total score.

# Create a list: This list contains questions. A question is itself a list, which contains 
# two numbers. Iterate through each question and ask the user for input: For example, 
# if the two numbers of the question are 2 and 3, the input prompt should read something like 
# "What's the answer to 2 + 3?"
# Compare the user input to the actual result of adding the 2 numbers together. If they are 
# the same (i.e. the user answered correctly), print a success message and add 1 point to 
# their score. If they are different, print out a not-as-much-success message (and don't 
# change their score). When they have answered all of the questions (correctly or incorrectly), 
# print out their score.


questions = [
  [1,2],
  [2,2],
  [3,3]
]

score = 0 
#in the code below I had one element as c
# for a, b,c in questions:
#   response = int(input("What's the value of " + str(a) + "+" + str(b) +"?"))
#   if response == c:
#    print("Correct")
#    score += 1
#   else:
#     print("Incorrect")
# print(score)

score = 0
for a, b in questions:
  response = int(input("What's the value of " + str(a) + "+" + str(b) +"?"))
  answer = a + b
  print("Calculated", answer)
  if (response == answer):
    print("Correct")
    score += 1
  else:
    print("Icorrect")
print("Your final score is: " + str(score))

