import urllib.parse

"""六个元素齐全的url"""
url = "https://jira.inkept.cn/secure/RapidBoard.jspa?rapidView=188&view=detail&selectedIssue=LOV-1120#grn"
result = urllib.parse.urlparse(url)
print("urlparse 返回类型：", type(result))
print(result)
# 通说属性名获取值
print("通过属性名称获取协议类型result.scheme:", result.scheme)
# 通过索引获取值
print("通过索引获取域名result[1]：", result[1], end='\n\n')

"""没有协议的url"""
url1 = "jira.inkept.cn/secure/RapidBoard.jspa;urst?rapidView=188&view=detail&selectedIssue=LOV-1120#grn"
result = urllib.parse.urlparse(url1)
print("urlparse 返回类型：", type(result))
print(result)
# 通说属性名获取值
print("通过属性名称获取协议类型result.scheme:", result.scheme)
# 通过索引获取值
print("通过索引获取域名result[1]：", result[1])

"""使用URLsplit解析url，忽略param，并入和path一起"""
result = urllib.parse.urlsplit(url)
print("urlsplit返回结果类型：", result)
print(result)

"""使用urlunparse 六个参数，组合url，返回一个完成url字符串"""
parts = ('https', 'jira.inkept.cn', '/secure/RapidBoard.jspa', 'urst', 'rapidView=188&view=detail&selectedIssue=LOV-1120', 'grn')
#不能使用字典类型
#parts_1= {"scheme":'', "netloc":'', "path":'jira.inkept.cn/secure/RapidBoard.jspa', "params":'urst', "query":'rapidView=188&view=detail&selectedIssue=LOV-1120', "fragment":'grn'}
reslut = urllib.parse.urlunparse(parts)
print("组合之后完整的url：", reslut)

"""使用urlunparse 五个参数，组合url，返回一个完成url字符串"""
parts = [
'https', 'jira.inkept.cn', '/secure/RapidBoard.jspa', 'rapidView=188&view=detail&selectedIssue=LOV-1120', 'grn']
reslut = urllib.parse.urlunsplit(parts)
print("组合之后完整的url：", reslut)
