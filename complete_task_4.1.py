# Домашнее задание на SQL



# Этап 1.1 В базе данных teacher создайте таблицу Students. 

# import sqlite3
# connection = sqlite3.connect ('teacher.db')
# cursor = connection.cursor()

# sqlquery = """CREATE TABLE Students
# (Student_Id INTEGER PRIMARY KEY,
# Student_Name TEXT,
# School_Id INTEGER);"""

# cursor.execute(sqlquery)
# connection.commit()



# Этап 1.2. Добавили еще одну таблицу с информацией о школах.

# import sqlite3
# connection = sqlite3.connect ('teacher.db')
# cursor = connection.cursor()

# sqlquery = """CREATE TABLE School
# (School_Id INTEGER PRIMARY KEY,
# School_Name TEXT,
# Place_Count INTEGER);"""

# cursor.execute(sqlquery)
# connection.commit()



# Этап 2.1. Наполните таблицу следующими данными о студентах.

# import sqlite3
# connection = sqlite3.connect ('teacher.db')
# cursor = connection.cursor()

# sqlquery = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
# VALUES 
# ('201', 'Иван', '1'), 
# ('202', 'Петр', '2'),
# ('203', 'Анастасия', '3'),
# ('204', 'Игорь', '4');"""

# cursor.execute(sqlquery)
# connection.commit()



# Этап 2.2. Наполнили таблицу данными о школах:

# import sqlite3
# connection = sqlite3.connect ('teacher.db')
# cursor = connection.cursor()

# sqlquery = """INSERT INTO School (School_Id, School_Name, Place_Count)
# VALUES 
# ('1', 'Протон', '200'), 
# ('2', 'Перспектива', '300'),
# ('3', 'Спектр', '400'),
# ('4', 'Содружество', '500');"""

# cursor.execute(sqlquery)
# connection.commit()



# Этап 3. Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.
# Формат вывода:
# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3

def get_connection():
  connection = sqlite3.connect('teacher.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_info_student(student_id):
    try:
      con = get_connection()
      cursor = con.cursor()
      sqlquery = 'SELECT * FROM Students JOIN School ON Students.School_Id = School.School_Id WHERE Student_Id = ?'
      cursor.execute (sqlquery, (student_id,))
      student_info = cursor.fetchall()
      for row in student_info:
        print('ID Студента: ', row[0])
        print('Имя студента: ', row[1])
        print('ID школы: ', row[2])
        print('Название школы: ', row[4])
        close_connection(con)
    except (Exception, sqlite3.Error) as error:
      print ('Ошибка вида', error)

get_info_student(201)