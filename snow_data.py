import requests
import sqlite3

from bs4 import BeautifulSoup

#NOTE: for some reason the year is off by one. Putting '1981' in the POST data gives 
#values from 1980.


snow_db = sqlite3.connect('snow-database.db')
snow_db.execute('CREATE TABLE snow_level (DAY date, SNOW_LEVEL int)')


for year in range(1980, 2017):

	POST_data = {'sitenum':'515', 'report':'STAND', 'timeseries':'Daily', 'interval':'YEAR='+str(year), 'temp_unit':'8', 'format':'view', 'autoscale':'false', 'legendpos':'right', 'userEmail':'', 'intervalDirection':'-'}
	page = requests.post('https://wcc.sc.egov.usda.gov/nwcc/view', POST_data)

	soup = BeautifulSoup(page.text, "html5lib")
	table_cells = soup.find_all('td')

	for i in range(len(table_cells)):
		if str(year - 1) in table_cells[i].text:
			snow_db.execute('INSERT INTO snow_level VALUES (?, ?)', (table_cells[i].text, table_cells[i+3].text))


snow_db.commit()
snow_db.close()
