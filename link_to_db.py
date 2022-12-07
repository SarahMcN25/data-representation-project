# This program will link commands from arrivalsDAO.py to my DB. 
# Author: Sarah McNelis - G00398343

from  classFunction import arrivalsDAO

# GET ALL ARRIVALS
print("Get all arrivals: ")
allArrivals = arrivalsDAO.getAll()
for arrival in allArrivals:
  print(arrival)


# CREATE AN ARRIVAL
latestid = arrivalsDAO.create(('British Airways', 'BHX', 'SNN', 'BA6774'))


# FIND ARRIVAL BY ID 
result = arrivalsDAO.findByID(latestid)
print ("Create arrival and find by id: ")
print (result)


# UPDATE AN ARRIVAL
arrivalsDAO.update(('Emirates', 'DXB', 'SNN', 'EK0162', latestid))
result = arrivalsDAO.findByID(latestid)
print("Updating arrival")
print (result)


# DELETE AN ARRIVAL
arrivalsDAO.delete(latestid)
