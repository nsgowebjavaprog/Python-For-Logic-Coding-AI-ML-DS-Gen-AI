# filling in the blanks with random words

# e.g:  Today i wend to a _____ zoo.  [fill: adjective_1]

print("Welcome to Mad Libs Game!")
adj = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb (past tense): ")
place = input("Enter a place: ")

story = f"Today I went to a {adj} zoo in {place}. I saw a {noun} that {verb} loudly!"
print("\nHere is your story:")
print(story)