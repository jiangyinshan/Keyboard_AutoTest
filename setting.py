import unittest
from adbtest.utils import util
from adbtest.devices_key import samsung6_inputkey
import time
from appium import webdriver

desired_caps = {};
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = '5203adddfc7334c1'
desired_caps['noReset'] = 'true'
#driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps);


class en_correctTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps);
    def tearDown(self):
        self.driver.quit()
    def test_start(self):
        # el1 = driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.facebook.orca:id/(name removed)']")
        # el1.click() #根据xpath点击
        print("设置小数字键盘开始")
        self.driver.keyevent(3)
        time.sleep(1)
        utils.click_apps(self, 0)
        utils.click_emojipro(self, 0)
        time.sleep(5)
        self.driver.keyevent(4)
        utils.click_mine(self, 0)
        utils.click_preferences(self, 0)
        utils.click_number_row(self, 0)
        time.sleep(1)
        self.driver.keyevent(123); #光标移动到末尾
        samsung6_inputkey.space(self, 0); #上屏 copy
        t1 = utils.gettext(self)
        if t1 == "Copy":
            print("英语自动纠错测试通过")
        else:
            print("英语自动纠错测试未通过")
        time.sleep(1)
        utils.cleartext(self);
        self.driver.keyevent(4)
        print("英语自动纠错测试结束")
if __name__ == '__main__':
    # 构造测试集  defaultTestLoader（）即TestLoader（）测试用例加载器，包括多个加载测试用例的方法，返回一个测试套件
    # loadTestsFromTestCase（）根据给定的测试类，获取其中的所有测试方法，并返回一个测试套件
    suite = unittest.TestLoader().loadTestsFromTestCase(en_correctTest)
    # unittest框架的TextTestRunner（）类，通过该类下面的run（）方法来运行suite所组装的测试用例，入参为suite测试套件
    unittest.TextTestRunner(verbosity=2).run(suite)
    # 上面两行代码可以换成下面一行
    # unittest.main()