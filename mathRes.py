
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
#from apscheduler.schedulers.asyncio import AsyncIOScheduler
# hour=18
# min=40
# hournow=18
# minnow=41
# if( (min+30)%60 != min+30):
#     if(hournow < (hour+1) % 24 or minnow <= (min+30) % 60):
#         print("ok")
#     else:
#         print("no")
# if( (min+30)%60 == min+30):
#     print("yes")
#     if(hournow <= hour % 24 and minnow <= (min+30) % 60):
#         print("ok")
#     else:
#         print("no")


currentime=datetime.datetime.now()
currentdate=date.today()
print(f"{currentime.hour}:{currentime.minute}") 
print(currentdate.weekday())
    

