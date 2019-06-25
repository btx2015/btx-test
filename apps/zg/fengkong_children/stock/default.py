
from ....base import BaseModule


class Module(BaseModule):

    def test(self):
        # 点击设为默认
        self.xpath_click("设为默认按钮", "//form[@class='el-form el-form--inline']/div[3]")
        # 点击确认按钮
        self.xpath_click("确认按钮", "//div[@class='el-message-box__btns']/button[2]")
        # 验证
        default_button = self.xpath_text("设为默认按钮", "//form[@class='el-form el-form--inline']/div[3]").strip()
        if not default_button == "默认模板":
            self.report('设置默认模板失败')
