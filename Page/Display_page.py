from selenium.webdriver.common.by import By
from Base.base_action import BaseAction

class DisplayPage(BaseAction):
    # 显示按钮,这样写是一个元组
    display_button = By.XPATH, "//*[contains(@text,'显示')]"
    sleep_button = By.XPATH, "//*[contains(@text,'休眠')]"
    sleep_time_button=By.XPATH, "//*[contains(@text,'1分钟')]"

    def __init__(self, driver):
        BaseAction.__init__(self,driver)
        self.click_display()

    # def __init__(self, driver):
    #     self.driver = driver
    #     # init里面可以写已经确定的前置功能,譬如所有的测试case 都是在display page 下面那就可以写，对应的测试脚本中可以不写
    #     self.find_element(self.display_button).click()

    def click_display(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        # self.find_element(self.display_button).click()
        self.click(self.display_button)

    def click_sleep(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'休眠')]").click()
        self.click(self.sleep_button)

    def click_sleep_time(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'1分钟')]").click()
        self.click(self.sleep_time_button)


    #自定义查找元素的方法，当出现相同元素的不同操作时，可以避免重复，直接传入查找方式和查找的值时即可
    # def find_element(self, location):
    #     return self.driver.find_element(location[0], location[1])
