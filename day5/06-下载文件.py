from base import webdriver, By, time, os

# 准备配置项
options = webdriver.ChromeOptions()
download = os.path.abspath('download')
prefs = {
    'profile.default_content_settings.popups': 0,  # 取消弹窗
    'download.default_directory': download  # 设置保存位置
}
options.add_experimental_option('prefs', prefs)

# 打开浏览器，请求目标网址
driver = webdriver.Chrome(options=options)
driver.get('https://chromedriver.chromium.org/downloads')

# 操作：进行下载操作
time.sleep(6)
# 定位下载标签，然后点击
driver.find_element(By.LINK_TEXT, 'ChromeDriver 105.0.5195.52').click()

# 退出浏览器
time.sleep(100)
driver.quit()
