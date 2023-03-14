# This time, the user is setting their own password, and we want 
# to make sure that a password is secure enough. Ask the user to 
# input a password, and then input it again to confirm it. 
# The application should verify that:
# a) Both passwords match
# b) The password is at least 8 characters long
# If both checks pass, tell the user that they've successfully 
# set the password. If they don't, tell the user what the problem 
# was: Whether the passwords didn't match, or whether it was too short.
# Note: As alluded to before, you'll need to use the `==` operator 
# here instead of `is`. This is true whenever you're comparing user 
# input to another value, for a kind of esoteric computer science reason. 

password = input("Password:")
reConirmedpassword = input("Re-confirm your password:")

if password != reConirmedpassword:
  print ("Passwords must be the same ")
elif len(password) < 8:
  print("Password is too short")
else:
  print("Your password is okay!")


