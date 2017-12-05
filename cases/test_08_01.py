# -*- coding:utf-8 -*-
__author__ = 'dinght'
from selenium import webdriver
from test_case.selenium_train.Common.Login_logout import Login
import unittest
class TestLogIn(unittest.TestCase):
    u'''测试登录功能'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://passport.cnblogs.com/user/signin"
        self.driver.get(self.url)
        self.driver.implicitly_wait(30)

    def test_login(self):
        u'''验证输入正确的用户名和密码，登录成功 '''
        Login(driver=self.driver,username="18200285063",psw="dht15117299104@")
        #获取登录账号名
        text1 = self.driver.find_element_by_id("lnk_current_user").text
        print(text1)
        self.assertEqual(text1,"HazelRunner_dd")

    def tearDown(self):
        self.driver.quit()
'''
if __name__ == "__main__":
    unittest.main()
'''

