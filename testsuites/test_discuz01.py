from testsuites.base_testcase import BaseTestCase
from pageobjects.discuz_mainpage import MainPage
import unittest
# 用户登录
# 默认板块发帖
# 默认板块回帖
# 用户退出
class Discuz(BaseTestCase):
    def test_login(self):
        mainPage=MainPage(self.driver)
        name=mainPage.login("sasa","1393269559")
        self.assertEqual(name,"sasa",msg="登录失败")
        if "sasa" in name:
            mainPage.send("Hello","Hello,unittest!")
            result = mainPage.get_t_tit()
            self.assertEqual(result, "Hello", msg="发帖失败")
            mainPage.repl("asdfgfdgfgf")
            ex=mainPage.exit()
            assert "用户名" in ex

if __name__=="__main__":
    unittest.main(verbosity=2)
