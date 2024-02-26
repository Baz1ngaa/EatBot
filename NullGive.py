

import logging
from os import getenv
from sys import exit

import asyncio
import sqlite3
import time
import datetime

from datetime import date
import random
from collections import Counter
import pytz


db=sqlite3.connect('EatTest.db')
sql=db.cursor()
sql.execute("SELECT login FROM profileTel")
allLogins = sql.fetchall()  
print(allLogins)
for peopleMan in allLogins:
    sql.execute(f'UPDATE profileTel SET BFallowed = 0 WHERE login = "{peopleMan}"')
    db.commit()
    sql.execute(f'UPDATE profileTel SET LNallowed = 0 WHERE login = "{peopleMan}"')
    db.commit()
    sql.execute(f'UPDATE profileTel SET EVallowed = 0 WHERE login = "{peopleMan}"')
    db.commit()
    print("ready")
sql.execute("SELECT Name FROM Allowed")
allNameAllowed=sql.fetchone()
for oneName in allNameAllowed:
    sql.execute(f'UPDATE Allowed SET Allowed = 1 WHERE Name = "{oneName}"')
    db.commit()
         