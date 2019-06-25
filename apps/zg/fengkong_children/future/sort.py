
from ....base import BaseModule


class Module(BaseModule):

    def test(self):
        # 点击品种排序
        self.xpath_click("品种按钮", "//form[@class='el-form el-form--inline']/div[3]/div/button")
        # 获取第一个品种排序输入框的值
        sort_name = self.xpath_text("第一个品种排序品种名称", "//tbody/tr[1]/td[1]/div/span")
        element_name = "品种排序输入框"
        sort_value = self.xpath_value(element_name, "//tbody/tr[1]/td[3]/div/div/input")
        sort_input = int(sort_value) + 1
        self.xpath_input(sort_name, "//tbody/tr[1]/td[3]/div/div/input", sort_input)
        # 验证
        self.pager.time.sleep(1)
        sorts = self.xpath_select("品种排序", "//tbody/tr")
        for sort in sorts:
            try:
                name = sort.find_element_by_xpath("//tbody/tr[1]/td[1]/div/span")
            except Exception:
                self.report('品种排序的品种名称', 1)
            else:
                name.get_attribute('textContent').strip()
                if sort_name == name:
                    value = sort.find_element_by_xpath("//td[3]/div/input").get_attribute('value')
                    if not sort_input == value:
                        self.report('品种排序修改失败')
                    break
