from socket import gethostbyname, error
import re

# 域名解析


def parsing_domain_name(domainName):
    '''
    :param: str domainName 域名或者IP
    :return: type:str ip address
    '''
    p = re.compile(
        '^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(domainName):
        return domainName
    try:
        # 解析百度的域名所对应的ip，gethostbyname主要解析单个域名
        hostip = gethostbyname(domainName)
    except error as e:
        print("gethostbyname failed")
        hostip = domainName
    return hostip


if __name__ == "__main__":
    domain = 'www.baidu.com'
    parsing_domain_name(domain)
