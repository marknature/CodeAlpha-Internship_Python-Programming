import csv

# Load chat data from CSV
chat_data = {}
with open("Basic Chatbot(pedefined responses).csv", mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    previous_user_message = None
    for sender, message in reader:
        if sender.lower() == "user":
            previous_user_message = message.strip().lower()
        elif sender.lower() == "assistant" and previous_user_message:
            if previous_user_message not in chat_data:
                chat_data[previous_user_message] = message.strip()
            previous_user_message = None

# Chatbot logic
def basic_chatbot():
    print("Chatbot: Hello, I'm Kev! A chatbot powered by a csv file with predefined and limited responses."/n+"Type 'bye' to exit.")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        response = chat_data.get(user_input, "I don't understand.")
        print(f"Chatbot: {response}")

# Run the chatbot
basic_chatbot()
