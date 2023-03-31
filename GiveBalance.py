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
from docx import Document
from docx.shared import Inches
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
for value in sql.execute("SELECT * FROM profileTel"):
    print(value)
login_id=input("ID: ")
newbalance=input("Баланс: ")
sql.execute(f'UPDATE profileTel SET strike = {int(newbalance)} WHERE login = "{int(login_id)}"')
db.commit()