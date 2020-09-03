

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        #init里面可以写已经确定的前置功能,譬如所有的测试case 都是在display page 下面那就可以写，对应的测试脚本中可以不写
        self.click_search()

    def click_search(self):
        self.driver.find_element_by_xpath("//*[contains(@content-desc,'搜索')]").click()

    def send_key(self,keys):
        self.driver.find_element_by_xpath("//*[contains(@test,'搜索…')]").send_keys(keys)