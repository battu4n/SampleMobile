
import unittest
from appium import webdriver
from time import sleep
import os
import pytest
import logging
os.system("start /B start cmd.exe @cmd /k appium ")

class gmail(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10.0'
        desired_caps['deviceName'] = 'Galaxy M01 Core'
        desired_caps['appPackage']= 'com.google.android.gm'
        desired_caps['appActivity']='.ConversationListActivityGmail'
        desired_caps['autoAcceptAlerts'] = 'true'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        sleep(10)
    def tearDown(self):
        self.driver.quit()

    @pytest.mark.sanity
    def test_gmail_launch(self):
        sleep(10)
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p'
                            )
        if (self.driver.find_element_by_xpath("//android.widget.TextView[@text ='GOT IT']").is_displayed()):
            self.driver.find_element_by_xpath("//android.widget.TextView[@text ='GOT IT']").click()
        elif (self.driver.find_element_by_xpath("//android.widget.TextView[@text ='got it']").is_displayed()):
            self.driver.find_element_by_xpath("//android.widget.TextView[@text ='got it']").click()
        sleep(10)
        if (self.driver.find_element_by_xpath("//android.widget.TextView[@text ='TAKE ME TO GMAIL']")).is_displayed():
            self.driver.find_element_by_xpath("//android.widget.TextView[@text ='TAKE ME TO GMAIL']").click()
        elif (self.driver.find_element_by_xpath("//android.widget.TextView[@text ='take me to gmail']")).is_displayed():
            self.driver.find_element_by_xpath("//android.widget.TextView[@text ='take me to gmail']").click()
        """if (self.driver.find_element_by_xpath("//android.widget.Button[@text ='Next']")).is_displayed():
            self.driver.find_element_by_xpath("//android.widget.Button[@text ='Next']").click()
        elif (self.driver.find_element_by_xpath("//android.widget.Button[@text ='OK']")).is_displayed():
             self.driver.find_element_by_xpath("//android.widget.Button[@text ='OK']").click()"""

    @pytest.mark.regression
    def test_gmail_compose(self):
        sleep(10)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text ='GOT IT']").is_displayed()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text ='GOT IT']").click()
        sleep(10)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text ='TAKE ME TO GMAIL']").is_displayed()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text ='TAKE ME TO GMAIL']").click()
        sleep(10)
        #if (self.driver.find_element_by_xpath("//android.widget.Button[@text ='Next']")).is_displayed():
         #self.driver.find_element_by_xpath("//android.widget.Button[@text ='Next']").click()
        if (self.driver.find_element_by_id('next_button')).is_displayed():
                self.driver.find_element_by_id('next_button').click()
        sleep(5)
        compose = self.driver.find_element_by_id('compose_button').click()
        sleep(10)
        if(self.driver.find_element_by_id('button1')).click():
            sleep(10)
        to_mail = self.driver.find_element_by_xpath("//android.widget.TextView[[@text= 'To']]").send_keys("battu4n@gmail.com")
        compose_mail = self.driver.find_element_by_xpath("//android.widget.EditText[@text = 'Compose email']")
        compose_mail.send_keys("Narendra Writing mobile testing with pycharm")

    @pytest.mark.sanity
    def test_gmail_reply(self):
        sleep(10)
        gotit = self.driver.find_element_by_xpath("//android.widget.TextView[@text ='GOT IT']").click()
        sleep(10)
        if (self.driver.find_element_by_xpath("//android.widget.TextView[@text ='TAKE ME TO GMAIL']")).is_displayed():
            self.driver.find_element_by_xpath("//android.widget.TextView[@text ='TAKE ME TO GMAIL']").click()
        elif (self.driver.find_element_by_xpath("//android.widget.TextView[@text ='take me to gmail']")).is_displayed():
            self.driver.find_element_by_xpath("//android.widget.TextView[@text ='take me to gmail']").click()
        sleep(10)
        #if (self.driver.find_element_by_xpath("//android.widget.Button[@text ='Next']")).is_displayed():
           # self.driver.find_element_by_xpath("//android.widget.Button[@text ='Next']").click()
        sleep(10)
        if(self.driver.find_element_by_id('next_button')).is_displayed():
                self.driver.find_element_by_id('next_button').click()
        sleep(10)
        reply = self.driver.find_element_by_id("snippet").click()

        sleep(15)
        #self.driver.find_element_by_xpath("//android.widget.ImageView[@content-desc ='Reply']").click()
        self.driver.find_element_by_id("reply").click()
        sleep(15)
        if (self.driver.find_element_by_xpath("//android.widget.Button[@text ='OK']")).is_displayed():
            self.driver.find_element_by_xpath("//android.widget.Button[@text ='OK']").click()
        else:
            self.driver.find_element_by_xpath("//android.widget.Button[@text ='GOT IT']").click()
        sleep(10)
        self.driver.find_element_by_id("wc_body").send_keys("Narendra Writing mobile testing with pycharm")
        self.driver.find_element_by_id("send").click()
        if (self.driver.find_element_by_id("delete")).is_displayed():
            print("Reply message sent successfully to request mail id ")

# ---START OF SCRIPT
if __name__ == '__main__':
    unittest.main()