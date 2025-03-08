# main.py
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