# This program creates an application server that will implement a RESTful API. 
# Author: Sarah McNelis - G00398343

# Code adapted from W8 lecture and labs: <https://web.microsoftstream.com/video/c575feed-7ee1-4eec-b70e-c1b49204146c?list=studio> 


from flask import Flask, url_for, request, redirect, abort, jsonify


app = Flask(__name__, static_url_path='', static_folder='staticpages')


# Dummy array for testing
arrivals=[
        {"ID":1, "Airline":"Ryanair", "Origin": "STN", "Destination":"SNN", "Flight Number":"FR310" },
        {"ID":2, "Airline":"AerLingus", "Origin": "JFK", "Destination":"SNN", "Flight Number":"EI110" },
        {"ID":3, "Airline":"Delta Airlines", "Origin": "ATL", "Destination":"SNN", "Flight Number":"DL206" },
        {"ID":4, "Airline":"American Airlines", "Origin": "PHL", "Destination":"SNN", "Flight Number":"AA089" }
]


nextId = 5 


# TEST
@app.route('/')
def index():
    return "hello"


# GET ALL ARRIVALS
# curl http://127.0.0.1:5000/arrivals
@app.route('/arrivals')
def getAll():
    #return "served by Get All()" #debug

    return jsonify(arrivals)


# FIND ARRIVAL BY ID 
# curl http://127.0.0.1:5000/arrivals/2
@app.route('/arrivals/<int:id>')
def findById(id):
    #return "served by find by id with id " + str(id) # debug

    # Lambda searches arrivals and only return back specific id.
    foundArrivals = list(filter (lambda t : t["ID"]== id, arrivals))

    if len(foundArrivals) == 0:
        return jsonify({}), 204

    return jsonify(foundArrivals[0])


# CREATE AN ARRIVAL
# curl -X POST -H "content-type:application/json" -d "{\"Airline\":\"EasyJet\", \"Origin\":\"CDG\", \"Destination\":\"SNN\", \"Flight Number\":\"EZY6771\"}"  http://127.0.0.1:5000/arrivals
@app.route('/arrivals', methods=['POST'])
def create():
    #return "served by create()" # debug

    global nextId

    if not request.json:
        abort(400)

    arrival = {
        "ID":nextId, 
        "Airline": request.json["Airline"], 
        "Origin": request.json["Origin"],
        "Destination": request.json["Destination"],
        "Flight Number": request.json["Flight Number"]
    }
    # Append to arrivals, up an id and return in json form. 
    arrivals.append(arrival)
    nextId += 1
    return jsonify(arrival)


# UPDATE AN ARRIVAL
#  curl -X PUT -H "content-type:application/json" -d "{\"Airline\":\"Lufthansa\", \"Origin\":\"FRA\", \"Destination\":\"SNN\", \"Flight Number\":\"LH401\"}"  http://127.0.0.1:5000/arrivals/1
@app.route('/arrivals/<int:id>', methods=['PUT'])
def update(id):
    #return "served by update with id " + str(id) #debug

    foundArrivals = list(filter (lambda t : t["ID"]== id, arrivals))

    if len(foundArrivals) == 0:
        return jsonify({}), 404

    currentArrival = foundArrivals[0]

    if 'Airline' in request.json:
        currentArrival['Airline'] = request.json['Airline']

    if 'Origin' in request.json:
        currentArrival['Origin'] = request.json['Origin']
            
    if 'Destination' in request.json:
        currentArrival['Destination'] = request.json['Destination']

    if 'Flight Number' in request.json:
        currentArrival['Flight Number'] = request.json['Flight Number']

    return jsonify(currentArrival)


# DELETE AN ARRIVAL
# curl -X DELETE http://127.0.0.1:5000/arrivals/1
@app.route('/arrivals/<int:id>', methods=['DELETE'])
def delete(id):
    #return "served by delete with id " + str(id) #debug

    foundArrivals = list(filter (lambda t : t["ID"]== id, arrivals))

    if len(foundArrivals) == 0:
        return jsonify({}), 404

    arrivals.remove(foundArrivals[0])

    return jsonify({"done":True})


# RUN THE PROGRAM
if __name__ == "__main__":
    app.run(debug=True)