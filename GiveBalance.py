


import sqlite3




db=sqlite3.connect('EatYuliia.db')
sql=db.cursor()
for value in sql.execute("SELECT * FROM profileTel"):
    print(value)
login_id=input("ID: ")
newbalance=input("Баланс: ")
sql.execute(f'UPDATE profileTel SET strike = {int(newbalance)} WHERE login = "{int(login_id)}"')
db.commit()