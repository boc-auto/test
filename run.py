
import unittest
from utils.HTMLTestRunner_PY import HTMLTestRunner



if __name__ == '__main__':
    report_title = 'Example用例执行报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = './result.html'
    test_dir = "./case"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py")
    # unittest.TextTestRunner(verbosity=2).run(discover)
    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(discover)















