"""
STATUS: WIP
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import threading


PATH = "C:\Program Files (x86)\chromedriver.exe"
# driver = webdriver.Chrome(PATH)

# driver.get("https://skribbl.io/?0ddyJUDBGjJI")

# f = open("words.txt")
# words = list(f.read().split("\n"))


def test_logic(id):

    print(f"PRINT THIS: {id}")

    driver = webdriver.Chrome(PATH)
    driver.get("https://skribbl.io/?bWyfz9xjEBjZ")
    # Implement your test logic
    playButton = driver.find_element_by_xpath("//button[text()='Play!']")

    playButton.click()

    chat = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id = 'inputChat']"))
    )
    # print(chat)

    # toGuess = WebDriverWait(driver, 60).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "//div[@id='currentWord']"))
    # )

    while(True):
        #checkpoint = input("Press enter when ready: ")
        gameWIN = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@id='overlay'][contains(@style, 'opacity')]"))
        )
        gameWIN = driver.find_element_by_xpath(
            "//div[@id='overlay'][contains(@style, 'opacity')]")
        gameDetector = gameWIN.get_attribute('style')

        # time.sleep(20)
        currentWord = None
        while(currentWord is None or len(currentWord) == 0):
            currentWord = driver.find_element_by_xpath(
                "//div[@id = 'currentWord']")
            target = currentWord.text
        f = open(f"letters{len(target)}.txt")
        words = list(f.read().split("\n"))

        i = math.ceil(len(words) / 6)
        while gameDetector.__contains__('0'):
            word = words[i]
            chat.clear()
            chat.send_keys(word)
            chat.send_keys(Keys.ENTER)

            gameWIN = driver.find_element_by_xpath(
                "//div[@id='overlay'][contains(@style, 'opacity')]")
            gameDetector = gameWIN.get_attribute('style')
            i += 1
            time.sleep(1)


N = 6   # Number of browsers to spawn
thread_list = list()

# Start test
for i in range(N):
    t = threading.Thread(name='Test {}'.format(
        i), target=test_logic, args=(i,))
    t.start()
    time.sleep(1)
    print(t.name + ' started!')
    thread_list.append(t)

# Wait for all threads to complete
for thread in thread_list:
    thread.join()

print('Test completed!')
