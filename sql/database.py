import sqlite3

connection = sqlite3.connect("game.db")

cursor = connection.cursor()

user_input = input("Přidej postavičku do databáze:")
class_input = input("Přidej classu k postavičce:")

cursor.execute("INSERT INTO characters (name, class) VALUES (?, ?)" ,(user_input, class_input))


connection.commit()

cursor.execute("SELECT * FROM characters")
rows = cursor.fetchall()

# for row in rows:
#     print(row)

connection.close()