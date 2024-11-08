from flask import Flask, jsonify, request

app = Flask(__name__)
heart_record = []

@app.route('/heart', methods = ['POST'])
def create_new_record():
    new_record = request.get_json()
    heart_record.append(new_record)
    return f'Successful! Record ID: {new_record["heart_id"]}', 200

@app.route('/heart', methods = ['GET'])
def read_info():
    return jsonify(heart_record)

@app.route('/heart/<int:index>', methods = ['GET'])
def get_specific(index):
    return jsonify(heart_record[index])

@app.route('/heart/<int:index>', methods = ['PUT'])
def update_record(index):
    new_record = request.get_json()
    heart_record[index] = new_record
    return jsonify(heart_record[index]), 200

@app.route('/heart/<int:index>', methods = ['DELETE'])
def delete_record(index):
    heart_record.pop(index)
    return 'Record has been successfully deleted', 200
if __name__ == "__main__":
    app.run()