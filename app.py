
from flask import Flask, request, jsonify
import pickle

# Load the model
model = pickle.load(open('C:\\Users\\Asus\\GST\\random_forest_model.pkl', 'rb'))

# Initialize Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # get input data from request
    prediction = model.predict([data['input']])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
