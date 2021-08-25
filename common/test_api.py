"""
1、从excel表中读取测试用例数据
2、发送请求
3、对比期望结果和实际结果
4、把结果写到excel表中


"""

from common import send_requests
from common import read_excel


# 读取测试用例
excel_path = "../data/test_case_api.xlsx"
excel_sheet = "login"
cases = read_excel.read_cases(excel_path, excel_sheet)

# 发送请求并断言
head = {"X-Lemonban-Media-Type":"lemonban.v2", "Content-Type":"application/json"}
results = send_requests.post_request(cases, head)

# 把结果写到excel表格中
read_excel.write_cases(excel_path, excel_sheet, results)