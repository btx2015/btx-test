from ...base import BaseModule


class Module(BaseModule):

    def __init__(self, pager, page):
        BaseModule.__init__(self, pager, page)

    # 入口函数
    def test(self):
        # 登陆
        self.login()

    # # # # # 以下是用例 # # # # #

    # 登陆测试用例
    def login(self):
        # username = input('Please input the username:')
        # password = input('Please input the password:')
        # captcha = input('Please input the captcha:')
        username = "leasin"
        password = "leasin"
        captcha = "a3b4"
        # 输入账号 密码 验证码
        self.xpath_input("用户名输入框", "//*[@placeholder='请输入用户名']", username)
        self.xpath_input("密码输入框", "//*[@placeholder='请输入密码']", password)
        self.xpath_input("验证码输入框", "//*[@placeholder='请输入验证码']", captcha)
        # 点击登陆
        self.xpath_click("登陆按钮", "//button[@class='el-button subBtn el-button--primary']")

        # 判断是否登陆成功
        welcome = self.xpath_text("欢迎语", "//h1")
        if not welcome == "欢迎使用后台系统":
            self.report("登陆", "登陆失败，检测不到首页欢迎语")
            exit()
