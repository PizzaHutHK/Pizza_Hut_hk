import webbrowser
import datetime
import pymysql
from flask import Flask, render_template, redirect, url_for, request



#Connect to the database
DB = pymysql.connect( 
  host = "sg2plzcpnl487151.prod.sin2.secureserver.net",
  user = "i8296166_wp1",
  password = "Z.77XCsx57LUBE2vK9X68",  
  database = "Delivery_Information"
)
CUR = DB.cursor() 


