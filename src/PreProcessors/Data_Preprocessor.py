# data preprocessing
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

import pandas as pd

# nltk.download('stopwords')
# nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocessor(data):
    
    # Convert to lowercase
    sentence = data.lower()
    
    # Remove punctuation
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        
    # Remove numbers
    sentence = re.sub(r'\d+', '', sentence)
        
    # Remove stopwords and apply lemmatization
    sentence = ' '.join([lemmatizer.lemmatize(word) for word in sentence.split() if word not in stop_words])
        
    # Append the processed sentence and its label
    processed_data = sentence    
    
    return processed_data


