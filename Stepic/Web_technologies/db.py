# Подключение к базе 
import MySQLdb


db = MySQLdb.connect(host='localhost', user='joe', 
	passwd='moonpie', db='thangt')

cursor = db.cursor()
# Запросы с использованием cursor
db.commit()
db.close()

# Выполнение запросов

cursor.execute("""
	update users set age = age + 1 where name = %s
	""", (name,))

cursor.execute("select * from users")
users = cursor.fetchall() # Получает все строки сразу
# Используется когда немного строк

cursor.execute("""
	select * from users where name = %s 
	""", (name,))
user = cursor.fetchone() # ПОлучить одно значение

# Вставка многих записей 

cursor.executemany(
	"INSERT INTO users (name, age) VALUE (%s, %s)"
	[
		('Igor', 18 ),
		('Petr', 16 ),
	]
)
db.commit()
db.close()

# Placeholders

email = "' OR '1' = '1"

cursor.execute(
	"SELECT * FROM users WHERE email = '%" + email + "'",
) # Грозит sql инъекцией 

cursor.execute(
	"SELECT * FROM users WHERE email = '%s'",
	email
)

# Базы данных в django

from django.db import connection, connections


cur = connection.cursor()
cur.execute("select * rfom tbl limit 10")

default_cur = connections['default'].cursor() 	# Выполняем соединение
default_cur.execute("select * from tbl2 limit 10") 	# Делаем запрос
another_cur = connections['another'].cursor()
another_cur.execute("select * from tbl2 limit 10")
