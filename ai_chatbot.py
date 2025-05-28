import nltk
from nltk.chat.util import Chat, reflections
import random
from datetime import datetime

# Enhanced pairs with better emotional support and date handling
pairs = [
    [
        r"hi|hello|hey|greetings",
        ["Hello! How can I help you today?", "Hi there!", "Hey! What can I do for you?"]
    ],
    [
        r"nothing",
        ["If there's nothing specific, I'm happy to just chat!", "Okay, no problem. I'm here if you need anything."]
    ],
    [
        r"(how are you|how're you|how are you doing)",
        ["I'm doing well, thanks for asking! How about you?", "I'm great! How can I assist you today?"]
    ],
    [
        r"(i am|i'm) (not good|not well|not doing well|feeling down|sad|depressed)",
        ["I'm really sorry to hear that. Would you like to talk about what's bothering you?", 
         "That sounds really difficult. Remember I'm here to listen if you need to share."]
    ],
    [
        r"(not good|not well|feeling bad)",
        ["I'm sorry you're feeling that way. Is there something specific that's troubling you?"]
    ],
    [
        r"(what is|what's) the time(\?)?|time(\?)?",
        [f"It's currently {datetime.now().strftime('%I:%M %p')}",
         f"The time is now {datetime.now().strftime('%H:%M')}"]
    ],
    [
        r"(what is|what's) the date(\?)?|date(\?)?|today('?s|\s*)date",
        [f"Today is {datetime.now().strftime('%A, %B %d, %Y')}",
         f"The date is {datetime.now().strftime('%m/%d/%Y')}"]
    ],
    [
        r"(weather|forecast|temperature)( now)?(\?)?|what('s| is) the weather( like)?( now)?(\?)?",
        ["For the most accurate weather information, I recommend checking weather.com or your local weather app!"]
    ],
    [
        r"ok(ay)?",
        ["Alright!", "Okay! Let me know if there's anything else I can help with."]
    ],
    [
        r"thank(s| you)",
        ["You're very welcome!", "Happy to help!", "My pleasure!"]
    ],
    [
        r"(bye|goodbye|quit|see you)",
        ["Goodbye! Take care of yourself!", "It was nice chatting! Wishing you well!", "Take care and don't hesitate to come back if you need anything!"]
    ],
    [
        r"(.*)",
        ["I want to make sure I understand correctly. Could you say that in another way?",
         "I'm still learning. Could you help me understand what you mean?"]
    ]
]

class SupportiveChatBot(Chat):
    def __init__(self, pairs, reflections):
        super().__init__(pairs, reflections)
    
    def respond(self, str):
        str = str.lower().strip()
        if not str:
            return "I'm here to chat if you'd like to type something."
        return super().respond(str)

def chat():
    print("Hello! I'm your supportive chatbot. Type 'quit' to exit.")
    chatbot = SupportiveChatBot(pairs, reflections)
    chatbot.converse()

if __name__ == "__main__":
    chat()
