# my_assistant.py
# Author: Alyxandria Gibson

HANDOFF_WORDS = ["refund", "dispute", "return", "complaint"]


class FAQAssistant:
    """A mock FAQ assistant for Tampa Outfitters."""

    def __init__(self, name, instructions, faq_tool):
        """Set up an assistant with its own name, instructions, faq tool, and history."""
        self.name = name
        self.instructions = instructions
        self.faq_tool = faq_tool
        self.history = []

    def respond(self, user_message):
        """Record the message, determine a reply, record the reply, and return it."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Select a reply based on keyword rules."""
        text = user_message.lower()
        if self.needs_human(text):
            return "Financial and return requests require a human agent. I am routing you to customer support."
        if "policy" in text or "hours" in text or "shipping" in text:
            return self.faq_reply(user_message)
        if "hello" in text:
            return f"Hello! I'm {self.name}. I can answer questions about store hours, shipping, and policies."
        return "I'm not sure how to help with that. I can answer questions about store hours, shipping, and policies."

    def needs_human(self, text):
        """Return True if the request requires a human to handle it."""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def faq_reply(self, user_message):
        """Retrieve an answer using the FAQ tool."""
        topic = self.faq_tool.find_topic(user_message)
        if topic is None:
            return "Which topic? Please ask about store hours, shipping, or policies."
        answer = self.faq_tool.answer_for(topic)
        return answer
