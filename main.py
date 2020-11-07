from flask import Flask, jsonify, request
from flask import make_response,redirect,render_template

app = Flask(__name__)

data=0

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/update',methods=['GET'])
def sensor_data():
    global data
    return jsonify({'count':data})



@app.route('/update/<value>',methods=['POST'])
def update_sensor_data(value):
    global data
    data=value
    return("Sensor value updated")
