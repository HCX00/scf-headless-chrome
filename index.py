# -*- coding: utf8 -*-
import os
import stat
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main_handler(event, context):
    # 复制文件到 /tmp 并赋执行权限
    shutil.copytree('./chromedriver', '/tmp/chromedriver')
    files = ['/tmp/chromedriver/' + filename for filename in os.listdir('/tmp/chromedriver/')]
    for filepath in files:
        os.chmod(filepath, os.stat(filepath).st_mode | stat.S_IXUSR)

    # 设置 chrome
    options = Options()
    options.binary_location = '/tmp/chromedriver/headless-chromium-tencent'
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    browser = webdriver.Chrome('/tmp/chromedriver/chromedriver', chrome_options=options)
