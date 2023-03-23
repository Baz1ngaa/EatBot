import sqlite3
db=sqlite3.connect('EatYuliia.db')
sql=db.cursor()

db.commit()
#user_id="121"
#user_region="europa"
#user_klass="11"

#sql.execute(f"SELECT login FROM profileTel WHERE login = '{user_id}'")
#if sql.fetchone() is None:
 #   sql.execute(f"INSERT INTO profileTel VALUES (?,?,?)", (user_id, user_region, user_klass))
  #  db.commit()
nuwmerUsers=0
for value in sql.execute("SELECT * FROM profileTel"):
    nuwmerUsers=nuwmerUsers+1
    print(value)
print("Всего пользователей:", nuwmerUsers)