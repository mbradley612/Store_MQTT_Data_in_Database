#------------------------------------------
#--- Author: Pradeep Singh
#--- Date: 20th January 2017
#--- Version: 1.0
#--- Python Ver: 2.7
#--- Details At: https://iotbytes.wordpress.com/store-mqtt-data-from-sensors-into-sql-database/
#------------------------------------------

import sqlite3

# SQLite DB Name
DB_Name =  "BoatGPS.db"

# SQLite DB Table Schema
TableSchema="""
drop table if exists GPSIMU_Data ;
create table GPSIMU_Data (
  id integer primary key autoincrement,
  lon float,
  lat float,
  speed float,
  track float,
  timestamp datetime,
  mode integer
  
);

"""

#Connect or Create DB File
conn = sqlite3.connect(DB_Name)
curs = conn.cursor()

#Create Tables
sqlite3.complete_statement(TableSchema)
curs.executescript(TableSchema)

#Close DB
curs.close()
conn.close()
