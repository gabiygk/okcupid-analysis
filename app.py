from flask import Flask, render_template, request, jsonify
import joblib
import os
from classifier.model_utils import predict_gender_from_text

app = Flask(__name__)

# Load model and vectorizer
MODEL_PATH = 'classifier/gender_classifier.pkl'
VECTORIZER_PATH = 'classifier/tfidf_vectorizer.pkl'

if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
    clf = joblib.load(MODEL_PATH)
    tfidf = joblib.load(VECTORIZER_PATH)
    model_loaded = True
    print("Model loaded successfully!")
else:
    model_loaded = False
    print(f"Warning: Model files not found!")
    print(f"Please run the save_model code in your notebook first.")
    print(f"Looking for: {MODEL_PATH} and {VECTORIZER_PATH}")

@app.route('/')
def index():
    return render_template('index.html', model_loaded=model_loaded)

@app.route('/predict', methods=['POST'])
def predict():
    if not model_loaded:
        return jsonify({
            'error': 'Model not loaded. Please save the model first.'
        }), 500
    
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({
                'error': 'Please provide some text to analyze.'
            }), 400
        
        result = predict_gender_from_text(text, tfidf, clf)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

