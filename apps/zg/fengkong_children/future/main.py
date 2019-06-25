
from ....base import BaseModule


class Module(BaseModule):

    def test(self):
        # 点击主力合约配置
        self.xpath_click("主力合约配置按钮", "//form[@class='el-form el-form--inline']/div[4]/div/button")
        self.pager.time.sleep(1)
        # 点击所有品种下拉框
        # self.xpath_click("所有品种下拉框", "//div[@class='el-dialog__body']/form/div[1]/div/div/div/input")
        # self.pager.time.sleep(1)
        # 点击所有品种下拉框的第一个选项
        # self.xpath_click("所有品种下拉框的第一个选项", "//body/div[@class='el-select-dropdown el-popper'][2]/div[1]/div/ul/li[1]")
        # 点击自动切换主力合约开关
        class_name = self.xpath_class("切换主力合约开关", "//div[@role='switch']")
        if not class_name == "el-switch":
            self.xpath_click("自动切换主力合约开关", "//span[@class='el-switch__core']")
        # 获取第一个合约的主力状态
        contract_state = self.xpath_text("第一个合约的主力状态", "//table/tbody/tr[1]/td[3]")
        # 切换第一个合约的主力状态
        self.xpath_click("第一个合约的主力状态", "//table/tbody/tr[1]/td[3]")
        # 点击修改确认
        self.xpath_click("确认按钮", "//div[@class='el-message-box__btns']/button[2]")
        # 获取第一个合约的主力状态
        contract_change = self.xpath_text("第一个合约的主力状态", "//table/tbody/tr[1]/td[3]")
        # 验证
        if contract_state == contract_change:
            self.report("合约修改主力状态失败")
        # 关闭窗口
        self.pager.time.sleep(1)
        self.xpath_click("弹窗关闭按钮", "//div[@class='el-dialog__wrapper'][4]/div/div[1]/button")
