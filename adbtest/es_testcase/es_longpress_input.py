from openpyxl import load_workbook
from adbtest.utils import util
from adbtest.devices_key import samsung6_inputkey
from adbtest.utils.manage_case_road import manage_case_road
from adbtest.utils.openypxl_util import excel
import unittest
import time
from appium import webdriver

desired_caps = {};
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = '5203adddfc7334c1'
desired_caps['noReset'] = 'true'


# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps);


class es_longpress_inputTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps);

    def tearDown(self):
        self.driver.quit()

    def test_start(self):
        xls_road = manage_case_road().get_road()  # 获取回归用例文件路径
        xls = excel(xls_road)
        words = xls.getCellValue(9, 2)
        print("西班牙语长按候选词栏上屏测试开始")
        try:
            util.keyboard_show(self)
            time.sleep(1)
            self.driver.keyevent(123)  # 光标移动到末尾
            time.sleep(1)
            for i in range(len(words) + 1):  # 根据输入内容单元格点击对应按键
                word = words[i - 1:i]
                print(word)
                util.input_by_tag(word, self)
            samsung6_inputkey.longpress_sugg(self, 1200)
            samsung6_inputkey.longpress_sugg_input(self, 0)
            time.sleep(1)
            message = util.gettext(self)
            xls.setCellValue(9, 5, message)  # 实际上屏内容
            if len(message) <= 0:
                xls.setCellValue(9, 4, "输入框内容为空，测试结果错误")  # 保存测试结论
                time.sleep(1)
            elif message is not None:  # 将输入框内容message转换成小写字母和tag对比
                xls.setCellValue(9, 4, "长按输入上屏成功")  # 保存测试结论
                time.sleep(1)
            xls.saveData(xls_road)
            time.sleep(1)
        except OSError:
            pass
        finally:
            util.cleartext(self)
            self.driver.keyevent(4)
            print("西班牙语长按候选词栏上屏测试结束")


if __name__ == '__main__':
    # 构造测试集  defaultTestLoader（）即TestLoader（）测试用例加载器，包括多个加载测试用例的方法，返回一个测试套件
    # loadTestsFromTestCase（）根据给定的测试类，获取其中的所有测试方法，并返回一个测试套件
    suite = unittest.TestLoader().loadTestsFromTestCase(es_longpress_inputTest)
    # unittest框架的TextTestRunner（）类，通过该类下面的run（）方法来运行suite所组装的测试用例，入参为suite测试套件
    unittest.TextTestRunner(verbosity=2).run(suite)
    # 上面两行代码可以换成下面一行
    # unittest.main()
