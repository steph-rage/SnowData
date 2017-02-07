import requests
import sqlite3

from bs4 import BeautifulSoup

#NOTE: for some reason the year is off by one. Putting '1981' in the POST data gives 
#values from 1980.


snow_db = sqlite3.connect('snow-database.db')
snow_db.execute('CREATE TABLE snow_level (day DATE, snow_level INT, season BLOB)')


for year in range(1980, 2017):

	POST_data = {'sitenum':'515', 'report':'STAND', 'timeseries':'Daily', 'interval':'YEAR='+str(year), 'temp_unit':'8', 'format':'view', 'autoscale':'false', 'legendpos':'right', 'userEmail':'', 'intervalDirection':'-'}
	page = requests.post('https://wcc.sc.egov.usda.gov/nwcc/view', POST_data)

	soup = BeautifulSoup(page.text, "html5lib")
	table_cells = soup.find_all('td')

	for i in range(len(table_cells)):
		if str(year - 1) in table_cells[i].text:
			snow_db.execute('INSERT INTO snow_level (day, snow_level) VALUES (?, ?)', (table_cells[i].text, table_cells[i+2].text))

snow_db.execute('DELETE FROM snow_level WHERE snow_level IS -99.9')
snow_db.execute('DELETE FROM snow_level WHERE day LIKE "%Washington%"')

for year in range(1980, 2017):
	season = str(year)[2:] + "-" + str(year + 1)[2:]
	start_date = str(year) + "-08-25"
	end_date = str(year + 1) + "-08-26"
	snow_db.execute('UPDATE snow_level SET season = ? WHERE day BETWEEN ? AND ?', (season, start_date, end_date))


snow_db.commit()
snow_db.close()
