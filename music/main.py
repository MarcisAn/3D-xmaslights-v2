import time

from selenium import webdriver
import random
from selenium.webdriver.firefox.options import Options

options = Options()
#options.headless = True
driver = webdriver.Firefox(options=options)

driver.get("https://studio.moises.ai/login")
time.sleep(3)
driver.find_element("xpath", "/html/body/div/div/div/div/div[2]/div/div/div[2]/form/div[1]/div/input").send_keys("marcis-andersons@inbox.lv")
driver.find_element("xpath", "/html/body/div/div/div/div/div[2]/div/div/div[2]/form/div[2]/div/input").send_keys("marcis030506")
driver.find_element("xpath", "/html/body/div/div/div/div/div[2]/div/div/div[2]/form/button").click()
time.sleep(1)
driver.find_element("xpath", "https://studio.moises.ai/upload/split/")



