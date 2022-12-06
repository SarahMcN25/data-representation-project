# This file contains a class which has functions to implement SQL commands in a python script. 
# This will be imported and used in link_to_db.py
# Author: Sarah McNelis - G00398343

import mysql.connector

class ArrivalsDAO:
    host =""
    user = ""
    password =""
    database =""
    connection = ""
    cursor =""

    def __init__(self): 
        # COME BACK TO THIS!!!!! SHOULD BE READ IN FROM CONFIG FILE!!!!! SEE W5/6
        self.host="localhost"
        self.user="root"
        self.password=""
        self.database="arrivals_at_snn"
    
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


    # CREATE AN ARRIVAL
    def create(self, values):
        cursor = self.getCursor()
        sql="INSERT INTO arrivals (airline, origin, destination, flight_number) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid


    # GET ALL ARRIVALS
    def getAll(self):
        cursor = self.getCursor()
        sql="SELECT * FROM arrivals"
        cursor.execute(sql)
        result = cursor.fetchall()
        self.closeAll()
        return result


    # FIND ARRIVAL BY ID
    def findByID(self, id):
        cursor = self.getCursor()
        sql="SELECT * FROM arrivals WHERE id=%s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return result


    # UPDATE ARRIVAL
    def update(self, values):
        cursor = self.getCursor()
        sql="UPDATE arrivals SET airline=%s, origin=%s, destination=%s, flight_number=%s  WHERE id=%s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()


    # DELETE ARRIVAL
    def delete(self, id):
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
    def createtable(self):
        cursor = self.getcursor()
        sql="CREATE TABLE arrivals (id int AUTO_INCREMENT NOT NULL PRIMARY KEY, airline varchar(250), origin varchar(3), destination varchar(3), flightnumber varchar(10))"
        cursor.execute(sql)
        self.connection.commit()
        self.closeAll()


arrivalsDAO = ArrivalsDAO()

'''
# TEST
 if __name__ == "__main__":
    # Once off setting up DB and table
#   arrivalsDAO.createDatabase()
#   arrivalsDAO.createTable()
    data = ('British Airways', 'BHX', 'SNN', 'BA6774')
    arrivalsDAO.create(data)
    print("It works!")
'''