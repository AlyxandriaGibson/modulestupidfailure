# Week 11 answers

## Exercise 1
1. The message the customer never saw:
    "You are Sunny. Answer in one short sentence."
2. How many times the customer has spoken:
    2 times.
3. Can the model tell that the last reply came from the order tool? Why does that matter?
    No, because every reply has the role "assistant," not a tool specific role, so the model can not identify it as a tool response.
4. The customer now types "thanks'. How many messages are sent on the next call?
    6 messages, the 5 existing ones plus the new "thanks".