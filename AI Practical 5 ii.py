# Predefined responses for the chatbot
responses = {
"greeting": ["Hello! How can I assist you today?", "Hi there! How can I help you?", "Hey! How can I
assist you today?"],
"goodbye": ["Goodbye! Have a great day!", "Thanks for visiting! Take care!", "Goodbye! Feel free to
come back anytime!"],
"help": ["I can assist you with product information, services, and general inquiries. How can I help
you?",
"I am here to help you with any questions about our products or services. How can I assist?"],
"unknown": ["Sorry, I didn't understand that. Can you please clarify?", "I'm not sure about that, can
you rephrase it?", "Can you please provide more details?"],
"product_info": ["We offer a wide range of products including electronics, clothing, and home goods.
Would you like to know more about a specific product?",
"Our product catalog includes electronics, fashion, and home appliances. How can I assist
you with a specific product?"],
"store_hours": ["Store is open on Monday to Saturday from 9:00 AM to 6:00 PM. We are closed on
Sunday.",
"Our store hours are 9:00 AM to 6:00 PM, Monday through Saturday. We are closed on
Sundays."],
"contact_info": ["You can reach us by phone at (123) 456-7890 or via email at
support@example.com.",
"For customer support, call us at (123) 456-7890 or email us at support@example.com."],
}
# List to store user feedback
feedback_list = []
# Function to respond based on user's input
def get_response(user_input):
    user_input = user_input.lower().strip()
# If the user greets, return a greeting response
if any(greeting in user_input for greeting in ["hello", "hi", "hey"]):
return random.choice(responses["greeting"])
# If the user says goodbye, return a goodbye response
elif any(farewell in user_input for farewell in ["bye", "goodbye", "see you"]):
return random.choice(responses["goodbye"])
# If the user asks for help, return a help response
elif "help" in user_input:
return random.choice(responses["help"])
# If the user asks about products, return a product information response
elif any(keyword in user_input for keyword in ["product", "item", "buy"]):
return random.choice(responses["product_info"])
# If the user asks about store hours, return store hours response
elif any(keyword in user_input for keyword in ["hours", "open", "close"]):
return random.choice(responses["store_hours"])
# If the user asks for contact information, return the contact info
elif any(keyword in user_input for keyword in ["contact", "phone", "email"]):
return random.choice(responses["contact_info"])
# For any other input, return an unknown response
else:
    return random.choice(responses["unknown"])
# Function to get user feedback at the end of the conversation
def get_feedback():
print("\nWe'd love to hear your feedback! Please rate the conversation from 1 to 5 (1 being poor, 5
being excellent).")
feedback_rating = input("Your rating (1-5): ").strip()
# Validate feedback input
if feedback_rating.isdigit() and 1 <= int(feedback_rating) <= 5:
feedback_list.append(feedback_rating)
print(f"Thank you for your feedback! You rated this interaction as {feedback_rating}/5.")
else:
print("Invalid input. Please enter a number between 1 and 5.")
# Main function for interacting with the chatbot
def chatbot():
print("Welcome to the Customer Support Chatbot!")
print("Type 'bye' to end the conversation.")
while True:
user_input = input("You: ")
# End the conversation if the user types 'bye' or similar
if any(farewell in user_input.lower() for farewell in ["bye", "goodbye", "see you"]):
print("Chatbot:", random.choice(responses["goodbye"]))
break
# Otherwise, provide a response based on user input
jobs = [(3, 100), (1, 50), (2, 10)] # (deadline, profit)
jobs.sort(key=lambda x: x[1], reverse=True)
schedule = [None] * max(job[0] for job in jobs)
for deadline, profit in jobs:
 for i in range(deadline - 1, -1, -1):
 if schedule[i] is None:
 schedule[i] = profit
 break
print("Maximized Profit:", sum(filter(None, schedule)))







'''
============= RESTART: C:/Users/LENOVO/Desktop/AI Practical 5 ii.py ============
Welcome to the Customer Support Chatbot!
Type 'bye' to end the conversation.
You: Hii
Chatbot: Hey! How can I assist you today?
You: Need Some Help
Chatbot: I am here to help you with any questions about our products or services. How can I assist?
You: Information about product
Chatbot: Our product catalog includes electronics, fashion, and home appliances. How can I assist you with a specific product?
You: what is the opening time of the store
Chatbot: Store is open on Monday to Saturday from 9:00 AM to 6:00 PM. We are closed on Sunday.
You: How can I contact you
Chatbot: You can reach us by phone at (123) 456-7890 or via email at support@example.com.
You: thankyou bye
Chatbot: Thanks for visiting! Take care!

We'd love to hear your feedback! Please rate the conversation from 1 to 5 (1 being poor, 5 being excellent).
Your rating (1-5): 5
Thank you for your feedback! You rated this interaction as 5/5.
'''


