from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import time
import openpyxl as excel
import keyboard
import openpyxl as excel
import pyautogui,time


# function to read contacts from a text file
def readContacts(fileName):
    lst = []
    file = excel.load_workbook(fileName)
    sheet = file.active
    firstCol = sheet['A']
    for cell in range(len(firstCol)):
        contact = (firstCol[cell].value).encode('utf-8')
        lst.append(contact)
    return lst


targets = readContacts("tt.xlsx")

driver = webdriver.Chrome('./chromedriver')
driver.get("https://web.whatsapp.com/")
input(" Hit Enter ")
wait = WebDriverWait(driver, 600)
wait5 = WebDriverWait(driver, 5)
pyautogui.keyDown('alt')
time.sleep(.2)
pyautogui.press('tab')
time.sleep(2)
pyautogui.keyUp('alt')
groupname="Test group"
i=1
for target in targets : 
    driver.find_element_by_xpath('//*[@title="Menu"]').click()# header > div.sbcXq > div > span > div:nth-child(3) > div
    driver.find_element_by_xpath('//*[@title="New group"]').click()
    pyautogui.typewrite(target.decode('utf-8'))
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.typewrite(groupname+str(i))
    pyautogui.press('enter')
    driver.refresh()
    i=i+1
    time.sleep(10)
driver.close()
