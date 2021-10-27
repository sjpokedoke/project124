from flask import Flask, jsonify, request

app = Flask

list = [
    {
        'id': 1,
        'Name': 'Raju',
        'Contact': '9987644456',
        'Done': False,
    },
    {
        'id': 2,
        'Name': 'Rahul',
        'Contact': '9876543222',
        'Done': False,
    }
]

@app.route("/")
def helloworld():
    return "Hello world!"

@app.route("/addata", methods = ["POST"])
def addtask():
    if not request.json:
        request jsonify({
            "status": "error",
            "message": "Please add data",
        }, 400)
    
    contact = {
        'id': tasks[-1]["ID"]+1,
        'Name': request.json["Name"],
        'Contact': request.json['Contact', ''],
        'Done': False
    }
    list.append(contact)
    return jsonify ({
        "status": "success",
        "message": "contact added successfully"
    })

@app.route("/getdata")
def gettask():
    return jsonify({
        "data": list
    })

if (__name__ == "__main__"):
    app.run(debug = True)