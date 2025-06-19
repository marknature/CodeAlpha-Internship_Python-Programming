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


