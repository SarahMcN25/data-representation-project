# This file contains a class which has functions to implement SQL commands in a python script. 
# This will be imported and used in link_to_db.py
# Author: Sarah McNelis - G00398343

import mysql.connector
import config as cfg

class ArrivalsDAO:
    host = ""
    user = ""
    password = ""
    database = ""
    connection = ""
    cursor = ""


    # GET CONFIG DETAILS
    def __init__(self): 
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']
    

    # GET CURSOR - MAKE CONNECTION 
    def getCursor(self): 
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor


    # CLOSE CURSOR AND CONNECTION
    def closeAll(self):
        self.connection.close()
        self.cursor.close()


    # GET ALL ARRIVALS
    def getAllArrivals(self):
        cursor = self.getCursor()
        sql="SELECT * FROM arrivals"
        cursor.execute(sql)
        result = cursor.fetchall()
        self.closeAll()
        return result


    # CREATE AN ARRIVAL
    def createArrival(self, values):
        cursor = self.getCursor()
        sql="INSERT INTO arrivals (airline, origin, destination, flight_number, scheduled_arrival, actual_arrival) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid


    # UPDATE ARRIVAL
    def updateArrival(self, values):
        cursor = self.getCursor()
        sql="UPDATE arrivals SET airline=%s, origin=%s, destination=%s, flight_number=%s, scheduled_arrival=%s, actual_arrival=%s WHERE id=%s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()


    # DELETE ARRIVAL
    def deleteArrival(self, id):
        cursor = self.getCursor()
        sql="DELETE FROM arrivals WHERE id=%s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll
        print("Arrival deleted") 

    
    # CREATE A DATABASE
    def createDatabase(self):
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password   
        )
        self.cursor = self.connection.cursor()
        sql="CREATE DATABASE "+ self.database
        self.cursor.execute(sql)
        self.connection.commit()
        self.closeAll()


    # CREATE A DATABASE TABLE
    def createTable(self):
        cursor = self.getcursor()
        sql="CREATE TABLE arrivals (id int AUTO_INCREMENT NOT NULL PRIMARY KEY, airline varchar(50), origin varchar(3), destination varchar(3), flight_number varchar(10), scheduled_arrival varchar(4), actual_arrival varchar(4))"
        cursor.execute(sql)
        self.connection.commit()
        self.closeAll()


arrivalsDAO = ArrivalsDAO()

'''
# MAIN FUNCTION
 if __name__ == "__main__":
    # Once off setting up DB and table
#   arrivalsDAO.createDatabase()
#   arrivalsDAO.createTable()
    # TESTING DATA
    data = ('British Airways', 'BHX', 'SNN', 'BA6774')
    arrivalsDAO.create(data)
    print("It works!")
'''