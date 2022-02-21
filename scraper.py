import requests
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = requests.get(url=START_URL)
time.sleep(10)

def scraper():
    header = ["Name","Distance","Mass","Radius"]
    planet_data=[]
    for i in range(0,100):
        soup = BeautifulSoup(browser.content,features="html.parser")
        for tr_tag in soup.find_all("tr"):
            td_tags = soup.find_all("td")
            temp_list = []
            for index,td_tag in enumerate(td_tags):
                if index == 1:
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
    with open("scraper_2.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(header)
        csvwriter.writerow(planet_data)

scraper()

         
