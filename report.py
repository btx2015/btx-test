# 测试报告生成类
import os
import datetime


class Report:

    def __init__(self, case):
        app_path = os.path.dirname(__file__)
        report_path = "/report/" + case + "/" + datetime.datetime.now().strftime('%Y%m%d')
        path = app_path + report_path
        if not os.path.isdir(path):
            os.makedirs(path)
        file_name = self.report_name()
        self.file_name = path + "/" + file_name

    @staticmethod
    def report_name():
        return '测试报告' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ".txt"

    def create_report(self, error_message):
        report = open(self.file_name, 'w', encoding='utf-8')
        report.writelines(error_message)
        report.close()
