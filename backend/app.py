from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data_list = []


@app.route('/api/data', methods=['GET', 'POST'])
def manage_data():
    if request.method == 'POST':
        new_data = request.json
        if 'id' not in new_data or 'name' not in new_data or 'value' not in new_data:
            return jsonify({"error": "Invalid input"}), 400

        data_list.append(new_data)
        return jsonify(new_data), 201

    return jsonify(data_list)


@app.route('/api/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    global data_list
    data_list = [item for item in data_list if item['id'] != data_id]
    return jsonify({"message": "Data deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
