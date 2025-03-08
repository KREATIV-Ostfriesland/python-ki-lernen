# ml_model.py
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import logging

class MLModel:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.classifier = MultinomialNB()
        self.trained = False
        
        # Initiale Trainingsdaten (einfache Beispieldaten)
        self.X_train = [
            "hallo",
            "hilfe",
            "wie geht es dir",
            "was machst du",
            "tschüss"
        ]
        self.y_train = [
            "Hallo, wie kann ich dir helfen?",
            "Erzähl mir, wobei du Hilfe brauchst.",
            "Mir geht es gut, danke der Nachfrage!",
            "Ich chatte gerade mit dir.",
            "Auf Wiedersehen!"
        ]
        self.train_model()

    def train_model(self):
        # Training des Modells mit den aktuellen Daten
        X_counts = self.vectorizer.fit_transform(self.X_train)
        self.classifier.fit(X_counts, self.y_train)
        self.trained = True
        logging.info("MLModel: Training abgeschlossen.")

    def update_model(self, new_input, new_response):
        # Aktualisiere die Trainingsdaten und retrainiere das Modell
        self.X_train.append(new_input)
        self.y_train.append(new_response)
        self.train_model()
        logging.info("MLModel: Modell aktualisiert mit neuen Daten.")

    def predict_response(self, user_input):
        if not self.trained:
            return "Entschuldigung, ich bin noch nicht trainiert."
        input_counts = self.vectorizer.transform([user_input])
        prediction = self.classifier.predict(input_counts)
        return prediction[0]
