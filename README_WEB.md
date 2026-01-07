# Gender Prediction Web Interface

A simple web interface to demonstrate the gender prediction AI from text analysis.

## Setup

1. **First, save your trained model** by running the model saving cell in `analysis.ipynb` (it will create `classifier/tfidf_vectorizer.pkl` and `classifier/gender_classifier.pkl`)

2. **Install dependencies** (if not already installed):
   ```bash
   pip install flask joblib scikit-learn numpy
   ```
   Or use the requirements file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the web app**:
   ```bash
   python app.py
   ```

4. **Open your browser** and go to: `http://localhost:5000`

## Usage

- Enter any text in the text box
- Click "Predict Gender" to see the AI's prediction
- The interface will show:
  - Predicted gender (Male/Female)
  - Probability scores for each gender

## Files

- `app.py` - Flask web application
- `classifier/model_utils.py` - Prediction function and utilities
- `classifier/save_model.py` - Script to save trained models
- `templates/index.html` - Web interface HTML
- `classifier/gender_classifier.pkl` - Trained model (created after saving)
- `classifier/tfidf_vectorizer.pkl` - TF-IDF vectorizer (created after saving)

