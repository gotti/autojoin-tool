from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
import time
import os

#username = input("input your username\n")
#password = getpass.getpass("input your password\n")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
target = os.getenv("TARGET")

options = webdriver.firefox.options.Options()
options.add_argument("--headless")
options.set_preference("network.proxy.type", 1)
options.set_preference("network.proxy.socks", "proxy")
options.set_preference("network.proxy.socks_port", 1080)

driver = webdriver.Firefox(options=options)
driver.get(target)
#wait = WebDriverWait(driver, 10)
#wait.until(expected_conditions.url_to_be("https://shibboleth.cc.uec.ac.jp/idp/profile/SAML2/Redirect/SSO?execution=e1s1"))
time.sleep(4)

windows = driver.window_handles

driver.find_element(by=By.CLASS_NAME, value="showLoginButton").click()

time.sleep(2)

new_window = driver.window_handles

driver.switch_to.window(list(set(new_window)-set(windows))[0])

driver.find_element(by=By.ID, value="username").send_keys(username)
driver.find_element(by=By.ID, value="password").send_keys(password)
driver.find_element(by=By.CLASS_NAME, value="form-button").click()
time.sleep(1)

driver.find_element(by=By.LINK_TEXT, value="» 2022 コンピュータネットワーク-高田-火4").click()

time.sleep(2)

driver.find_element(by=By.LINK_TEXT, value="出席").click()

time.sleep(2)

tableElm = driver.find_element(by=By.CSS_SELECTOR, value="table.table-striped")

l = tableElm.find_elements(by=By.CSS_SELECTOR, value="tr.odd")

for e in l:
    # 出席済み
    if e.text.count("出席") == 3:
        continue
    print("Try submitting...: ", e.text)
    e.find_element(by=By.TAG_NAME, value="a").click()
    break

exit(1)
