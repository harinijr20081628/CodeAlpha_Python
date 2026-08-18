print("🤖 Chatbot: Hello! I'm your AI chatbot.")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower().strip()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How are you?")

    elif user == "how are you":
        print("Bot: I'm doing great! 😊")

    elif user == "im good" or user == "i am good":
        print("Bot: That's great to hear! 😊")

    elif user == "what is your name":
        print("Bot: My name is Harini's Chatbot.")

    elif user == "what can you do":
        print("Bot: I can answer simple questions and chat with you.")

    elif user == "what is python":
        print("Bot: Python is a popular programming language.")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "what is machine learning":
        print("Bot: Machine Learning is a part of AI that learns from data.")

    elif user == "what is data science":
        print("Bot: Data Science is used to analyze data and find useful information.")

    elif user == "good morning" or user == "morning":
        print("Bot: Good morning! Have a great day! ☀️")

    elif user == "good night":
        print("Bot: Good night! Sleep well! 🌙")

    elif user == "thank you" or user == "thanks":
        print("Bot: You're welcome! 😊")

    elif user == "who created you":
        print("Bot: I was created as a Python chatbot project.")

    elif user == "bye" or user == "exit":
        print("Bot: Goodbye! Have a nice day! 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that.")