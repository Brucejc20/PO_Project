

from appium import webdriver

import time


# class init_driver:
#
#     def __init__(self):
#         desired_cab = {}
#
#         desired_cab['platformName'] = 'android'
#         desired_cab['platformVersion'] = '5.1.1'
#         desired_cab['deviceName'] = 'localhost:62001'
#         desired_cab['appPackage'] = 'com.android.settings'
#         desired_cab['appActivity'] = 'com.android.settings.Settings'
#         desired_cab['automationName'] = 'UiAutomator2'
#         desired_cab['udid'] = "127.0.0.1:62001"
#
#         driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cab)
#         return driver
#
#         driver.find_element_by_xpath("//*[contains(@text,'显示')]")
#         driver.find_element(by)

def init_driver():
    desired_cab = {}

    desired_cab['platformName'] = 'android'
    desired_cab['platformVersion'] = '5.1.1'
    desired_cab['deviceName'] = 'localhost:62001'
    desired_cab['appPackage'] = 'com.android.settings'
    desired_cab['appActivity'] = 'com.android.settings.Settings'
    desired_cab['automationName'] = 'UiAutomator2'
    desired_cab['udid'] = "127.0.0.1:62001"

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cab)
    return driver
