import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from plugins.utils import print_same_line


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
        self.sub_count = 0

    def close_browser(self):
        self.driver.close()
        return

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def explore_tag(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        # gathering photos
        pic_hrefs = []
        pseudo = []
        for i in range(0, 6):
            try:
                for j in range(0, i + 1):
                    if j == 0:
                        driver.execute_script("window.scrollTo(window.scrollTop, {});".format(4284))
                    else:
                        driver.execute_script("window.scrollTo(window.scrollTop, {});".format(6120))
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [
                    elem.get_attribute('href') for elem in hrefs_in_view
                    if '.com/p/' in elem.get_attribute('href')
                ]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                for pic_href in pic_hrefs:
                    driver.get(pic_href)
                    time.sleep(random.randint(2, 4))
                    self.like_photo_function(driver)
                    time.sleep(random.randint(2, 4))
                    userfound = self.sub_to_owner(driver)
                    if userfound is not None:
                        continue
                    pseudo.append(userfound)
                if len(pseudo) >= 40:
                    break
            except Exception:
                continue


    def like_photo_function(self, driver):
        try:
            like_button = driver.find_element_by_xpath('//span[@aria-label="J’aime"]')
            like_button.click()
        except Exception:
            pass

    def sub_to_owner(self, driver):
        try:
            sub_button = lambda: driver.find_element_by_xpath("//div/button[text()='S’abonner']")
            button_type = sub_button().text
            if button_type == 'S’abonner':
                sub_button().click()
                self.sub_count += 1
                return driver.find_element_by_xpath("//h2/a")
            return None
        except Exception:
            pass
