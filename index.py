# 分仓测试
# 启动脚本

import importlib
from pager import Pager
from report import Report


# 调度器
def dispatch(page, pages, level=1):
    if not page == '':
        page = page + '.'
    for page_name in pages:
        next_page = page + page_name
        print(next_page)
        if level == 1:
            pager.get("/#/" + page_name)
        if 'children' not in pages[page_name]:
            pages[page_name]['children'] = {}
            case = importlib.import_module('apps.' + app + '.' + next_page)
            test = case.Module(pager, next_page)
            test.test()
        else:
            next_level = level + 1
            dispatch(next_page, pages[page_name]['children'], next_level)


# localhost = input('Please input the localhost:')

localhost = "http://localhost:8080"
app = 'zg'

# 引入测试用例配置
lib = importlib.import_module('config.' + app)
modules = lib.get_modules()

# 实例化测试报告类
report = Report(app)
# 实例化 web driver 重构类
pager = Pager(report, localhost, modules)
pager.get('')

print('# # # # # TEST START # # # # #')
dispatch('', modules)
print('# # # # # TEST COMPLETE # # # # # \n')

input(report.file_name)
