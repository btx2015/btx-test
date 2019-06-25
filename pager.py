# driver 重构类

from selenium import webdriver
import time


class Pager:

    # 操作间隔时长
    sleep = 1

    def __init__(self, report, localhost, modules):
        self.report = report
        self.time = time
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.localhost = localhost
        self.modules = modules

    # 打开链接
    def get(self, url):
        self.driver.get(self.localhost + url)
        time.sleep(3)

    # 重构 web driver 定位元素方法
    # method 定位方法 id, class, xpath
    # attribute 元素属性 id号 class名称 xpath
    # operate 定位后的操作 点击 click 输入 input
    # params 附带参数 [ 页面名称，元素名称，输入内容（operate == input 时） ]
    def find_element(self, method, attribute, operate, params):
        time.sleep(self.sleep)
        try:
            if method == 'id':
                element = self.driver.find_element_by_id(attribute)
            elif method == 'xpath':
                element = self.driver.find_element_by_xpath(attribute)
            elif method == 'class':
                element = self.driver.find_element_by_class_name(attribute)
            elif method == 'tag':
                element = self.driver.find_element_by_tag_name(attribute)
            else:
                raise Exception
        except Exception:
            self.element_error(params[0], params[1])
        else:
            if operate == "click":
                element.click()
            elif operate == "input":
                element.clear()
                element.send_keys(params[2])
            elif operate == "text":
                return element.get_attribute('textContent').strip()
            elif operate == "value":
                return element.get_attribute('value')
            elif operate == "class":
                return element.get_attribute('class')
            else:
                pass
            return element

    def find_elements(self, method, attribute, params):
        time.sleep(self.sleep)
        try:
            if method == 'id':
                elements = self.driver.find_elements_by_id(attribute)
            elif method == 'xpath':
                elements = self.driver.find_elements_by_xpath(attribute)
            elif method == 'class':
                elements = self.driver.find_elements_by_class_name(attribute)
            elif method == 'tag':
                elements = self.driver.find_elements_by_tag_name(attribute)
            else:
                raise Exception
        except Exception:
            self.element_error(params[0], params[1])
        else:
            return elements

    # 生成测试报告
    def element_error(self, page_name, element_name):
        page_name = self.explain_page_name(page_name)
        error_msg = "页面： 【" + page_name + "】 元素： 【" + element_name + "】 无法定位。 \n"
        self.report.create_report(error_msg)

    def operate_error(self, page_name, describe):
        page_name = self.explain_page_name(page_name)
        error_msg = "页面： 【" + page_name + "】" + describe + "。 \n"
        self.report.create_report(error_msg)

    def explain_page_name(self, page_name):
        pages = page_name.split('.')
        name = ''
        config = self.modules
        for page in pages:
            if not name == '':
                name = name + ' '
            name = name + config[page]['name']
            config = config[page]['children']
        return name
