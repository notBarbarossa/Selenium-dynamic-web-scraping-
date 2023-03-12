from bs4 import BeautifulSoup
from user_agent import generate_user_agent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import lxml
import time

url = "https://www.youtube.com/@britneyspears/videos"
agent = generate_user_agent(device_type="desktop")

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={agent}")
options.add_argument("--disable-blink-features=AutomationControlled")

driver_service = Service(executable_path="D:\PyCharm\PROJECTS\Sds\webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service, options=options)

try:
    """"""
    driver.get(url=url)
    time.sleep(5)

    for i in range(7):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(2)

    with open("britney.html", "w", encoding="utf-8") as file:
        file.write(driver.page_source)
    time.sleep(2)

    with open("britney.html", "r", encoding="utf-8") as file2:
        src = file2.read()

    soup = BeautifulSoup(src, "lxml")

    block = soup.find("div", id="contents", class_="style-scope ytd-rich-grid-renderer")
    data = block.find_all("ytd-rich-grid-row", class_="style-scope ytd-rich-grid-renderer")

    for i in data:
        name = i.find("h3", class_="style-scope ytd-rich-grid-media").text
        print(name)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
