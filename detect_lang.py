import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector
#from tqdm import tqdm  # For progress bars

# Load the Dutch language model
nlp = spacy.load("nl_core_news_sm")

# Custom language detector factory function
@Language.factory("language_detector") 
def create_language_detector(nlp, name):
    return LanguageDetector() # Create the detector component

# Add language detector to the spaCy pipeline
nlp.add_pipe("language_detector", last=True)  

# Function to check if the text is in English
def is_english(text):
    doc = nlp(text)  # Process the text with the spaCy pipeline
    detect_language = doc._.language  # Access language detection results
    return detect_language['language'] == 'en'  # Check if detected language is English
