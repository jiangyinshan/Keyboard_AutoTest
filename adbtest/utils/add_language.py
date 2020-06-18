from adbtest.utils import util
from adbtest.devices_key import samsung6_inputkey
import unittest
import time
from appium import webdriver

desired_caps = {};
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = '5203adddfc7334c1'
desired_caps['noReset'] = 'true'
oneplus_desired_caps = {};
oneplus_desired_caps['platformName'] = 'Android'
oneplus_desired_caps['platformVersion'] = '10'
oneplus_desired_caps['deviceName'] = '4e62be76'
oneplus_desired_caps['noReset'] = 'true'
#driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps);
class es_click_inputTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps);
    def tearDown(self):
        self.driver.quit()
    def test_start(self):
        self.driver.keyevent(3)
        menu = self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.sec.android.app.launcher:id/home_allAppsIcon']")
        menu.click() #点击apps按钮
        kika = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Kika Keyboard' and @content-desc='Kika Keyboard']")
        kika.click() #点击启动kika
        print("开始睡眠")
        time.sleep(3)
        print("睡眠结束")
        self.driver.keyevent(4) #点击返回键，关闭开屏广告
        util.click_mine(self)
        time.sleep(1)
        util.click_language(self)
        time.sleep(1)
        util.add_es(self)
if __name__ == '__main__':
    # 构造测试集  defaultTestLoader（）即TestLoader（）测试用例加载器，包括多个加载测试用例的方法，返回一个测试套件
    # loadTestsFromTestCase（）根据给定的测试类，获取其中的所有测试方法，并返回一个测试套件
    suite = unittest.TestLoader().loadTestsFromTestCase(es_click_inputTest)
    # unittest框架的TextTestRunner（）类，通过该类下面的run（）方法来运行suite所组装的测试用例，入参为suite测试套件
    unittest.TextTestRunner(verbosity=2).run(suite)
    # 上面两行代码可以换成下面一行
    # unittest.main()