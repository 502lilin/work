#coding=UTF-8
import requests
from selenium import webdriver
from time import sleep
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
print("浏览器最大化")
driver.maximize_window()
driver.quit()
