# main.py

import logging
from config import LOG_FILE, LOG_LEVEL
logging.basicConfig(filename=LOG_FILE, level=LOG_LEVEL.upper())

from chatbot import ChatBot

def main():
    bot = ChatBot()
    print("Hallo! Ich bin dein einfacher Chatbot. Was möchtest du wissen? (Tippe 'exit' zum Beenden)")
    
    while True:
        user_input = input("Du: ")
        if user_input.lower() in ["exit", "quit"]:
            print("ChatBot: Auf Wiedersehen!")
            break
        response = bot.respond(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()

# In diesem Beispiel haben wir die Hauptfunktionalität unseres Chatbots in der main.py-Datei implementiert.
# Wir haben ein ChatBot-Objekt erstellt und eine einfache Benutzerschnittstelle implementiert, die es dem Benutzer ermöglicht, mit dem Chatbot zu interagieren.     


