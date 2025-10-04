def chatbot():
    print("\n🤖 Chatbot is online! Type 'bye' to exit.\n")

    responses = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hi there! Nice to meet you.",
        "hey": "Hey! How’s it going?",
        "how are you": "I'm just a program, but I'm doing great! How about you?",
        "i am fine": "Glad to hear that!",
        "what is your name": "I'm your simple Python Chatbot.",
        "who made you": "I was created by a Python programmer like you!",
        "thanks": "You're welcome!",
        "thank you": "Anytime! Happy to help.",
        "good morning": "Good morning! Have a wonderful day.",
        "good night": "Good night! Sweet dreams.",
        "bye": "Goodbye! Have a nice day.",
        "help": "I can reply to greetings like 'hello', 'hi', 'how are you', and 'bye'."
    }

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in responses:
            print("Bot:", responses[user_input])
            if user_input == "bye":  # End the chat
                break
        else:
            print("Bot:Sorry, I don't understand that. Try saying 'hello', 'how are you', or 'help'.")

if __name__ == "__main__":
    chatbot()
