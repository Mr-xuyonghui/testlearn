# -*- coding: utf-8 -*-
import urllib.request
import ssl
# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

# 创建一个密码管理者
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# 添加用户名和密码

top_level_url = "https://example.com/foo/"

# 如果知道 realm, 我们可以使用他代替 ``None``.
# password_mgr.add_password(None, top_level_url, username, password)
password_mgr.add_password(None, top_level_url, 'username', 'password')

# 创建了一个新的handler
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# 创建 "opener" (OpenerDirector 实例)
opener = urllib.request.build_opener(handler)

# 使用 opener 获取一个URL
a_url = 'https://www.python.org/'
x = opener.open(a_url)
print(x.read().decode("utf-8"))

# 安装 opener.
# 现在所有调用 urllib.request.urlopen 将用我们的 opener.
urllib.request.install_opener(opener)
