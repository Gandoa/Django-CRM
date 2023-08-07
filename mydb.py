import mysql.connector

dataBase = mysql.connector.connect(
		host = 'localhost',
		user = 'Gando',
		passwd = 'Marseille10@'

	)



cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE elderco")

print('ALL DONE !')