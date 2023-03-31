
# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
# from aiogram.dispatcher.filters import Text 
# from aiogram import Dispatcher, types
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# import logging
# from os import getenv
# from sys import exit
# import aiogram.utils.markdown as fmt
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.types import BotCommand
# import asyncio
# from docx import Document
# from docx.shared import Inches
# import sqlite3
# import time
import datetime
from datetime import date
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import pytz

import sqlite3
from collections import Counter

db=sqlite3.connect('EatTest.db')
sql=db.cursor()

# hour=17
# min=
# hournow=18
# minnow=26
# interval=60
# if( (min+interval)%60 != min+interval):
#     if(hournow < (hour+1) % 24 or minnow <= (min+interval) % 60):
#         print("ok")
#     else:
#         print("no")
# if( (min+interval)%60 == min+interval):
#     print("yes")
#     if(hournow <= hour % 24 and minnow <= (min+interval) % 60):
#         print("ok")
#     else:
#         print("no")
eveningHour=19
eveningMinute=50
intervalEat=50
tz_Vienna = pytz.timezone('Europe/Vienna')
currentime=datetime.datetime.now(tz_Vienna)
print(eveningHour, ":", eveningMinute)
print("Текущее: ",currentime.hour, ":", currentime.minute)

if( (eveningMinute+intervalEat)%60 != eveningMinute+intervalEat):
    if(currentime.hour+1 <=  ((eveningHour+1) % 24) or currentime.minute <= ((eveningMinute+intervalEat) % 60)):

        print( "Умница, ты поела вовремя")
        print("1")
    else:
        print( "К сожалению, ты поела не вовремя")
        print("2")


if( (eveningMinute+intervalEat)%60 == eveningMinute+intervalEat):
    if(currentime.hour <= (eveningHour % 24) and currentime.minute <= ((eveningMinute+intervalEat) % 60)):
        print( "Умница, ты поела вовремя")
        print("3")            
                       
                        
    else:
        print( "К сожалению, ты поела не вовремя")
        print("4")
    

