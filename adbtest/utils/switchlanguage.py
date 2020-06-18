import unittest
import time
from appium import webdriver
from adbtest.utils import util

desired_caps = {};
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = '5203adddfc7334c1'
desired_caps['noReset'] = 'true'
#driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps);


class switchlanguageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps);
    def tearDown(self):
        self.driver.quit()
    def test_start(self):
        el1 = self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.facebook.orca:id/(name removed)']")
        el1.click() #根据xpath点击 messenger输入框
        utils.swichlanguage(self)
        # driver.tap([(436,995),(537,893)],50)
        #self.driver.tap([(408,1225)],2000).swipe(408,1225,50,1223,1000)
        time.sleep(1)
        utils.cleartext(self);
        self.driver.keyevent(4)
if __name__ == '__main__':
    # 构造测试集  defaultTestLoader（）即TestLoader（）测试用例加载器，包括多个加载测试用例的方法，返回一个测试套件
    # loadTestsFromTestCase（）根据给定的测试类，获取其中的所有测试方法，并返回一个测试套件
    suite = unittest.TestLoader().loadTestsFromTestCase(switchlanguageTest)
    # unittest框架的TextTestRunner（）类，通过该类下面的run（）方法来运行suite所组装的测试用例，入参为suite测试套件
    unittest.TextTestRunner(verbosity=2).run(suite)
    # 上面两行代码可以换成下面一行
    # unittest.main()