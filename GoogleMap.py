from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time,csv

class googleMapScraper:
    def __init__(self) -> None:
        pass

    def openBrowser(self):
        # driverPath = ChromeDriverManager().install()
        servc = Service()
        driver = 'None'

    
    def userSearch(self):
        inputSearch = input('enter your search:- ')
        querry = f"{'https://www.google.com/search?q='}{inputSearch}"
        userSearch = '+'.join(querry.split())

    
    def scrollDown(self,driver,endpoint):
        for page in range(endpoint):
            body = driver.find_element(By.TAG_NAME, 'body')
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)

    def getPageResp(self,driver,userSearch):
        driver.get(userSearch)
        endPoint = 1
        self.scrollDown(driver,endPoint)
        time.sleep(1)
        xpath = '//span[contains(text(),"More places")]'
        element = driver.find_element(By.XPATH,xpath)
        element.click()
        time.sleep(1)
  
        boxesTag = driver.find_elements(By.XPATH,'//div[@class="rl_tile-group"]//div[@jscontroller]/div[@jscontroller]')
        self.parseData(driver,boxesTag)

    def parseData(self,driver,boxesTag):
        for box in boxesTag:
            box.click()
            time.sleep(5)
            endpoint = 1
            self.scrollDown(driver,endpoint)
            try: title = driver.find_element(By.XPATH,'//h2[@data-attrid="title"]').text.strip()
            except: title = 'None'
            try: ratting = driver.find_element(By.XPATH,'//span[@class="fzTgPe Aq14fc"]').text.strip()
            except: ratting = 'None'
            try: reviews = driver.find_element(By.XPATH,'//span[@style][contains(text(),"reviews")]/parent::span').get_attribute('innerText').strip()
            except: reviews = 'None'
            try: websiteLink = driver.find_element(By.XPATH,'//a[@class="mI8Pwc"]').get_attribute('href')
            except: websiteLink = 'None'
            try: locatedIn = driver.find_element(By.XPATH,'//span[contains(text(),"Located in:")]/parent::div/a').get_attribute('textContent').strip()
            except: locatedIn = 'None'
            try: address = driver.find_element(By.XPATH,'//span[@class="LrzXr"]').get_attribute('textContent').strip()
            except: address = 'None'
            try: openClosetime = driver.find_element(By.XPATH,'//span[@class="TLou0b"]//span').get_attribute('innerText').replace('\u202f','').strip()
            except: openClosetime = 'None'
            try: phoneNumber = driver.find_element(By.XPATH,'//span[contains(@aria-label,"Call phone number")]').get_attribute('textContent').strip()
            except: phoneNumber = 'None'
            try: totalPhotos = driver.find_element(By.XPATH,'//span[contains(text(),"Photos")]/parent::button/span').text.strip()
            except: totalPhotos = 'None'
            try: workName = driver.find_element(By.XPATH,'//span[@class="YhemCb"]').text.strip()
            except: workName = 'None'
            try: questions = driver.find_element(By.XPATH,'//span[contains(text(),"questions ")]').text.strip()
            except: questions = 'None'
            try: shortDescription = driver.find_element(By.XPATH,'//div[@jsname="EvNWZc"]').text.strip()
            except: shortDescription = 'None'
            try: 
                profilesTag = driver.find_elements(By.XPATH,'//g-link/a')
                profiles = [tag.get_attribute('href') for tag in profilesTag]
            except: profiles = 'None'
            try: 
                webResultTag = driver.find_elements(By.XPATH,'//cite/parent::div/a')
                webResult = [tag.get_attribute('href') for tag in webResultTag]
            except: webResult = 'None'
            try: serviceOptions = driver.find_element(By.XPATH,'//span[contains(text(),"Service options:")]/parent::div').get_attribute('innerText').replace('\xa0','').strip()
            except: serviceOptions = 'None'
            try: areaServed = driver.find_element(By.XPATH,'//div[contains(text(),"Areas served:")]/parent::div').get_attribute('innerText').replace('\xa0','').strip()
            except: areaServed = 'None'
            row = [title,workName,ratting,reviews,websiteLink,locatedIn,address,areaServed,serviceOptions,phoneNumber,totalPhotos,openClosetime,questions,profiles,webResult,shortDescription]
            print(f"[Info] Getting Company Name:- {title}")
    
    def saveData(self,row):
        with open(file='GoogleMapData.csv',mode='a',newline='',encoding='UTF-8') as file:
            csv.writer(file).writerow(row)

    def header(self):
        header = ['Title','Work Name','Ratting','Reviews','Website Link','Located In','Address','Area Served','Service Options','Phone Number','Total Photos','Open or Close Time','Questions','Profiles','Web Result','Short Description']
        with open(file='GoogleMapData.csv',mode='w',newline='') as file:
            csv.writer(file).writerow(header)

    def run(self):
        userSearch = self.userSearch()
        driver = self.openBrowser()
        self.getPageResp(driver,userSearch)

myClass = googleMapScraper()
open(file='GoogleMapData.txt',mode='w').close()
print(f"\n[Info] Do you want to delete all data and add new data! ")
answer = input('enter your decision (y/n):- ')
if answer == 'y':
    myClass.header()
else:
    myClass.header()
