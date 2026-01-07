"""
Script to save the trained model and vectorizer.
Run this after training the model in your notebook.

Make sure the following variables are available in your notebook:
- tfidf: TfidfVectorizer object
- clf: LogisticRegression model
"""

import joblib
import json

# This script expects you to copy the model objects from your notebook
# You can also run this code directly in a notebook cell:

"""
import joblib

# Save the vectorizer and model
joblib.dump(tfidf, 'classifier/tfidf_vectorizer.pkl')
joblib.dump(clf, 'classifier/gender_classifier.pkl')

print("Model saved successfully!")
"""

if __name__ == "__main__":
    print("This script should be run from your notebook.")
    print("Copy the following code to a notebook cell after training:")
    print()
    print("import joblib")
    print("joblib.dump(tfidf, 'classifier/tfidf_vectorizer.pkl')")
    print("joblib.dump(clf, 'classifier/gender_classifier.pkl')")
    print("print('Model saved successfully!')")

