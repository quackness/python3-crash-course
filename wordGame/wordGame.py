    # Ask the user for a word (Get user input)
    # Quietly (i.e. without the user seeing) replace 
    #a section of the story with the user's word
    # Repeat until all the blanks have been filled
    # Print out the final string to the user

#tools
    # Multi-line strings
    # User input with `input('...')`
    # The `.replace('phrase', 'new phrase')` method
    # The humble `print('...')` statement
#1st solution
# place = '____'
# item = '____'
# providePlce = input("Provide place:")
# provideItem = input("Provide item:")

# place = place.replace(place, providePlce)
# item = item.replace(item, provideItem)
# string = "Just as I arrived at " + place +", I realized I had forgotten my " + item +"."
# print(string)

#2nd solution
proseString = """
Hi mom,

Just writing to tell you that I've quit my job as a OCCUPATION and I'm moving to COUNTRY. The truth is, I've always been passionate about PLURAL_NOUN, and COUNTRY is the best place in the world to build a career around them. I'll need to start small-- At first, all I'll be allowed to do is to VERB near them, but when people see how ADJECTIVE I can be, I'm sure to rise to the top.

Don't worry about me, and tell dad to take good care of my PERSONAL_ITEM. I'll be sure to call every HOLIDAY.

Love,

NAME
"""


userInput = input("Please type anything:")
newProseString = proseString.replace("HOLIDAY", userInput)
print(newProseString)



