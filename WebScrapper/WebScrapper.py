#import time
#from selenium import webdriver
#url = "https://supertote.mu/racing"
#driver = webdriver.Firefox(executable_path=r"geckodriver.exe")
#driver.get(url)
##driver.execute_script("window.scrollTo(0,5000)")
##time.sleep(10)

#tds = driver.

#for td in tds:
#    print (td.text)
    

##MyClass
#class powercutregion:
#    day = ""
#    date = ""
#    region = ""
#    road = ""

#mypowercutregion = powercutregion()

import urllib3
from bs4 import BeautifulSoup
http = urllib3.PoolManager()

url = "https://supertote.mu/racing"
response = http.request('GET', url)
soup = BeautifulSoup(response.data)
all_links = soup.find_all('a', 'race-info')
for link in all_links:
    print (link)