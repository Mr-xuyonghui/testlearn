import logging
import os
import sys
import pymysql

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
    def __init__(self, name=os.path.split(os.path.splitext(sys.argv[0])[0])[-1], filename=None, isstream="True",
                 level="DEBUG", filemodel="w"):
        super().__init__(name)
        # self.filename = filename
        # self.isstream = isstream
        # self.level = level
        # self.filemodel = filemodel
        self.format = "'%(asctime)s | {0} - %(lineno)d | %(levelname)s  %(message)s'".format(self.name)
        # 获取脚本运行文件名
        # exce_script_name =os.path.split(os.path.splitext(sys.argv[0])[0])[-1]
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


class SqlHandler():
    def __init__(self, host, uesr, password, dbname, charset="utf8", connect_timeout=120):
        self.host = host
        self.uesr = uesr
        self.password = password
        self.dataname = dbname
        # self.port = port,
        self.charset = charset
        self.connect_timeout = connect_timeout

    def get_conn(self, curtye=pymysql.cursors.Cursor):  # 建立数据连接
        self.conn = pymysql.connect(host=self.host, user=self.uesr, password=self.password, database=self.dataname,charset=self.charset, connect_timeout=self.connect_timeout)
        self.cursor = self.conn.cursor(cursor=curtye)
        print("数据库已链接")
        # return self.conn, self.cursor

    def close_conn(self):  # 关闭数据库连接
        # self.cursor.commit()
        self.cursor.close()
        self.conn.close()
        print("已关闭数据库连接")

    def rcollback(self):  # 回滚操作
        self.conn.rollback()
        self.cursor.close()
        self.conn.close()

    def get_one(self, sql, *param):  # 获取单个值
        try:
            self.get_conn()
            self.cursor.execute(sql,*param)
            result = self.cursor.fetchone()
            self.close_conn()
            return result
        except Exception as e:
            print(e)

    def get_all(self, sql, *param):  # 获取结果集中所有值
        try:
            self.get_conn()
            self.cursor.execute(sql, *param)
            result = self.cursor.fetchall()
            self.close_conn()
            return result
        except Exception as e:
            print(e)

    def get_inti_size(self, size, sql, *param):  # 获取指定数量
        try:
            self.get_conn()
            self.cursor.execute(sql, *param)
            result = self.cursor.fetchmany(size=size)
            self.close_conn()
            return result
        except Exception as e:
            print(e)

    def update_data(self, sql, *param):
        try:
            self.get_conn()
            self.cursor.execute(sql, *param)
            self.conn.commit()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    logger = Loghandler(filename="LOG.txt", isstream="True")
    logger.debug("test logging")
