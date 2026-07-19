print("===================================")
print("      Welcome to Nova AI 🤖")
print(" Type 'bye' or 'exit' to quit.")
print("===================================")
while True:
    user = input("\nYou: ").lower().strip()

    if user == "hello" or user == "hi":
        print("Nova AI: Hello! How can I help you?")

    elif user == "how are you":
        print("Nova AI: I'm fine. Thanks for asking!")

    elif user == "your name":
        print("Nova AI: My name is Nova AI.")

    elif user == "help":
        print("Nova AI: I can respond to greetings and basic questions.")

    elif user == "thanks":
        print("Nova AI: You're welcome!")

    elif user == "good morning":
        print("Nova AI: Good Morning! Have a great day.")

    elif user == "good night":
        print("Nova AI: Good Night! Take care.")
    
    elif user == "bye" or user == "exit":
        print("Nova AI: Goodbye! Have a nice day.")
        break

    else:
        print("Nova AI: Sorry, I don't understand that.")