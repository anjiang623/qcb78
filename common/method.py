import time
# 验证标题
def verify_title(driver, title):
    if driver.title == title:
        print("页面标题验证通过")
    else:
        print("页面标题验证不通过")

# 登录
def login(driver, username, password):
    # 获取账号输入文本框，并输入账号
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
    # 获取密码输入文本框，并输入密码
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    # 找到立即登录按钮，并点击
    driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()

# 判断正常登录成功
def verify_login_sucess(driver, name):
    # 获取页面中的用户名，判断是否和预期一致
    page_name = driver.find_element_by_xpath('//*[@class="pull-left info"]/p').text
    if page_name == name:
        print("正常登录成功")
    else:
        print("登录失败")

# 验证零售出库搜索功能
def verify_search(driver,number):
    # 验证点击菜单能正常打开
    # 点击第1级菜单下的第1个零售出库，验证能否正常打开
    driver.find_element_by_xpath('//*[text()="零售出库"]').click()
    # 切换iframe
    li_id = driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id")
    iframe_id = li_id + "-frame"
    print(iframe_id)
    driver.switch_to.frame(iframe_id)

    # 点击搜索框，输入448，点击查询
    driver.find_element_by_xpath('//*[@id="searchNumber"]').send_keys(number)
    driver.find_element_by_xpath('//span[text()="查询"]').click()
    # 检查搜索结果是否正确
    # 获取单据编号的号码
    time.sleep(2)
    num = driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text
    if number in num:
        print("搜索用例通过")
        print(num)
    else:
        print("搜索用例失败")