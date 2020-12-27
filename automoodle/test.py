from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException
import time
import sqlite3


def post_answer(user, tasks):
    name = user[0]
    passw = user[1]
    gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
    binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.offline.enable", False)
    profile.set_preference("network.http.use-cache", False)
    driver = webdriver.Firefox(profile, firefox_binary=binary, executable_path=gecko + '.exe')
    driver.delete_all_cookies()
    driver.get("https://rsdo.oblcit.ru/login/index.php")
    assert "Региональная" in driver.title
    elem = driver.find_element_by_name("username")
    elem.send_keys(name)
    elem = driver.find_element_by_name("password")
    elem.send_keys(passw)
    time.sleep(1)
    elem = driver.find_element_by_id("loginbtn")
    elem.click()
    time.sleep(1)
    for task in tasks:
        link = task[0]
        answer_file = task[1]
        driver.get(link)
        els = driver.find_elements_by_xpath('//button[contains(text(), "Редактировать ответ")]')
        print(els)
        if not els:
            elem = driver.find_element_by_class_name("singlebutton")
            elem.click()
            elem = driver.find_element_by_id("id_onlinetext_editoreditable")
            f = open(answer_file, 'r')
            text = f.read()
            f.close()
            elem.send_keys(text)
            time.sleep(1)
            elem = driver.find_element_by_name("submitbutton")
            elem.click()
            time.sleep(1)
    driver.close()


conn = sqlite3.connect("kurs2020.db")
cursor = conn.cursor()
sql = "SELECT name, pass FROM users WHERE id > 1"
cursor.execute(sql)
users = cursor.fetchall()
sql = "SELECT link, file FROM tasks WHERE id < 18"
cursor.execute(sql)
tasks = cursor.fetchall()
conn.close()
for user in users:
    post_answer(user, tasks)



