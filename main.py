from flask import Flask, jsonify, request
from flask import make_response,redirect,render_template

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/update',methods=['GET'])
def sensor_data():



@app.route('/update',methods=['POST'])
def update_sensor_data():
