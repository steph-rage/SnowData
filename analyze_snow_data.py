import sqlite3

snow_db = sqlite3.connect('snow-database.db')

cursor = snow_db.cursor()

data = cursor.execute("SELECT day, MAX(snow_level), season FROM snow_level GROUP BY season")

print "Date that Max Level of Snow is Reached:"
print "---------------------------------------"
print "Date        Snow Level       Season"
for _ in range(34):
	print data.fetchone()

snow_db.commit()
snow_db.close()