import logging
import os

# class Log():
#     def __init__(self):
#        pass
#     def logger(self):
#         #初始一个日志对象并命名
#         log=logging.getLogger()
#         log.setLevel('INFO')
#         formatter =logging.Formatter('[%(asctime)s] [%(levelname)s] [%(filename)s]-->[%(lineno)d]: %(message)s')
#         # flle_path = os.path.join(os.path.dirname(__file__),'log')
#         # if os.path.exists(flle_path):
#         #     os.mkdir(flle_path)
#         # file_name =os.path.join(flle_path,logname+".txt")
#         # filehandler =logging.FileHandler(logname+".txt")
#         # filehandler.setLevel(level.upper())
#         # filehandler.setFormatter(self.formatter)
#         # self.log.addHandler(filehandler)
#
#         con_handler=logging.StreamHandler()
#         con_handler.setFormatter(formatter)
#         con_handler.setLevel('INFO')
#         log.addHandler(con_handler)
#         return log
#
#     def info(self, message):
#         log.info(message)
#
#     def debug(self, message):
#         log.debug(message)
#
#     def warning(self, message):
#         log.warning(message)
#
#     def error(self, message):
#         log.error(message)
#
#     def critical(self, message):
#         log.critical(message)

#打印行数有问题，重写或者继承解决问题
# class Log_2():
#     def __init__(self):
#         log = logging.getLogger()
#         log.setLevel('INFO')
#         formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(filename)s]-->[%(lineno)d]: %(message)s')
#         # flle_path = os.path.join(os.path.dirname(__file__),'log')
#         # if os.path.exists(flle_path):
#         #     os.mkdir(flle_path)
#         # file_name =os.path.join(flle_path,logname+".txt")
#         # filehandler =logging.FileHandler(logname+".txt")
#         # filehandler.setLevel(level.upper())
#         # filehandler.setFormatter(self.formatter)
#         # self.log.addHandler(filehandler)
#
#         con_handler = logging.StreamHandler()
#         con_handler.setFormatter(formatter)
#         con_handler.setLevel('INFO')
#         log.addHandler(con_handler)
#         self.log=log
#
#     # def logger(self):
#     #     # 初始一个日志对象并命名
#     #     log = logging.getLogger()
#     #     log.setLevel('INFO')
#     #     formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(filename)s]-->[%(lineno)d]: %(message)s')
#     #     # flle_path = os.path.join(os.path.dirname(__file__),'log')
#     #     # if os.path.exists(flle_path):
#     #     #     os.mkdir(flle_path)
#     #     # file_name =os.path.join(flle_path,logname+".txt")
#     #     # filehandler =logging.FileHandler(logname+".txt")
#     #     # filehandler.setLevel(level.upper())
#     #     # filehandler.setFormatter(self.formatter)
#     #     # self.log.addHandler(filehandler)
#     #
#     #     con_handler = logging.StreamHandler()
#     #     con_handler.setFormatter(formatter)
#     #     con_handler.setLevel('INFO')
#     #     log.addHandler(con_handler)
#     #     return log
#
#     def info(self, message):
#         return self.log.info(message)
#
#     def debug(self, message):
#         return self.log.debug(message)
#
#     def warning(self, message):
#         return self.log.warning(message)
#
#     def error(self, message):
#         return self.log.error(message)
#
#     def critical(self, message):
#         return self.log.critical(message)

class Loghandler(logging.Logger):
    def __init__(self,
                 name='root',
                 level='DEBUG',
                 file=None,
                 format='[%(asctime)s] [%(levelname)s] [%(filename)s]-->[%(lineno)d]: %(message)s'
                 ):
        super().__init__(name)
        self.setLevel(level)
        formatter = logging.Formatter(format)
        if file:
            file_hander = logging.FileHandler(file,encoding='utf-8')
            file_hander.setLevel(level)
            file_hander.setFormatter(formatter)
            self.addHandler(file_hander)
        consle_hander = logging.StreamHandler()
        consle_hander.setLevel(level)
        consle_hander.setFormatter(formatter)
        self.addHandler(consle_hander)

if __name__ == '__main__':

    # log =Log().logger()
    # log.info("这是一条测试的日志")
    # log.debug("这是一条测试的日志")
    # log.warning("这是一条测试的日志")
    # log.error("这是一条测试的日志")

    # log_1=Log_2()
    # log_1.info("这是Log_2的一条测试的日志")
    # log_1.debug("这是Log_2的一条测试的日志")
    # log_1.warning("这是Log_2的一条测试的日志")
    # log_1.error("这是Log_2的一条测试的日志")

    logger=Loghandler()
    logger.info("这是Log_2的一条测试的日志")
    logger.debug("这是Log_2的一条测试的日志")
    logger.warning("这是Log_2的一条测试的日志")
    logger.error("这是Log_2的一条测试的日志")