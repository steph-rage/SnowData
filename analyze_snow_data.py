import sqlite3

snow_db = sqlite3.connect('snow-database.db')

cursor = snow_db.cursor()

data = cursor.execute("SELECT day, MAX(snow_level), season FROM snow_level GROUP BY season")

print "Date that Max Level of Snow is Reached:"
print "---------------------------------------"
print "Date          Max Snow Level       Season"
for _ in range(33):
	current = data.fetchone()
	print("{}          {}          {}".format(current[0], current[1], current[2]))

snow_db.commit()
snow_db.close()