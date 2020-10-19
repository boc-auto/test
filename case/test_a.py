import unittest
from utils.HTMLTestRunner_PY import HTMLTestRunner

class TestBaidu1(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('初始111')
    @classmethod
    def tearDownClass(cls) -> None:
        print('结束111')
    def setUp(self) -> None:
        print('开始测试111111')
    def tearDown(self) -> None:
        print('结束测试1111111')
        print('____________')
    def testcase1(self):
        print('111-111')
        self.assertEqual(1,1,'判断 1 == 1')
    def testcase2(self):
        print('111111')
        self.assertEqual(2,2,'判断 1 == 2')


class TestBaidu2(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('初始222')
    @classmethod
    def tearDownClass(cls) -> None:
        print('结束222')
    def setUp(self) -> None:
        print('开始测试222222')
    def tearDown(self) -> None:
        print('结束测试222222')
        print('____________')
    def test_201(self):
        print('201')
        self.assertEqual(1,1,'判断 1 == 1')
    def test_202(self):
        print('202')
        self.assertEqual(2,2,'判断 1 == 2')



if __name__ == '__main__':
    # unittest.main()       运行所有的测试用例

    # suite = unittest.TestSuite()
    # suite.addTest(TestBaidu1("testcase2"))
    # unittest.TextTestRunner().run(suite)      # 运行指定的测试用例

    # suite1 = unittest.TestLoader().loadTestsFromTestCase(TestBaidu2)
    # suite = unittest.TestSuite(suite1)
    # unittest.TextTestRunner(verbosity=2).run(suite)       #只执行某一个/几个测试类

    report_title = 'Example用例执行报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = './result.html'
    test_dir = "./"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py")
    # unittest.TextTestRunner(verbosity=2).run(discover)
    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(discover)

















































































