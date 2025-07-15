# Ask the user to enter their name and store it in the variable 'name'
name = input("What is your name? ")  # 'input' collects user input and stores it

# Greet the user and ask how they are feeling
print("Hello", name, "how are you? (good/bad/mad)")

# Define a function for each mood
def bad():
    print("Sorry to hear that :(")

def good():
    print("Great! :D")

def mad():
    print("Why? :=O")

# This dictionary acts like a 'switch' to link moods to their corresponding functions
ans = {
    "bad": bad,
    "good": good,
    "mad": mad
}

# Ask the user to enter their mood
# '.lower()' converts the input to lowercase to avoid case sensitivity issues
mood = input("Enter your mood: ").lower()

# Try to get the corresponding function from the dictionary
response = ans.get(mood)

# Special case: if the mood is "mad", do something different
if mood == "mad":
    ands = input("(You can tell me more if you want) ")  # Let the user share more
    print("That's understandable.")

# If a valid function was found (e.g., 'good' or 'bad'), call it
elif response:
    response()

# If the mood wasn't recognized, show an error message
else:
    print("Sorry, I didn't understand that mood.")
