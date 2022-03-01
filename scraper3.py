import requests
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = requests.get(START_URL)
time.sleep(10)

soup = bs(browser.text,"html.parser")
star_table = soup.find("table")

temp_list=[]
table_rows = star_table.find_all("tr")
for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    print(row)
    temp_list.append(row)

star_names = []
distance = []
mass=[]
radius=[]
lum=[]

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    lum.append(temp_list[i][7])

df = pd.DataFrame(list(zip(star_names,distance,mass,radius,lum)),columns=['star_name',"distance","mass","radius","luminosity"])

df.to_csv("star_data.csv")
