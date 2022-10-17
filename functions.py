import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import pgeocode
from geopy.distance import geodesic

mydb=mysql.connector.connect(
host='localhost',
database='mydatabase',
user='root',
password='***',
auth_plugin='mysql_native_password')

if mydb.is_connected():
  print('Successfully connected!')

cursor = mydb.cursor()

def printCityFunc(city, distance):

        cursor.reset()
        cursor.execute("SELECT zip FROM markets WHERE city='{}'".format(city))
        zip = str(cursor.fetchone())
        zip = zip[2:-3]

        data = pgeocode.Nominatim('US')
        df = data.query_postal_code(zip)
        df = list(df[-3: -1])

        cursor.reset()
        cursor.execute("SELECT y, x FROM markets")
        records = cursor.fetchall()

        marketStr = []

        for coords in records:

            if geodesic(coords, df).km <= distance:
                
                y = str(coords[0])
                x = str(coords[1])

                cursor.reset()
                cursor.execute("SELECT MarketName FROM Markets WHERE y = '{}' && x ='{}'".format(y, x))
                markets = str(cursor.fetchall())
                markets = markets[3:-4]

                howFarKm = str(int(geodesic(coords, df).km))
                
                marketStr.append(markets + ' ~ ' + howFarKm + ' km')

        return marketStr

 

def aboutMarketFunc(marketsName):
    try:
        marketsName = marketsName[0:-7]
        nullDigit = ' '
        if marketsName[-1] == nullDigit:
            marketsName = marketsName[0:-1]
        else: pass

        cursor.reset()
        cursor.execute("SELECT state, city, street, zip FROM Markets WHERE MarketName = '{}'".format(marketsName))
        markets = cursor.fetchone()
        # print(markets)

        marketsLst = []
        for properties in markets:
            marketsLst.append(properties)
                # print(marketsLst)

        output = marketsName + ' is situated in ' + marketsLst[0] + ', ' + marketsLst[1] + ' on ' + marketsLst[2] + ', the postal code is ' + marketsLst[3] + ' here is what we have'
    
        return output
    except:
        print('лажа, достала уже')
        return 'Sorry no data for this market in DataBase'

##############################################################
#                           MENU                             #
##############################################################

def addCitiesToComboBoxFunc():
    cursor.execute("SELECT city FROM markets")
    cities = cursor.fetchall()

    cityLst = []

    for city in cities:
        city = str(city)
        city = city[2:-3]
        cityLst.append(city)

    return sorted(cityLst)

##############################################################
#                           BUTTON                           #
##############################################################
def searchButtonClickedFunc():
    print('the button was clicked')




def radioActionFunc(rate, name):
    cursor.reset()
    cursor.execute("SELECT Rating FROM markets WHERE MarketName = '{}'".format(name))
    oldRate = str(cursor.fetchone())
    
    if oldRate == '(None,)':
        cursor.reset()
        cursor.execute("UPDATE markets SET Rating = '{}' WHERE MarketName = '{}';".format(rate, name))
        print('Рейтинг' + str(rate) + 'добавлен')
    else:
        oldRate = oldRate[1:-2]
        newRate = (float(oldRate) + float(rate))/2
        print(newRate)
        cursor.reset()
        cursor.execute("UPDATE markets SET Rating = '{}' WHERE MarketName = '{}';".format(newRate, name))


def getFromDB():
        cursor.reset()
        cursor.execute("SELECT MarketName FROM markets WHERE city='New York ' ")
        markets = cursor.fetchall()
        print(markets)

