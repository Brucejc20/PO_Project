import os, sys,pytest
from time import sleep

sys.path.append(os.getcwd())
from Base.base_driver import init_driver
from Page.Display_page import DisplayPage


class Test_Search:

    def setup(self):
        self.driver = init_driver()
        self.display_page = DisplayPage(self.driver)

    def test_click_display(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        sleep(1)
        self.display_page.click_sleep()
        sleep(1)
        self.display_page.click_sleep_time()

if __name__ == '__main__':
    pytest.main("-s ./Script/test_display.py")

