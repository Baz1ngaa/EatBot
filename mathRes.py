
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

hour=17
min=25
hournow=18
minnow=26
interval=60
if( (min+interval)%60 != min+interval):
    if(hournow < (hour+1) % 24 or minnow <= (min+interval) % 60):
        print("ok")
    else:
        print("no")
if( (min+interval)%60 == min+interval):
    print("yes")
    if(hournow <= hour % 24 and minnow <= (min+interval) % 60):
        print("ok")
    else:
        print("no")


tz_Vienna = pytz.timezone('Europe/Vienna')
currentime=datetime.datetime.now(tz_Vienna)
currentdate=date.today()
print(f"{currentime.hour}:{currentime.minute}")

if (currentdate.weekday()==0 or currentdate.weekday()== 1 or currentdate.weekday()== 2 or currentdate.weekday()==3 or currentdate.weekday()==4 ):
    print(currentdate.weekday()) 

    

