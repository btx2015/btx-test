
from ....base import BaseModule


class Module(BaseModule):

    def test(self):
        # 点击内盘期货标签
        self.xpath_click("内盘期货标签", "//div[@id='tab-future']")
