journey = """Just a small tone girl
Leaving in a lonely whirl
She took the midnight tray going anywhere
Just a seedy boy
Bored and raised in South Detroit or something
He took the midnight tray going anywhere"""

# journey = journey.replace(
#   "tone", "town"
# )
# journey = journey.replace(
#   "tray", "train"
# )
# journey = journey.replace(
#   "whirl", "world"
# )

journey = (journey
.replace("tone", "town")
.replace("Leaving", "Living")
.replace("tray", "train")
.replace("seedy", "city")
.replace("Bored", "bored")
.replace(" or something", "")
)

print(journey)