# chatbot.py

class ChatBot:
    def __init__(self):
        # Hier können wir später Modelle laden oder Konfigurationen initialisieren
        pass

    def respond(self, message):
        """
        Eine einfache Logik, die auf Schlüsselwörtern basiert.
        Diese Methode können wir später durch ML-basierte Ansätze erweitern.
        """
        if "hallo" in message.lower():
            return "Hallo! Wie kann ich dir helfen?"
        elif "hilfe" in message.lower():
            return "Natürlich, ich stehe zur Verfügung. Was brauchst du?"
        else:
            return "Das ist interessant! Erzähl mir mehr."
