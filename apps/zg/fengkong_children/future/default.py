
from ....base import BaseModule


class Module(BaseModule):

    def test(self):
        # 点击设为默认
        self.xpath_click("内盘期货设为默认按钮", "//form[@class='el-form el-form--inline']/div[2]/div/button[2]")
        # 点击确认按钮
        self.xpath_click("内盘期货确认按钮", "//div[@class='el-message-box__btns']/button[2]")
        self.pager.time.sleep(1)
        # 验证
        default_button = self.xpath_text("内盘期货设为默认按钮", "//form[@class='el-form el-form--inline']/div[2]/div/button[2]")
        if not default_button == "默认模板":
            self.report('默认模板设置失败')
