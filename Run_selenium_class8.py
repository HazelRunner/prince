# -*- coding:utf-8 -*-
__author__ = 'dinght'
import unittest,time



def all_case():
    #待执行用例目录
    case_dir = "D:\\Pycharm-Train\\test\\test_case\\selenium_train\\cases"
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,pattern='test*.py',top_level_dir=None)

    #discover筛选出来的方法，循环加载到测试套件中
    for test_case in discover:
        for case in test_case:
            testunit.addTest(case)
    print (testunit)
    return testunit

if __name__ == "__main__":
    unittest.main()
