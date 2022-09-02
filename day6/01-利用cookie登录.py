from base import webdriver, time

# 打开浏览器， 请求目标网址
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# TODO 设置cookie，实现登录
cookies = [
    {
        'name': 'BDUSS',
        'value': 'FmOFdTTGhXYnZNd0plNUt4bHM0akFDWlJnYkFuci1YSUNKdkczWjhVQlk3RGhqSVFBQUFBJCQAAAAAAAAAAAEAAABmRcgnyvOx6rXmZGQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFhfEWNYXxFjMH'
    },
    {
        'name': 'BDUSS_BFESS',
        'value': 'FmOFdTTGhXYnZNd0plNUt4bHM0akFDWlJnYkFuci1YSUNKdkczWjhVQlk3RGhqSVFBQUFBJCQAAAAAAAAAAAEAAABmRcgnyvOx6rXmZGQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFhfEWNYXxFjMH'
    }
]
for cookie in cookies:
    driver.add_cookie(cookie)

# 浏览器刷新
driver.refresh()

# 退出浏览器
time.sleep(10)
driver.quit()
