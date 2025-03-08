# chatbot.py
import logging

from ml_model import MLModel
from nlp_utils import preprocess_text

class ChatBot:
    def __init__(self):
        # Initialisiere das ML-Modell und Logging
        self.ml_model = MLModel()
        logging.info("ChatBot: Initialisierung abgeschlossen.")

    def respond(self, message):
        # NLP-Vorverarbeitung der Eingabe
        tokens = preprocess_text(message)
        processed_text = " ".join(tokens)
        
        # Vorhersage der Antwort mithilfe des ML-Modells
        response = self.ml_model.predict_response(processed_text)
        
        # Update des Modells mit der aktuellen Konversation (simpler Lernansatz)
        self.ml_model.update_model(processed_text, response)
        
        logging.info(f"ChatBot: Eingabe: {message} | Vorverarbeitet: {processed_text} | Antwort: {response}")
        return response
