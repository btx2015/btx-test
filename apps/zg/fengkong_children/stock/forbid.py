
from ....base import BaseModule


class Module(BaseModule):

    def test(self):
        # 点击禁买股标签
        self.xpath_click("禁买股标签", "//div[@id='tab-1']")
        # 点击股票名称代码
        self.xpath_click("股票名称代码下拉框", "//input[@placeholder='股票名称代码']")
        self.pager.time.sleep(1)
        # 获取第一个选项的名字
        click_forbid = self.xpath_text("股票名称代码下拉框第一个选项", "//ul[@role='listbox']/li[1]")
        # 点击第一个选项
        self.xpath_click("股票名称代码下拉框第一个选项", "//ul[@role='listbox']/li[1]")
        # 点击添加按钮
        self.xpath_click("禁买股添加按钮", "//div[@id='pane-1']/div/div[2]/button[1]")
        # 点击确认按钮
        self.xpath_click("添加禁买股确认按钮", "//div[@class='el-message-box__btns']/button[2]")

        self.pager.time.sleep(2)

        # 验证
        forbid_name = self.xpath_text("禁买股列表中的名称", "//tbody/tr[1]/td[1]/div")
        forbid_code = self.xpath_text("禁买股列表中的代码", "//tbody/tr[1]/td[2]/div")
        save_forbid = forbid_name + "(" + forbid_code + ")"
        if not click_forbid == save_forbid:
            self.report("添加禁卖股保存失败")
