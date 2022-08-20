from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

class InstaBot():
    def __init__(self,path):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path=path,options=options)
        pass

    def login(self,myusername,mypassword):
        self.driver.get("https://www.instagram.com/")
        time.sleep(5)

        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        username.send_keys(myusername)
        password.send_keys(mypassword)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        
        pass

    def get_followers(self):
        pass

    def get_following(self):
        pass

    def get_likes(self):
        pass

    def auto_follow(self):
        pass

    def unfollow(self):
        pass

chrome_driver_path = "C:\\Development\\chromedriver.exe"
bot = InstaBot(chrome_driver_path)
bot.login("pauloleroy","Galo.1344528")
