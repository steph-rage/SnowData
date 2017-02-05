import requests

from bs4 import BeautifulSoup

page = []


#Year counts the number of years since 1981, the first available year with data
#for year in range(1981, 2017):
#
#	POST_data = {'sitenum':'515', 'report':'STAND', 'timeseries':'Hourly', 'interval':'YEAR='+str(year), 'temp_unit':'8', 'format':'view', 'autoscale':'false', 'legendpos':'right', 'userEmail':'', 'intervalDirection':'-'}
#	page.append(requests.post('https://wcc.sc.egov.usda.gov/nwcc/view', POST_data))

POST_data = {'sitenum':'515', 'report':'STAND', 'timeseries':'Hourly', 'interval':'YEAR=1981', 'temp_unit':'8', 'format':'view', 'autoscale':'false', 'legendpos':'right', 'userEmail':'', 'intervalDirection':'-'}
page = requests.post('https://wcc.sc.egov.usda.gov/nwcc/view', POST_data)


soup = BeautifulSoup(page.text, "html5lib")

table_cells = soup.find_all('td')

print(table_cells)