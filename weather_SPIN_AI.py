import sys

from Extensions.TKDataAccess import TKDataAccess

dataAccess = TKDataAccess()
connectionStatus = dataAccess.Connect("127.0.0.1:3101", "guest", "")
   

ret = dataAccess.GetObjectValue("Tag.tag100")

	
 

 

from bs4 import BeautifulSoup
import requests
city = str(ret)
city = city+" weather"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
 
 

city = city.replace(" ", "+")
res = requests.get(
    f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
print("Searching...\n")
soup = BeautifulSoup(res.text, 'html.parser')
location = soup.select('#wob_loc')[0].getText().strip()
time = soup.select('#wob_dts')[0].getText().strip()
info = soup.select('#wob_dc')[0].getText().strip()
weather = soup.select('#wob_tm')[0].getText().strip()
aa=str(location)
bb=str(time)
cc=str(info)
dd=str(weather+"°C")
ff=str(weather)
 
dataAccess.SetObjectValue("Tag.tag200", aa) 
dataAccess.SetObjectValue("Tag.tag201", bb) 
dataAccess.SetObjectValue("Tag.tag202", cc) 
dataAccess.SetObjectValue("Tag.tag203", dd) 
dataAccess.SetObjectValue("Tag.tag204", ff) 
# This code is contributed by adityatri