from openpyxl import load_workbook
from adbtest.utils import util
from adbtest.devices_key import samsung6_inputkey
from adbtest.utils.manage_case_road import manage_case_road
# 使用pandas读取excel文件
import unittest
import time
from appium import webdriver

from adbtest.utils.openypxl_util import excel

desired_caps = {};
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = '5203adddfc7334c1'
desired_caps['noReset'] = 'true'


# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps);


class en_longpress_inputTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps);

    def tearDown(self):
        self.driver.quit()

    def test_start(self):
        xls_road = manage_case_road().get_road()  # 获取回归用例文件路径
        xls = excel(xls_road)
        words = xls.getCellValue(4, 2)  # 获取英语纠错点击按键内容
        try:
            util.keyboard_show(self)
            time.sleep(1)
            print(words)
            print("英语长按上屏测试开始")
            time.sleep(1)
            # 根据输入内容单元格点击对应按键
            for i in range(len(words) + 1):
                word = words[i - 1:i]
                print(word)
                util.input_by_tag(word, self)
            samsung6_inputkey.longpress_sugg(self, 1200)
            samsung6_inputkey.longpress_sugg_input(self, 0)
            time.sleep(1)
            message = util.gettext(self)
            xls.setCellValue(4, 5, message)  # 实际上屏内容
            if len(message) <= 0:
                xls.setCellValue(4, 4, "输入框内容为空，测试结果错误")
                time.sleep(1)
            elif message is not None:  # 将输入框内容message转换成小写字母和tag对比
                xls.setCellValue(4, 4, "输入内容不为空,上屏成功")
                time.sleep(1)
            xls.saveData(xls_road)
            time.sleep(1)
        except OSError:
            pass
        finally:
            util.cleartext(self)
            self.driver.keyevent(4)
            print("英语长按候选词栏上屏测试结束")


if __name__ == '__main__':
    # 构造测试集  defaultTestLoader（）即TestLoader（）测试用例加载器，包括多个加载测试用例的方法，返回一个测试套件
    # loadTestsFromTestCase（）根据给定的测试类，获取其中的所有测试方法，并返回一个测试套件
    suite = unittest.TestLoader().loadTestsFromTestCase(en_longpress_inputTest)
    # unittest框架的TextTestRunner（）类，通过该类下面的run（）方法来运行suite所组装的测试用例，入参为suite测试套件
    unittest.TextTestRunner(verbosity=2).run(suite)
    # 上面两行代码可以换成下面一行
    # unittest.main()
