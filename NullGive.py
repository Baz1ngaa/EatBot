from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text 
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import logging
from os import getenv
from sys import exit
import aiogram.utils.markdown as fmt
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand
import asyncio
import sqlite3
import time
import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import date
import random
from collections import Counter
import pytz


db=sqlite3.connect('EatTest.db')
sql=db.cursor()
sql.execute("SELECT login FROM profileTel")
allLogins = sql.fetchone()  
for peopleMan in allLogins:
    sql.execute(f'UPDATE profileTel SET BFallowed = 1 WHERE login = "{peopleMan}"')
    db.commit()
    sql.execute(f'UPDATE profileTel SET LNallowed = 0 WHERE login = "{peopleMan}"')
    db.commit()
    sql.execute(f'UPDATE profileTel SET EVallowed = 1 WHERE login = "{peopleMan}"')
    db.commit()
    print("ready")
sql.execute("SELECT Name FROM Allowed")
allNameAllowed=sql.fetchone()
for oneName in allNameAllowed:
    sql.execute(f'UPDATE Allowed SET Allowed = 1 WHERE Name = "{oneName}"')
    db.commit()
         