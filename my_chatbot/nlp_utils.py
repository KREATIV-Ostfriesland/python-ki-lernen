import nltk
import os
from nltk.tokenize import word_tokenize

# Füge deinen nltk_data-Pfad hinzu, falls nicht schon in nltk.data.path enthalten
nltk_data_path = os.path.expanduser('~/nltk_data')
if nltk_data_path not in nltk.data.path:
    nltk.data.path.append(nltk_data_path)

# Überprüfe und lade 'punkt' herunter, falls nötig
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', download_dir=nltk_data_path)

# Überprüfe und lade 'punkt_tab' herunter, falls nötig
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab', download_dir=nltk_data_path)

def preprocess_text(text):
    """
    Wandelt den Text in Kleinbuchstaben um und tokenisiert ihn.
    """
    return word_tokenize(text.lower())