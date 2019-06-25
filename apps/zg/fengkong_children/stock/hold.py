
from ....base import BaseModule


class Module(BaseModule):

    def test(self):
        # 点击仓比限制标签
        self.xpath_click("仓比限制标签", "//div[@id='tab-0']")
        # 点击编辑模板
        self.xpath_click("编辑模板按钮", "//form/div/div/div/button[1]")
        # 输入子账号持仓金额
        hold_name = '子账号持仓金额输入框'
        hold_input = '0'
        self.xpath_input(hold_name, "//form[@id='cbxz']/div[2]/div/div[2]/div/div/div/input", hold_input)
        hold_input = self.xpath_value(hold_name, "//form[@id='cbxz']/div[2]/div/div[2]/div/div/div/input")
        # 点击保存按钮
        self.xpath_click("保存按钮", "//form/div/div/div/button[2]")
        # 点击确认按钮
        self.xpath_click("确认按钮", "//div[@class='el-message-box__btns']/button[2]")

        # 验证
        hold_save = self.xpath_value(hold_name, "//form[@id='cbxz']/div[2]/div/div[2]/div/div/div/input")
        if not hold_input == hold_save:
            self.report("仓比限制的子账号持仓金额设置失败")
