from enum import Enum, unique
import logging

mysql_config = 'test'
api_env = 'test'
DOMAIN = 'suv'


def show_config():
    logging.info('server config is {} mysql server is {}  api_suffix is {}'.format(
        mysql_config, MYSQL_CONFIG[mysql_config].value[0], ENV_API[api_env].value))


def set_env(target_env='test', target_pro_server=''):
    """切换预置环境. """
    global api_env
    global mysql_config
    if 'pro' == target_env and target_pro_server:
        mysql_config = target_pro_server
    else:
        mysql_config = target_env
    api_env = target_env
    return mysql_config, api_env


@unique
class ENV_API(Enum):
    test = '/testapi'
    release = '/releaseapi'
    pro = '/'


@unique
class DOMAINS(Enum):
    iyc = 'api.s.youcheyihou.com'
    suv = 'api.s.suv666.com'


@unique
class MYSQL_CONFIG(Enum):
    test = {
        "server": "192.168.6.27",
        "port": 3306,
        "username": "iyc_test",
        "password": "Iyourcar88"
    },
    release = {
        "server": "mysql-release01-gz.lc",
        "port": 3306,
        "username": "iyc_test",
        "password": "Iyourcar88"
    }
    pro_autobuy = {
    }