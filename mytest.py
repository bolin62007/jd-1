# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Mytest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://passport.jd.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_my(self):
        driver = self.driver
        driver.get(self.base_url + "/new/login.aspx?ReturnUrl=https://item.jd.com/4390094.html")
        driver.find_element_by_link_text(u"账户登录").click()
        driver.find_element_by_id("loginname").send_keys("18371542519")
        driver.find_element_by_id("nloginpwd").send_keys("Super123!")
        driver.find_element_by_id("loginsubmit").click()
        driver.find_element_by_id("J-toolbar-load-hook").click()
        driver.find_element_by_id("choose-btn-qiang").click()
        driver.find_element_by_id("choose-btn-qiang").click()
        driver.find_element_by_id("choose-btn-qiang").click()
        driver.find_element_by_id("J-toolbar-load-hook").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
