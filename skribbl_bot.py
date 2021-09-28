"""
STATUS: WIP

Bot is intended for use in private room only
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

# Change this
link = input("Paste link")
driver.get(link)

playButton = driver.find_element_by_xpath("//button[text()='Play!']")
playButton.click()

waitStart = input("Enter once host starts")

chat = WebDriverWait(driver, 120).until(
    EC.presence_of_element_located(
        (By.XPATH, "//input[@id = 'inputChat']"))
)

while(True):
    gameWIN = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@id='overlay'][contains(@style, 'opacity')]"))
    )

    gameDetector = gameWIN.get_attribute('style')

    currentWord = None
    while(currentWord is None or len(target) == 0):
        currentWord = driver.find_element_by_xpath(
            "//div[@id = 'currentWord']")
        target = currentWord.text

    f = open(f"letters{len(target)}.txt")
    words = list(f.read().split("\n"))

    #i = math.ceil(len(words) / N)
    i = 0
    while gameDetector.__contains__('0'):
        shouldContinue = False
        word = words[i]

        currentWord = driver.find_element_by_xpath(
            "//div[@id = 'currentWord']")
        target = currentWord.text

        for pos, letter in enumerate(word):
            if letter != target[pos] and target[pos] != '_':
                shouldContinue = True
                break

        i = (i+1) % len(words)
        if shouldContinue:
            continue
        chat.clear()
        chat.send_keys(word)
        chat.send_keys(Keys.ENTER)

        gameWIN = driver.find_element_by_xpath(
            "//div[@id='overlay'][contains(@style, 'opacity')]")
        gameDetector = gameWIN.get_attribute('style')

        time.sleep(1)


"""TODO

1. If word length is > 13, then make a new file and add the word to it
2. Add word to list if not in list


"""
