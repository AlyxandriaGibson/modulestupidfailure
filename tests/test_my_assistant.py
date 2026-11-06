# test_my_assistant.py
# Author: Alyxandria Gibson

from my_assistant import FAQAssistant
from my_tool import FAQKnowledgeBase


def make_assistant():
    """Create a new assistant instance for testing."""
    faq_data = {
        "store hours": "We are open from 9 AM - 5 PM, Monday through Friday.",
        "shipping": "3-5 business days.",
    }
    tool = FAQKnowledgeBase(faq_data)
    return FAQAssistant("Bizzy", "Clearly answer and assist with FAQs.", tool)


def test_faq_questions_uses_tool():
    assistant = make_assistant()
    reply = assistant.respond("What are your store hours?")
    assert "We are open from 9 AM - 5 PM, Monday through Friday." in reply


def test_faq_missing_topic_asks_for_clarification():
    assistant = make_assistant()
    reply = assistant.respond("What is your policy?")
    assert "Which topic? Please ask about store hours, shipping, or policies." in reply


def test_human_handoff_for_sensitive_topics():
    assistant = make_assistant()
    reply = assistant.respond("I want a refund for my order.")
    assert (
        "Financial and return requests require a human agent. I am routing you to customer support."
        in reply
    )


def test_unknown_request_gets_safe_fallback():
    assistant = make_assistant()
    reply = assistant.respond("Can you tell me a joke?")
    assert "I'm not sure how to help with that." in reply


def test_history_records_turns():
    assistant = make_assistant()
    assistant.respond("hello")
    assistant.respond("What are your store hours?")
    assert len(assistant.history) == 4
