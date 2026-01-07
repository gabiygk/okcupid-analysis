import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

def clean(s):
    """Clean text the same way as training data"""
    s = s.lower()
    s = re.sub(r"[^a-z\s]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()

def predict_gender_from_text(text: str, tfidf, clf):
    """
    Given a phrase, return:
    - predicted gender label
    - probabilities for each class (male/female)
    """
    # Clean the text the same way as training
    text_clean = clean(text)
    
    # Vectorize with the SAME tfidf object
    X_new = tfidf.transform([text_clean])
    
    # Get probabilities
    probs = clf.predict_proba(X_new)[0]     # e.g. [p(class0), p(class1)]
    classes = clf.classes_                  # e.g. ['f', 'm']
    
    idx = np.argmax(probs)
    predicted_label = classes[idx]
    
    # Map 'm' to 'Male' and 'f' to 'Female' for display
    gender_map = {'m': 'Male', 'f': 'Female'}
    
    return {
        "input_text": text,
        "predicted_sex": predicted_label,
        "predicted_gender": gender_map.get(predicted_label, predicted_label),
        "probabilities": {gender_map.get(cls, cls): float(p) for cls, p in zip(classes, probs)}
    }

