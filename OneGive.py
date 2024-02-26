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


db=sqlite3.connect('EatYuliia.db')
sql=db.cursor()
sql.execute("SELECT login FROM profileTel")
allLogins = sql.fetchall()  
i=0
for i in range(len(allLogins)):
    
    sql.execute(f'UPDATE profileTel SET BFallowed = 1 WHERE login = "{allLogins[i][0]}"')
    db.commit()
    sql.execute(f'UPDATE profileTel SET LNallowed = 1 WHERE login = "{allLogins[i][0]}"')
    db.commit()
    sql.execute(f'UPDATE profileTel SET EVallowed = 1 WHERE login = "{allLogins[i][0]}"')
    db.commit()
    
sql.execute("SELECT Name FROM Allowed") 
allNameAllowed=sql.fetchone()
for oneName in allNameAllowed:
    sql.execute(f'UPDATE Allowed SET Allowed = 1 WHERE Name = "{oneName}"')
    db.commit()