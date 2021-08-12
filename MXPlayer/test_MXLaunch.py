import os
import unittest
from appium import webdriver
from time import sleep
import pytest
import logging
from utilities.customLoger import LogGen

class MXPlayer(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='10.0'
        desired_caps['deviceName']='Galaxy M01 Core'
        desired_caps['appPackage'] = 'com.mxtech.videoplayer.ad'
        desired_caps['appActivity'] = '.ActivityWelcomeMX'
        desired_caps['autoAcceptAlerts']='true'
        self.driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
        sleep(10)
    def tearDown(self):
        self.driver.quit()

    @pytest.mark.sanity
    def test_mxplayerlaunch(self):
        self.driver.find_element_by_xpath(".//android.widget.Button[@text='Allow']").click()
        sleep(5)
        if (self.driver.find_element_by_id('toolbar')).is_displayed():
            print("MX player launches successfully")
        else:
            print("MX player launch failed")

    @pytest.mark.regression
    def test_musicfolderopen(self):
        self.driver.find_element_by_xpath(".//android.widget.Button[@text='Allow']").click()
        sleep(5)
        if (self.driver.find_element_by_id('toolbar')).is_displayed():
            print("MX player launches successfully")
        else:
            print("MX player launch failed")
        self.driver.find_element_by_id('music_tab').click()
        sleep(10)
        self.driver.find_element_by_id("gaana_search_bar").send_keys("Temper songs")
        self.driver.hide_keyboard()
        self.driver.find_element_by_id('title').click()
        if (self.driver.find_element_by_id('music_next')).is_displayed():
            print("MX Player music test case pass")
        else:
            print("MX Player music test case failed")

if __name__=='__main__':
    unittest.main()
