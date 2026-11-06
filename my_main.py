# my_main.py
# Author: Alyxandria Gibson

from my_assistant import FAQAssistant
from my_tool import FAQKnowledgeBase

FAQ_DATA = {
    "hours": "We are open from 9 AM - 5 PM, Monday through Friday.",
    "shipping": "Standard shipping takes 3-5 business days, and is free on orders over $60.",
    "warranty": "We offer a 1-year warranty on all products.",
}

faq_tool = FAQKnowledgeBase(FAQ_DATA)
assistant = FAQAssistant(
    "Bizzy",
    "You are a helpful and friendly customer service assistant answering general FAQ inquiries for Tampa Outfitters.",
    faq_tool,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
