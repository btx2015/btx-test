
from ....base import BaseModule


class Module(BaseModule):

    def test(self):
        # 点击A股管理标签
        self.xpath_click("标签", "//div[@id='tab-stock']")
