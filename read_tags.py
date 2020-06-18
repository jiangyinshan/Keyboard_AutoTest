# 使用pandas读取excel文件
import pandas as pd

# print("😘")
# str="happy brithday to you"
# for i in range (len(str)):
#    print(str[i-1:i])
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


# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps);


class en_correctTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps);

    def tearDown(self):
        self.driver.quit()

    def test_start(self):
        io = r'\Users\xm20190901\Downloads\tag.xlsx'
        data = pd.read_excel(r'/Users/xm20190901/Downloads/tag.xlsx', sheet_name='Sheet1')
        data.head()
        nrows = data.shape[0]  # 获取最大行
        ncols = data.columns.size  # 获取最大列
        print(data)
        irow = 1
        util.click_messenger(self)
        for irow in range(nrows):
            taglist = data.iloc[irow, 0]
            print(taglist)
            for i in range(len(taglist) + 1):
                str = taglist[i - 1:i]
                time.sleep(1)
                util.input_by_tag(str, self)
                print(str)
            try:
                time.sleep(4)
                self.driver.tap([(603, 572)], 0);
                time.sleep(1)
                util.click_messenger(self)
                print("清空文本")
                time.sleep(1)
                util.cleartext(self)
                time.sleep(1)
            except OSError:
                pass
                continue
            print("开始输入间隔消息，顶出gif")
            try:
                samsung6_inputkey.a(self, 0)
                samsung6_inputkey.enter(self, 0)
                samsung6_inputkey.enter(self, 0)
                samsung6_inputkey.enter(self, 0)
                samsung6_inputkey.enter(self, 0)
                samsung6_inputkey.enter(self, 0)
                samsung6_inputkey.enter(self, 0)
                samsung6_inputkey.enter(self, 0)
                samsung6_inputkey.enter(self, 0)
                samsung6_inputkey.enter(self, 0)
                samsung6_inputkey.enter(self, 0)
                samsung6_inputkey.enter(self, 0)
                samsung6_inputkey.enter(self, 0)
                samsung6_inputkey.enter(self, 0)
                samsung6_inputkey.a(self, 0)
                util.send_message(self)
            except OSError:
                pass
                continue
            util.cleartext(self)


if __name__ == '__main__':
    # 构造测试集  defaultTestLoader（）即TestLoader（）测试用例加载器，包括多个加载测试用例的方法，返回一个测试套件
    # loadTestsFromTestCase（）根据给定的测试类，获取其中的所有测试方法，并返回一个测试套件
    suite = unittest.TestLoader().loadTestsFromTestCase(en_correctTest)
    # unittest框架的TextTestRunner（）类，通过该类下面的run（）方法来运行suite所组装的测试用例，入参为suite测试套件
    unittest.TextTestRunner(verbosity=2).run(suite)
    # 上面两行代码可以换成下面一行
    # unittest.main()
