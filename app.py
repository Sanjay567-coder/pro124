from flask import Flask,jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'Name': u'SAI',
        'Contact': u'9987644456', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'JAYAVEL',
        'Contact': u'9876543222', 
        'done': False
    },
    {
        'id': 3,
        'Name': u'LINGESH',
        'Contact': u'9584623180', 
        'done': False
    },
    {
        'id': 4,
        'Name': u'KRISHNA',
        'Contact': u'9559216955', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    tasks.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)