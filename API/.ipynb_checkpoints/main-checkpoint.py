from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS

connection_string = "mongodb://localhost:27017/"
client = MongoClient(connection_string)

app = Flask(__name__)

CORS(app)

@app.route('/<user_request>')
def hello_world(user_request):
    
    db = client.Mortality_Rate_OF_HHS_Region.AVG_Rate_Data

    data = db.find_one({'request': user_request})

    if data is None:
        return jsonify({"error": "Data not found"}), 404
    
    del data['_id']
    
    
    return jsonify(data), 200


if __name__ == '__main__':
    app.run(debug=True)

