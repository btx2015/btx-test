
from ....base import BaseModule
import datetime


class Module(BaseModule):

    def test(self):
        # 点击新建模板
        self.xpath_click("新建模板按钮", "//div[@id='pane-future']/div/div/div/form/div/div/button")
        # 输入模板名称
        template_name = '测试' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        self.xpath_input("模板名称输入框", "//div[@class='el-dialog__body']/form/div/div/div/div/input", template_name)
        # 点击确定
        self.xpath_click("确定按钮", "//div[@class='dialog-footer']/button[2]")
        # 点击确认
        self.xpath_click("确认按钮", "//div[@class='el-message-box__btns']/button[2]")

        self.pager.time.sleep(2)

        # 验证
        self.xpath_click("模板名称框", "//*[@placeholder='模板']")

        template_dropdown = self.xpath_select("模板下拉框", "//ul[@class='el-scrollbar__view el-select-dropdown__list']/li")

        create_success = False
        for template in template_dropdown:
            if template.get_attribute('textContent') == template_name:
                create_success = True
                template.click()
                break
        if not create_success:
            self.report('创建期货风控模板失败')
