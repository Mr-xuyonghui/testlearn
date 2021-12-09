import logging
import os
import sys

from selenium import webdriver
from selenium.common.exceptions import TimeoutException

# class Basepage:
#     def __init__(self, driver, load_timeout=5):
#         self.driver = driver
#         # 设置网页加载超时时间
#         self.driver.set_page_load_timeout(load_timeout)
#     def get(self,url):
#         try:
#             return self.driver.get(url)
#         except TimeoutException:
#             self.driver.execute_script("window.stop()")
class Loghandler(logging.Logger):
    def __init__(self,name=os.path.split(os.path.splitext(sys.argv[0])[0])[-1],filename=None,isstream ="True",level = "DEBUG",filemodel="w"):
        super().__init__(name)
        # self.filename = filename
        # self.isstream = isstream
        # self.level = level
        # self.filemodel = filemodel
        self.format = "'%(asctime)s | {0} - %(lineno)d | %(levelname)s  %(message)s'".format(self.name)
        #获取脚本运行文件名
        #exce_script_name =os.path.split(os.path.splitext(sys.argv[0])[0])[-1]
        logging.basicConfig(
            filename=filename,
            filemode=filemodel,
            format='%(asctime)s  %(filename)s : %(levelname)s  %(message)s',
            datefmt='%Y-%m-%d %A %H:%M:%S',
            level=level
        )
        if isstream:
            stream = logging.StreamHandler()
            stream.setLevel(level)
            stream.setFormatter(logging.Formatter(self.format))
            self.addHandler(stream)
if __name__ == '__main__':
    logger = Loghandler(filename="LOG.txt",isstream ="True")
    logger.debug("test logging")