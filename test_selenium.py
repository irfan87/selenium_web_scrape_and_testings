# import selenium library and set the path of chromedriver.exe live
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://books.toscrape.com/")

print(driver.title)

driver.quit()
