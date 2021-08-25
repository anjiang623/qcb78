import time

from selenium import webdriver
from data import test_web_data
from common import method

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(test_web_data.url)

# 获取页面标题，验证是否符合预期
method.verify_title(driver, "柠檬ERP")

data_dict = test_web_data.data_dict
# 登录
method.login(driver, data_dict["username"], data_dict["password"])

# 判断正常登录成功
method.verify_login_sucess(driver, "测试用户")

# 零售出库菜单下搜索单据编号
method.verify_search(driver, "448")




