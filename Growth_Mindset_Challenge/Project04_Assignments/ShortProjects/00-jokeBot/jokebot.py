PROMPT = "What do you want? "

JOKE = """Here is a joke for you! 🤖  
Panaversity GPT - Sophia is heading out to the grocery store.  
A programmer tells her: get a liter of milk, and if they have eggs, get 12.  
Sophia returns with 13 liters of milk. The programmer asks why, and Sophia replies:  
"Because they had eggs!" 🥚😂"""

SORRY = "Sorry, I only tell jokes! 🙃"

def joke_bot():
    """Asks the user what they want & tells a joke if they ask for it."""
    user_input = input(PROMPT).strip()

    if user_input.lower() == "joke":
        print(JOKE)
    else:
        print(SORRY)


joke_bot()
