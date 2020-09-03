import os, sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())


#
# from selenium.webdriver.support.wait import WebDriverWait
# from Base.base_driver import init_driver
#
#
# class BaseAction(init_driver):
#
#
#     def find_element(self,loc):
#         by=loc[0]
#         value=loc[1]
#         return WebDriverWait(self.driver,5,1).until(lambda x,x.find_element(by))
#
#     def find_elements(self, loc):
#         by = loc[0]
#         value = loc[1]
#         return WebDriverWait(self.driver, 5, 1).until(lambda x, x.find_element(by))
# def click(self):
#     pass
class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc):
        by = loc[0]
        value = loc[1]
        if by == By.XPATH:
            value = make_xpath_with_feature(value)
        return WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(by, value))

    def find_elements(self, loc):
        by = loc[0]
        value = loc[1]
        if by == By.XPATH:
            value = make_xpath_with_feature(value)
        return WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_elements(by, value))

    def input_text(self, loc, text, index=0):
        self.find_elements(loc)[index].send_keys(text)

    def click(self, loc, index=0):
        self.find_elements(loc)[index].click()

    # 多条件的拼接
    def make_xpath_with_unit_feature(self, loc):
        feature_start = "//*["
        feature_end = "]"

        if isinstance(loc, str):
            if loc.startswith("//*"):
                return loc
            else:
                feature = self.make_xpath_with_feature(loc)
                feature = feature_start + feature + feature_end
                return feature

        if isinstance(loc, list):
            str1 = ""
            for i in loc:
                short_str = self.make_xpath_with_feature(i)
                str1 += short_str + " and "
        feature = str1.rstrip(" and ")
        return feature_start + feature + feature_end

    def make_xpath_with_feature(self, loc):
        feature_start = "//*["
        feature_end = "]"
        arg = loc.split(",")
        key = 0
        value = 1
        mode = 2
        if arg[mode] == "1":
            feature = "@" + arg[key] + "=" + '"' + arg[value] + '"'
        elif arg[mode] == "2":
            feature = "contains(@" + arg[key] + "," + '"' + arg[value] + '"' + ")"
        if isinstance(loc, list):
            return feature
        if isinstance(loc, str):
            return feature_start + feature + feature_end
