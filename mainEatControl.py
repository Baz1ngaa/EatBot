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
#from data import config





API_TOKEN = '6129552928:AAEjUQt8iLEYAk2mCAApSZKDkxe14B8U5N8'
#main 6129552928:AAEjUQt8iLEYAk2mCAApSZKDkxe14B8U5N8
 
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
available_timeBreak = ["6:30","6:45","7:00", "7:15", "7:30"]
available_timeBreakWeeking = ["9:30","9:45","10:00", "10:15", "10:30", "10:45", "11:00", "11:15", "11:30"]
available_timeLaunch = ["12:30","12:45","13:00", "13.15","13:30", "13:45", "14:00", "14:15", "14:30", "14:45", "15:00"]
available_timeEvening = ["18:00", "18:15","18:30", "18.45","19:00", "19:15", "19:30","19:45", "20:00","19:45"]
available_YesOrNot = ["Да","Нет"]
available_Ready = ["Готово"]

prise=[90,140,300,420,800]
available_Present = [f"Шоколадка: {prise[0]}",f"Большая шоколадка: {prise[1]}",f"Ужин: {prise[2]}", f"Секретный подарок: {prise[3]}", f"День послушности: {prise[4]}" ]
global balance, allowedBalance
balance=0
allowedBalance=0
available_Eat=["Я позавтракала", " Я пообедала", "Я поужинала"]
nettName=["Цветочек","Розочка", "Котёнок", "Солнышко", "Звездочка", "Пупсик", "Счастье мое", "Зайка", "Зая", "Мышонок", "Выдренок", "Юлечка", "Юленька", "Принцесса", "Сокровище", "Вреднюлька", "Зайкин", "Пупсик", "Королева", "Милая"]
global intervalEat
intervalEat=30
class student(StatesGroup):
    waiting_for_timeBreakfast = State()
    waiting_for_timeLaunch = State()
    waiting_for_timeEvening = State()
    waiting_for_timeBreakfastWeeking = State()
    waiting_for_timeLaunchWeeking = State()
    waiting_for_timeEveningWeeking = State()
    waiting_for_ready = State()
    waiting_for_buy= State()
    waiting_for_startChoose= State()
    waiting_for_EatReadyChoose=State()
    #ready=State()
    #waiting_for_table=State()
    #waiting_for_gettable=State()


db=sqlite3.connect('EatYuliia.db')
sql=db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS profileTel (
    login TEXT,
    timeBreakfastHour INT, 
    timeBreakfastMinute INT,        
    timeLaunchHour INT,
    timeLaunchMinute INT,
    timeEveningHour INT,
    timeEveningMinute INT,
    timeBreakfastWeekingHour INT, 
    timeBreakfastWeekingMinute INT,        
    timeLaunchWeekingHour INT,
    timeLaunchWeekingMinute INT,
    timeEveningWeekingHour INT,
    timeEveningWeekingMinute INT,
    strike INT)""")
db.commit()





async def cmd_start(message: types.Message, state: FSMContext):
    
    
    await message.answer(f"Привет, {message.from_user.full_name}, я помогу тебе контролировать приемы пищи и вознаграждать тебя за их соблюдения. В определенное время я буду присылать уведомление, на которые ты должна будешь прислать подтверждение приема пищи.")
    time.sleep(1)
    await message.answer(f"Если ты успела поесть максимум через {intervalEat} минут после сообщения, то ты получишь на свой баланс 10 монет.\n\n*Расценки в магазине*: \n   {available_Present[0]} \n   {available_Present[1]} \n   {available_Present[2]} \n   {available_Present[3]} \n   {available_Present[4]} ", parse_mode="Markdown")
    time.sleep(1)
    
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for hour in available_timeBreak:
        keyboard.add(hour)
    await message.answer(f"Теперь выбери время, когда ты обычно *завтракаешь* в будни",reply_markup=keyboard, parse_mode="Markdown")
    global login_id
    login_id=message.from_user.id
    global user_id
    user_id=message.from_user.id
    global user_timeLaunchHour, user_timeLaunchMinute, user_timeEveningHour, user_timeEveningMinute, user_timeBreakfastHour, user_timeBreakfastMinute, user_timeLaunchWeekingHour, user_timeLaunchWeekingMinute, user_timeEveningWeekingHour, user_timeEveningWeekingMinute, user_timeBreakfastWeekingHour, user_timeBreakfastWeekingMinute,user_strike
    user_timeLaunchHour=0
    user_timeLaunchMinute=0
    user_timeEveningHour=0
    user_timeEveningMinute=0
    user_timeBreakfastHour=0 
    user_timeBreakfastMinute=0
    user_timeLaunchWeekingHour=0
    user_timeLaunchWeekingMinute=0
    user_timeEveningWeekingHour=0
    user_timeEveningWeekingMinute=0
    user_timeBreakfastWeekingHour=0 
    user_timeBreakfastWeekingMinute=0
    user_strike = 0
    sql.execute(f"SELECT login FROM profileTel WHERE login = '{login_id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO profileTel VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (login_id, user_timeBreakfastHour, user_timeBreakfastMinute,user_timeLaunchHour, user_timeLaunchMinute, user_timeEveningHour, user_timeEveningMinute,user_timeBreakfastWeekingHour, user_timeBreakfastWeekingMinute, user_timeLaunchWeekingHour, user_timeLaunchWeekingMinute, user_timeEveningWeekingHour, user_timeEveningWeekingMinute,  user_strike))
        db.commit()
    

    
    await state.set_state(student.waiting_for_timeBreakfast.state)
    
    

async def timeChooseBreak(message: types.Message, state: FSMContext):
    

    timeBreakfast=message.text.lower()
    user_timeBreakfastHour=timeBreakfast[0:1]
    user_timeBreakfastMinute=timeBreakfast[2:4]
    sql.execute(f'UPDATE profileTel SET timeBreakfastHour = "{user_timeBreakfastHour}" WHERE login = "{login_id}"')
    sql.execute(f'UPDATE profileTel SET timeBreakfastMinute = "{user_timeBreakfastMinute}" WHERE login = "{login_id}"')
    db.commit()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for hour in available_timeLaunch:
        keyboard.add(hour)
    await message.answer(f"Выбери время, когда ты обычно *обедаешь* в будни", reply_markup=keyboard, parse_mode="Markdown")
    await state.set_state(student.waiting_for_timeLaunch.state)

async def timeChooseLaunch(message: types.Message, state: FSMContext):
    timeLaunch=message.text.lower()
    user_timeLaunchHour=timeLaunch[0:2]
    user_timeLaunchMinute=timeLaunch[3:5]
    sql.execute(f'UPDATE profileTel SET timeLaunchHour = "{user_timeLaunchHour}" WHERE login = "{login_id}"')
    sql.execute(f'UPDATE profileTel SET timeLaunchMinute = "{user_timeLaunchMinute}" WHERE login = "{login_id}"')
    db.commit()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for hour in available_timeEvening:
        keyboard.add(hour)
    await message.answer(f"Выбери время, когда ты обычно *ужинаешь* в будни", reply_markup=keyboard, parse_mode="Markdown")
    await state.set_state(student.waiting_for_timeEvening.state)


async def timeChooseEvening(message: types.Message, state: FSMContext):
    timeEvening=message.text.lower()
    user_timeEveningHour=timeEvening[0:2]
    user_timeEveningMinute=timeEvening[3:5]
    sql.execute(f'UPDATE profileTel SET timeEveningHour = "{user_timeEveningHour}" WHERE login = "{login_id}"')
    sql.execute(f'UPDATE profileTel SET timeEveningMinute = "{user_timeEveningMinute}" WHERE login = "{login_id}"')
    db.commit()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for hour in available_timeBreakWeeking:
        keyboard.add(hour)
    await message.answer(f"Выбери время когда ты обычно *завтракаешь* в выходные", reply_markup=keyboard, parse_mode="Markdown")
    await state.set_state(student.waiting_for_timeBreakfastWeeking.state)


async def timeChooseBreakWeeking(message: types.Message, state: FSMContext):
    

    timeBreakfastWeeking=message.text.lower()
    if(timeBreakfastWeeking == "9:30" or timeBreakfastWeeking == "9:45"):
        user_timeBreakfastWeekingHour=timeBreakfastWeeking[0:1]
        user_timeBreakfastWeekingMinute=timeBreakfastWeeking[2:4]
    else:
        user_timeBreakfastWeekingHour=timeBreakfastWeeking[0:2]
        user_timeBreakfastWeekingMinute=timeBreakfastWeeking[3:5]



    sql.execute(f'UPDATE profileTel SET timeBreakfastWeekingHour = "{user_timeBreakfastWeekingHour}" WHERE login = "{login_id}"')
    sql.execute(f'UPDATE profileTel SET timeBreakfastWeekingMinute = "{user_timeBreakfastWeekingMinute}" WHERE login = "{login_id}"')
    db.commit()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for hour in available_timeLaunch:
        keyboard.add(hour)
    await message.answer(f"Выбери время, когда ты обычно *обедаешь* в выходные", reply_markup=keyboard, parse_mode="Markdown")
    await state.set_state(student.waiting_for_timeLaunchWeeking.state)

async def timeChooseLaunchWeeking(message: types.Message, state: FSMContext):
    timeLaunch=message.text.lower()
    user_timeLaunchWeekingHour=timeLaunch[0:2]
    user_timeLaunchWeekingMinute=timeLaunch[3:5]
    sql.execute(f'UPDATE profileTel SET timeLaunchWeekingHour = "{user_timeLaunchWeekingHour}" WHERE login = "{login_id}"')
    sql.execute(f'UPDATE profileTel SET timeLaunchWeekingMinute = "{user_timeLaunchWeekingMinute}" WHERE login = "{login_id}"')
    db.commit()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for hour in available_timeEvening:
        keyboard.add(hour)
    await message.answer(f"Выбери время, когда ты обычно *ужинаешь* в выходные", reply_markup=keyboard, parse_mode="Markdown")
    await state.set_state(student.waiting_for_timeEveningWeeking.state)


async def timeChooseEveningWeeking(message: types.Message, state: FSMContext):
    timeEvening=message.text.lower()
    user_timeEveningWeekingHour=timeEvening[0:2]
    user_timeEveningWeekingMinute=timeEvening[3:5]
    sql.execute(f'UPDATE profileTel SET timeEveningWeekingHour = "{user_timeEveningWeekingHour}" WHERE login = "{login_id}"')
    sql.execute(f'UPDATE profileTel SET timeEveningWeekingMinute = "{user_timeEveningWeekingMinute}" WHERE login = "{login_id}"')
    db.commit()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for hour in available_Ready:
        keyboard.add(hour)
    await message.answer(f"Отлично, нажми готово, чтобы подтвердить твое расписание", reply_markup=keyboard)
    await state.set_state(student.waiting_for_ready.state)


async def readyPeople(message: types.Message, state: FSMContext):
    await dp.bot.send_message(user_id,"Готово")
    schedule_jobs()

async def EatReady(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for hour in available_Eat:
        keyboard.add(hour)
    await message.answer("Ты покушала?", reply_markup=keyboard)
    await state.set_state(student.waiting_for_EatReadyChoose.state)
async def EatReadyChoose(message: types.Message, state: FSMContext):
    global login_id
    login_id=message.from_user.id
    global user_id
    user_id=message.from_user.id
    sql.execute(f"SELECT timeBreakfastHour, timeBreakfastMinute, timeLaunchHour, timeLaunchMinute, timeEveningHour, timeEveningMinute, timeBreakfastWeekingHour, timeBreakfastWeekingMinute, timeLaunchWeekingHour, timeLaunchWeekingMinute, timeEveningWeekingHour, timeEveningWeekingMinute FROM profileTel WHERE login= '{login_id}' ")
    breakfastHour, breakfastMinute,launchHour,launchMinute,eveningHour, eveningMinute,breakfastWeekingHour, breakfastWeekingMinute,launchWeekingHour,launchWeekingMinute,eveningWeekingHour, eveningWeekingMinute=sql.fetchone()
    currentime=datetime.datetime.now()
    currentdate=date.today()
    global allowedBalance, balance
    if(currentdate.weekday() == 0 or currentdate.weekday() == 1 or currentdate.weekday() == 2 or currentdate.weekday() == 3 or currentdate.weekday() == 4 ):    
        if(message.text.lower()== "я позавтракала"):
            
            if( (breakfastMinute+intervalEat)%60 != breakfastMinute+intervalEat):
                if(currentime.hour < (breakfastHour+1) % 24 or currentime.minute <= (breakfastMinute+intervalEat) % 60):
                    await dp.bot.send_message(user_id, "Умница, ты поела вовремя")
                    if(allowedBalance == 1):
                        balance=balance+10
                        sql.execute(f'UPDATE profileTel SET strike = "{balance}" WHERE login = "{login_id}"')
                        db.commit()
                        allowedBalance=0
                        
                else:
                    await dp.bot.send_message(user_id, "К сожалению, ты поела не вовремя")
            if( (breakfastMinute+intervalEat)%60 == breakfastMinute+intervalEat):
                if(currentime.hour <= breakfastHour % 24 and currentime.minute <= (breakfastMinute+intervalEat) % 60):
                    await dp.bot.send_message(user_id, "Умница, ты поела вовремя")
                    if(allowedBalance == 1):
                        balance=balance+10
                        sql.execute(f'UPDATE profileTel SET strike = "{balance}" WHERE login = "{login_id}"')
                        db.commit()
                        allowedBalance=0
                else:
                    await dp.bot.send_message(user_id, "К сожалению, ты поела не вовремя")
        if(message.text.lower()== "я пообедала"):
            
            if( (launchMinute+intervalEat)%60 != launchMinute+intervalEat):
                if(currentime.hour < (launchHour+1) % 24 or currentime.minute <= (launchMinute+intervalEat) % 60):
                    await dp.bot.send_message(user_id, "Умница, ты поела вовремя")
                    if(allowedBalance == 1):
                        balance=balance+10
                        sql.execute(f'UPDATE profileTel SET strike = "{balance}" WHERE login = "{login_id}"')
                        db.commit()
                        allowedBalance=0
                   
                else:
                    await dp.bot.send_message(user_id, "К сожалению, ты поела не вовремя")
                    
            if( (launchMinute+intervalEat)%60 == launchMinute+intervalEat):
                if(currentime.hour <= launchHour % 24 and currentime.minute <= (launchMinute+intervalEat) % 60):
                    await dp.bot.send_message(user_id, "Умница, ты поела вовремя")
                    if(allowedBalance == 1):
                        balance=balance+10
                        sql.execute(f'UPDATE profileTel SET strike = "{balance}" WHERE login = "{login_id}"')
                        db.commit()
                        allowedBalance=0
                    
                else:
                    await dp.bot.send_message(user_id, "К сожалению, ты поела не вовремя")
                    
        if(message.text.lower()== "я поужинала"):
            if( (eveningMinute+intervalEat)%60 != eveningMinute+intervalEat):
                if(currentime.hour < (eveningHour+1) % 24 or currentime.minute <= (eveningMinute+intervalEat) % 60):
                    await dp.bot.send_message(user_id, "Умница, ты поела вовремя")
                    if(allowedBalance == 1):
                        balance=balance+10
                        sql.execute(f'UPDATE profileTel SET strike = "{balance}" WHERE login = "{login_id}"')
                        db.commit()
                        allowedBalance=0
                else:
                    await dp.bot.send_message(user_id, "К сожалению, ты поела не вовремя")
            if( (eveningMinute+intervalEat)%60 == eveningMinute+intervalEat):
                if(currentime.hour <= eveningHour % 24 and currentime.minute <= (eveningMinute+intervalEat) % 60):
                    await dp.bot.send_message(user_id, "Умница, ты поела вовремя")
                    if(allowedBalance == 1):
                        balance=balance+10
                        sql.execute(f'UPDATE profileTel SET strike = "{balance}" WHERE login = "{login_id}"')
                        db.commit()
                        allowedBalance=0
                else:
                    await dp.bot.send_message(user_id, "К сожалению, ты поела не вовремя")




    if(currentdate.weekday() == 5 or currentdate.weekday() == 6 ):    
        if(message.text.lower()== "я позавтракала"):
            
            if( (breakfastWeekingMinute+intervalEat)%60 != breakfastWeekingMinute+intervalEat):
                if(currentime.hour < (breakfastWeekingHour+1) % 24 or currentime.minute <= (breakfastWeekingMinute+intervalEat) % 60):
                    await dp.bot.send_message(user_id, "Умница, ты поела вовремя")
                    if(allowedBalance == 1):
                        balance=balance+10
                        sql.execute(f'UPDATE profileTel SET strike = "{balance}" WHERE login = "{login_id}"')
                        db.commit()
                        allowedBalance=0
                else:
                    await dp.bot.send_message(user_id, "К сожалению, ты поела не вовремя")
            if( (breakfastWeekingMinute+intervalEat)%60 == breakfastWeekingMinute+intervalEat):
                if(currentime.hour <= breakfastWeekingHour % 24 and currentime.minute <= (breakfastWeekingMinute+intervalEat) % 60):
                    await dp.bot.send_message(user_id, "Умница, ты поела вовремя")
                    if(allowedBalance == 1):
                        balance=balance+10
                        sql.execute(f'UPDATE profileTel SET strike = "{balance}" WHERE login = "{login_id}"')
                        db.commit()
                        allowedBalance=0
                else:
                    await dp.bot.send_message(user_id, "К сожалению, ты поела не вовремя")
        if(message.text.lower()== "я пообедала"):
            
            if( (launchWeekingMinute+intervalEat)%60 != launchWeekingMinute+intervalEat):
                if(currentime.hour < (launchWeekingHour+1) % 24 or currentime.minute <= (launchWeekingMinute+intervalEat) % 60):
                    await dp.bot.send_message(user_id, "Умница, ты поела вовремя")
                    if(allowedBalance == 1):
                        balance=balance+10
                        sql.execute(f'UPDATE profileTel SET strike = "{balance}" WHERE login = "{login_id}"')
                        db.commit()
                        allowedBalance=0
                   
                else:
                    await dp.bot.send_message(user_id, "К сожалению, ты поела не вовремя")
                    
            if( (launchWeekingMinute+intervalEat)%60 == launchWeekingMinute+intervalEat):
                if(currentime.hour <= launchWeekingHour % 24 and currentime.minute <= (launchWeekingMinute+intervalEat) % 60):
                    await dp.bot.send_message(user_id, "Умница, ты поела вовремя")
                    if(allowedBalance == 1):
                        balance=balance+10
                        sql.execute(f'UPDATE profileTel SET strike = "{balance}" WHERE login = "{login_id}"')
                        db.commit()
                        allowedBalance=0
                    
                else:
                    await dp.bot.send_message(user_id, "К сожалению, ты поела не вовремя")
                    
        if(message.text.lower()== "я поужинала"):
            if( (eveningWeekingMinute+intervalEat)%60 != eveningWeekingMinute+intervalEat):
                if(currentime.hour < (eveningWeekingHour+1) % 24 or currentime.minute <= (eveningWeekingMinute+intervalEat) % 60):
                    await dp.bot.send_message(user_id, "Умница, ты поела вовремя")
                    if(allowedBalance == 1):
                        balance=balance+10
                        sql.execute(f'UPDATE profileTel SET strike = "{balance}" WHERE login = "{login_id}"')
                        db.commit()
                        allowedBalance=0
                else:
                    await dp.bot.send_message(user_id, "К сожалению, ты поела не вовремя")
            if( (eveningWeekingMinute+intervalEat)%60 == eveningWeekingMinute+intervalEat):
                if(currentime.hour <= eveningWeekingHour % 24 and currentime.minute <= (eveningWeekingMinute+intervalEat) % 60):
                    await dp.bot.send_message(user_id, "Умница, ты поела вовремя")
                    if(allowedBalance == 1):
                        balance=balance+10
                        sql.execute(f'UPDATE profileTel SET strike = "{balance}" WHERE login = "{login_id}"')
                        db.commit()
                        allowedBalance=0
                else:
                    await dp.bot.send_message(user_id, "К сожалению, ты поела не вовремя")

async def balanceCheck(message: types.Message, state: FSMContext):
    global balance
    login_id=message.from_user.id
    sql.execute(f"SELECT strike FROM profileTel WHERE login= '{login_id}' ")
    personStrike=sql.fetchone() 
    balance=personStrike[0]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for hour in available_Present:
        keyboard.add(hour)
    await dp.bot.send_message(login_id, f"*Твой баланс:* {balance}",reply_markup=keyboard, parse_mode="Markdown" )
    await state.set_state(student.waiting_for_buy.state)

async def buy(message: types.Message, state: FSMContext):
    global balance
    login_id=message.from_user.id
    sql.execute(f"SELECT strike FROM profileTel WHERE login= '{login_id}' ")
    personStrike=sql.fetchone()
   
    balance=personStrike[0]
    if(message.text.lower()== f"шоколадка: {prise[0]}"):
        if(balance >= prise[0]):
            balance=balance-prise[0]
            sql.execute(f'UPDATE profileTel SET strike = "{balance}" WHERE login = "{login_id}"')
            db.commit()
            await dp.bot.send_message(login_id, f"Куплена шоколадка \nТвой баланс: {balance}")
        else:
            await dp.bot.send_message(login_id, f"Недостаточно средств")
    if(message.text.lower()== f"большая шоколадка: {prise[1]}"):
        if(balance >= prise[1]):
            balance=balance-prise[1]
            sql.execute(f'UPDATE profileTel SET strike = "{balance}" WHERE login = "{login_id}"')
            db.commit()
            await dp.bot.send_message(login_id, f"Куплена большая шоколадка \nТвой баланс: {balance}")
        else:
            await dp.bot.send_message(login_id, f"Недостаточно средств")
    if(message.text.lower()== f"ужин: {prise[2]}"):
        if(balance >= prise[2]):
            balance=balance-prise[2]
            sql.execute(f'UPDATE profileTel SET strike = "{balance}" WHERE login = "{login_id}"')
            db.commit()
            await dp.bot.send_message(login_id, f"Куплен ужин \nТвой баланс: {balance}")
        else:
            await dp.bot.send_message(login_id, f"Недостаточно средств")
    if(message.text.lower()== f"секретный подарок: {prise[3]}"):
        if(balance >= prise[3]):
            balance=balance-prise[3]
            sql.execute(f'UPDATE profileTel SET strike = "{balance}" WHERE login = "{login_id}"')
            db.commit()
            await dp.bot.send_message(login_id, f"Куплен секретный подарок \nТвой баланс: {balance}")
        else:
            await dp.bot.send_message(login_id, f"Недостаточно средств")
    if(message.text.lower()== f"день послушности: {prise[4]}"):
        if(balance >= prise[4]):
            balance=balance-prise[4]
            sql.execute(f'UPDATE profileTel SET strike = "{balance}" WHERE login = "{login_id}"')
            db.commit()
            await dp.bot.send_message(login_id, f"Куплен день послушности \nТвой баланс: {balance}")
        else:
            await dp.bot.send_message(login_id, f"Недостаточно средств")
            


    

async def timeMessageBreakfast(dp: Dispatcher):
    Zahle=random.randint(0, 20)
    await dp.bot.send_message(user_id, f"Время завтракать, {nettName[Zahle]}! Приятного аппетита! 💞✨ \nНажми /ready , когда покушаешь")
    global allowedBalance
    allowedBalance=1


async def timeMessageLaunch(dp: Dispatcher):
    Zahle=random.randint(0, 20)
    await dp.bot.send_message(user_id, f"Время обедать, {nettName[Zahle]}! Приятного аппетита!💖✨ \nНажми /ready , когда покушаешь")
    global allowedBalance
    allowedBalance=1
    

async def timeMessageEvening(dp: Dispatcher):
    Zahle=random.randint(0, 20)
    await dp.bot.send_message(user_id, f"Время ужинать, {nettName[Zahle]} ! Приятного аппетита!💗✨ \nНажми /ready , когда покушаешь")
    global allowedBalance
    allowedBalance=1
    
    
    

scheduler = AsyncIOScheduler()


def schedule_jobs():
    
    sql.execute(f"SELECT timeBreakfastHour, timeBreakfastMinute, timeLaunchHour, timeLaunchMinute, timeEveningHour, timeEveningMinute, timeBreakfastWeekingHour, timeBreakfastWeekingMinute, timeLaunchWeekingHour, timeLaunchWeekingMinute, timeEveningWeekingHour, timeEveningWeekingMinute FROM profileTel WHERE login= '{login_id}' ")
    breakfastHour, breakfastMinute,launchHour,launchMinute,eveningHour, eveningMinute,breakfastWeekingHour, breakfastWeekingMinute,launchWeekingHour,launchWeekingMinute,eveningWeekingHour, eveningWeekingMinute=sql.fetchone()
    scheduler.add_job(timeMessageBreakfast, "cron",day_of_week='mon-fri', hour=breakfastHour, minute=breakfastMinute, args=(dp,))
    scheduler.add_job(timeMessageLaunch, "cron",day_of_week='mon-fri', hour=launchHour, minute=launchMinute, args=(dp,))
    scheduler.add_job(timeMessageEvening, "cron",day_of_week='mon-fri', hour=eveningHour, minute=eveningMinute, args=(dp,))
    scheduler.add_job(timeMessageBreakfast, "cron",day_of_week='sat-sun', hour=breakfastWeekingHour, minute=breakfastWeekingMinute, args=(dp,))
    scheduler.add_job(timeMessageLaunch, "cron",day_of_week='sat-sun', hour=launchWeekingHour, minute=launchWeekingMinute, args=(dp,))
    scheduler.add_job(timeMessageEvening, "cron",day_of_week='sat-sun', hour=eveningWeekingHour, minute=eveningWeekingMinute, args=(dp,))

    


    



def register_handlers_student(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(EatReady, commands="ready", state="*")
    dp.register_message_handler(balanceCheck, commands="balance", state="*")
    dp.register_message_handler(timeChooseBreak, state=student.waiting_for_timeBreakfast)
    dp.register_message_handler(timeChooseLaunch, state=student.waiting_for_timeLaunch)
    dp.register_message_handler(timeChooseEvening, state=student.waiting_for_timeEvening)
    dp.register_message_handler(timeChooseBreakWeeking, state=student.waiting_for_timeBreakfastWeeking)
    dp.register_message_handler(timeChooseLaunchWeeking, state=student.waiting_for_timeLaunchWeeking)
    dp.register_message_handler(timeChooseEveningWeeking, state=student.waiting_for_timeEveningWeeking)
    dp.register_message_handler(EatReadyChoose, state=student.waiting_for_EatReadyChoose)
    dp.register_message_handler(readyPeople, state=student.waiting_for_ready)
    dp.register_message_handler(buy, state=student.waiting_for_buy)
    dp.register_message_handler(timeMessageBreakfast, state="*")
    dp.register_message_handler(timeMessageLaunch, state="*")
    dp.register_message_handler(timeMessageEvening, state="*")




logger = logging.getLogger(__name__)


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command="/ready", description="Я поела"),
        types.BotCommand(command="/start", description="Старт"),
        types.BotCommand(command="/balance", description="Мой баланс"),
        
    ]
    
    await bot.set_my_commands(commands)


async def main():
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    
    logger.error("Starting bot")
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage())
    register_handlers_student(dp)
    scheduler.start()
    await set_commands(bot)
    await dp.start_polling()
    
 

if __name__ == '__main__':
    asyncio.run(main())
    
