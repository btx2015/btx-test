
from abc import ABCMeta, abstractmethod


class BaseModule(metaclass=ABCMeta):

    def __init__(self, pager, page_name):
        self.pager = pager
        self.page_name = page_name

    def xpath_find(self, element_name, xpath):
        return self.pager.find_element('xpath', xpath, '', [
            self.page_name, element_name
        ])

    # 定位元素并点击
    def xpath_click(self, element_name, xpath):
        return self.pager.find_element('xpath', xpath, 'click', [
            self.page_name, element_name
        ])

    # 定位元素并输入
    def xpath_input(self, element_name, xpath, content):
        return self.pager.find_element('xpath', xpath, 'input', [
            self.page_name, element_name, content
        ])

    def xpath_text(self, element_name, attribute):
        return self.pager.find_element('xpath', attribute, 'text', [
            self.page_name, element_name
        ])

    def xpath_value(self, element_name, attribute):
        return self.pager.find_element('xpath', attribute, 'value', [
            self.page_name, element_name
        ])

    def xpath_class(self, element_name, attribute):
        return self.pager.find_element('xpath', attribute, 'class', [
            self.page_name, element_name
        ])

    def xpath_select(self, element_name, attribute):
        return self.pager.find_elements('xpath', attribute, [
            self.page_name, element_name
        ])

    def report(self, describe, element=0):
        if element == 0:
            self.pager.operate_error(self.page_name, describe)
        else:
            self.pager.element_error(self.page_name, describe)

    @staticmethod
    def p(message):
        print(message)
        print()

    @abstractmethod
    def test(self):
        pass
