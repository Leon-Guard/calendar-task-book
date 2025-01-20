#!/usr/bin/python3
import sqlite3

class DataBase:
	def __init__(self):
		''' Первый запуск. Инициализируем нужные обьекты и создаем таблицу если ее нет. '''
		self.db = "zadachik_baze.db"
		self.conn = sqlite3.connect(self.db)
		self.cursor
		 = conn.cursor()

		self.cursor.execute('''
		CREATE TABLE IF NOT EXISTS Панель (
			id INTEGER PRIMARY KEY,
			имя TEXT NOT NULL
		);
		''')
		self.cursor.execute('''
		CREATE TABLE IF NOT EXISTS Категория (
			id INTEGER PRIMARY KEY,
			имя TEXT NOT NULL,
			цвет TEXT NOT NULL
		);
		''')
		self.cursor.execute('''
		CREATE TABLE IF NOT EXISTS Реакция (
			id INTEGER PRIMARY KEY,
			имя TEXT NOT NULL
		);
		''')
		self.cursor.execute('''
		CREATE TABLE IF NOT EXISTS Коментарий (
			id INTEGER PRIMARY KEY,
			id_задачи INTEGER, NOT NULL
			содержание TEXT NOT NULL,
			реакция INTEGER,
			FOREIGN KEY (реакция) REFERENCES Реакция (id)
		);
		''')
		self.cursor.execute('''
		CREATE TABLE IF NOT EXISTS Задача (
			id INTEGER PRIMARY KEY,
			название TEXT NOT NULL,
			описание TEXT NOT NULL,
			коментарий INTEGER,
			реакция INTEGER,
			категория INTEGER,
			конечная_дата INTEGER,
			прогресс INTEGER NOT NULL,
			FOREIGN KEY (категория) REFERENCES Категория (id),
			FOREIGN KEY (реакция) REFERENCES Реакция (id),
			FOREIGN KEY (коментарий) REFERENCES Коментарий (id)
		)
		''')
		self.conn.commit()

	def open():
		''' Открыть БД '''
		self.conn = sqlite3.connect(self.db)

	def save():
		''' Сохранить изменения '''
		self.conn.commit()

	def close():
		''' Закрыть БД '''
		self.conn.close()


	def add_task(s1, s2):
		'''	Добавить задачу. '''
		self.cursor.execute('\
			INSERT INTO Задача (название, описание, прогресс) VALUES (?, ?)',
			(s1, s2, 0))
		self.conn.commit()

	def add_kateg():
		'''	Добавить коментарий. '''
		self.cursor.execute('''
			INSERT INTO Коментарий ()
		''')
		self.conn.commit()

	def edit_task():
		''' Изменить задачу. '''
		pass

	def delete_task():
		'''  '''
		pass

	def duble_task():
		'''  '''
		pass

	def switch_view():
		'''  '''
		pass

	def add_comment():
		'''  '''
		pass

	def add_react():
		'''  '''
		pass

	def output():
		'''  '''
		pass


