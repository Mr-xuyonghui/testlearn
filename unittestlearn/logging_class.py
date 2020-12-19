import logging
import os

class Log():
    def logger(self):
        #初始一个日志对象并命名
        log=logging.getLogger()
        log.setLevel('INFO')
        formatter =logging.Formatter('[%(asctime)s] [%(levelname)s] [%(filename)s]-->[%(lineno)d]: %(message)s')
        # flle_path = os.path.join(os.path.dirname(__file__),'log')
        # if os.path.exists(flle_path):
        #     os.mkdir(flle_path)
        # file_name =os.path.join(flle_path,logname+".txt")
        # filehandler =logging.FileHandler(logname+".txt")
        # filehandler.setLevel(level.upper())
        # filehandler.setFormatter(self.formatter)
        # self.log.addHandler(filehandler)

        con_handler=logging.StreamHandler()
        con_handler.setFormatter(formatter)
        con_handler.setLevel('INFO')
        log.addHandler(con_handler)
        return log

    def info(self, message):
        log.info(message)

    def debug(self, message):
        log.debug(message)

    def warning(self, message):
        log.warning(message)

    def error(self, message):
        log.error(message)

    def critical(self, message):
        log.critical(message)
if __name__ == '__main__':

    log =Log().logger()
    log.info("这是一条测试的日志")
    log.debug("这是一条测试的日志")
    log.warning("这是一条测试的日志")
    log.error("这是一条测试的日志")