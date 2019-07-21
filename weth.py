import requests 
import bs4
from colorama import *
init(autoreset = True)
while True:
	location = input("Input  any Country/State/City to get weather info >  ")
	header = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
	rq = requests.get("http://www.google.com/search",params={'q':f"{location} weather"},headers=header)
	soup = bs4.BeautifulSoup(rq.text , "html.parser")
	try:
		loc = soup.find('div' , {'id' : 'wob_loc'})
		temp = soup.find('span' , {'id' : 'wob_tm'})
		time = soup.find('div' , {'id' : 'wob_dts'})
		stat = soup.find('div' , {'id' : 'wob_dcp'})
		prec = soup.find('span' , {'id' : 'wob_pp'})
		hum = soup.find('span' , {'id' : 'wob_hm'})
		wis = soup.find('span' , {'id' : 'wob_ws'})		
		print("\n")
		print("LOCATION : " +loc.text)
		print("TEMPRATURE : "+temp.text)
		print("WEATHER UPDATED ON : " +time.text)
		print(stat.text)
		print("\n")
		print(f"To see full weather info of {location} location press ENTER or press Ctrl+z to exit \n")
		input(' ?> ')
		
		print("\n")
		print("LOCATION : " +loc.text)
		print("TEMPRATURE : "+temp.text)
		print("WEATHER UPDATED ON : " +time.text)
		print("PRECIPITATION :" + prec.text)
		print("HUMIDITY :" + hum.text)
		print("WINDSPEED :" + wis.text) 
		print(stat.text)
	except:
		print(Back.RED +f"{location} is not a valid location ")
		print("\n")