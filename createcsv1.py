#Note: U need to customize this program, as per your project DB and tables.
import sys
import csv
import os
#import pymysql
#con = pymysql.connect(host='localhost', port=3306, user='team1', passwd='test623', db='apri1')

import sqlite3
con = sqlite3.connect('employ1')

cur = con.cursor()
cur.execute('SELECT * FROM activities;')
rows = cur.fetchall()
fp = open('activities1.csv', 'w')
myFile = csv.writer(fp)
myFile.writerows(rows)
fp.close()
print('activities1.csv file successfully created')
cur.execute('SELECT * FROM mentorset;')
rows = cur.fetchall()
fp = open('mentorset1.csv', 'w')
myFile = csv.writer(fp)
myFile.writerows(rows)
fp.close()
print('mentorset1.csv file successfully created')
con.commit()

