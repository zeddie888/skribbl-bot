
"""
STATUS:
PART 1- obtain words from github, DONE
PART 2- separate words, WIP, DONE
"""


####################### PART 1 ################################
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://skribbliohints.github.io/")

f = open("skribbl_words.txt", "w+")

words = WebDriverWait(driver, 15).until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//div[@class='b']"))
)

for word in words:
    f.write(word.text)
    f.write('\n')


print("DONE")
f.close()
driver.close()

"""


"""

###### PART 2 ############

f3 = open("letters3.txt", "w+")
f4 = open("letters4.txt", "w+")
f5 = open("letters5.txt", "w+")
f6 = open("letters6.txt", "w+")
f7 = open("letters7.txt", "w+")
f8 = open("letters8.txt", "w+")
f9 = open("letters9.txt", "w+")
f10 = open("letters10.txt", "w+")
f11 = open("letters11.txt", "w+")
f12 = open("letters12.txt", "w+")
f13 = open("letters13.txt", "w+")

f = open("skribbl_words.txt")
words = list(f.read().split("\n"))
for word in words:
    a = len(word)
    if a == 3:
        f3.write(word)
        f3.write("\n")
    if a == 4:
        f4.write(word)
        f4.write("\n")
    if a == 5:
        f5.write(word)
        f5.write("\n")
    if a == 6:
        f6.write(word)
        f6.write("\n")
    if a == 7:
        f7.write(word)
        f7.write("\n")
    if a == 8:
        f8.write(word)
        f8.write("\n")
    if a == 9:
        f9.write(word)
        f9.write("\n")
    if a == 10:
        f10.write(word)
        f10.write("\n")
    if a == 11:
        f11.write(word)
        f11.write("\n")
    if a == 12:
        f12.write(word)
        f12.write("\n")
    if a == 13:
        f13.write(word)
        f13.write("\n")
