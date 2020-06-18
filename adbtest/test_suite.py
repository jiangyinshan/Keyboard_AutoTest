import unittest
from adbtest.tool import HTMLTestRunner
# test_register是文件名，RegistTest是该文件里定义的一个类
from adbtest.en_testcase.en_correctTest import en_correctTest
from adbtest.en_testcase.en_click_inputTest import en_click_inputTest
from adbtest.en_testcase.en_longpress_input import en_longpress_inputTest
from adbtest.en_testcase.en_swipeTest import en_swipeTest
from adbtest.es_testcase.es_swipeTest import es_swipeTest
from adbtest.es_testcase.es_click_input import es_click_inputTest
from adbtest.es_testcase.es_correct import es_correctTest
from adbtest.es_testcase.es_longpress_input import es_longpress_inputTest
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(en_click_inputTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(en_correctTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(en_longpress_inputTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(en_swipeTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(es_click_inputTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(es_correctTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(es_swipeTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(es_longpress_inputTest))
    # 这一步是在当前文件夹里自动生成一个测试报告，测试报告名称就叫：UnittestTextReport.txt.
with open('HTMLReport.html', 'wb') as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                           title='回归测试用例报告',
                                           description='html test runner.',
                                           verbosity=2
                                           )
    runner.run(suite)