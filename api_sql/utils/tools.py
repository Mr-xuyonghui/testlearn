import hashlib
import logging
from datetime import datetime, timedelta
import json
import random
import qrcode
from time import time
import os
import jwt
from config import api_env, DOMAINS, ENV_API


def make_dates(beginDate, fromat="%Y-%m-%d"):
    endDate = endDate = datetime.now().strftime(fromat)
    dateList = []
    dt = datetime.strptime(beginDate, fromat)
    date = beginDate[:]
    while date <= endDate:
        dateList.append(date)
        dt = dt + timedelta(1)
        date = dt.strftime(fromat)
    return dateList


def cryptograph_text(text):
    """md5(text)."""
    logging.info(text)
    m = hashlib.md5()
    m.update(text.encode('utf-8'))
    return m.hexdigest()


def get_json_lines(filename: str, offsetlines=0, endlines=-1):
    get_file_data(filename, is_json=True,
                  offsetlines=offsetlines, endlines=endlines)


def get_data_lines(filename: str, has_title=False, offsetlines=0, endlines=-1):
    get_file_data(filename, has_title=has_title,
                  offsetlines=offsetlines, endlines=endlines)


def get_file_data(filename: str, has_title=False, offsetlines=0, endlines=-1, is_json=False):
    with open(filename, 'r') as f:
        lines = f.readlines()
        if not lines:
            print('%s 文件没内容' % filename)
            return None
    if is_json:
        has_title = False
    if has_title:
        title = lines[0].rstrip(os.linesep).split(',')
        length = len(title)
        if offsetlines != 0:
            offsetlines = 1
        is_json = False
    for i in range(len(lines)):
        if i < offsetlines:
            continue
        if i == endlines:
            break
        else:
            value = lines[i].rstrip(os.linesep).split(',')
            if has_title:
                yield zip(title, value)
            elif is_json:
                yield(json.loads(lines[i].rstrip(os.linesep)))
            else:
                yield value


options = ['-s', '-name']


def Modified_suffix(filename):
    """对无后缀的的文件追加后缀png."""
    try:
        if int is type(filename):
            filename = str(filename)
        if filename.split('.')[-1] not in ['png', 'jpg', 'gif', 'svg', 'jepg']:
            filename = filename + '.png'
    except AttributeError:
        logging.warning('filename错误,使用时间命名')
    return filename


def text_to_qr(text='https://www.youcheyihou.com/', is_show=False, save_filename='', txt_filename='', is_tty=False):
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=8,
                       border=8,
                       )
    if txt_filename:
        with open(txt_filename, 'r') as f:
            text = f.read()
    qr.add_data(text)
    qr.make(fit=True)
    if is_tty:
        print()
        qr.print_tty()
        print()
    if is_show:
        img = qr.make_image()
        img.save(Modified_suffix(save_filename))
        img.show()
    logging.debug('code url is ', text)


def url(url: str, api_env=api_env, domain='suv', protocol='http://'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            full_url = protocol + DOMAINS[domain].value + \
                ENV_API[api_env].value + "/" + url.lstrip('/')
            ret = func(full_url, *args, **kwargs)
            return ret
        return wrapper
    return decorator


def get_uid_by_token(token, algorithm='HS256', salt=''):
    """ 通过token解析uid. """
    if not salt:
        payload = jwt.decode(token, '', False, algorithm=algorithm)
    else:
        payload = jwt.decode(token, salt, True, algorithm=algorithm)
    return payload['uid']


def checkParameters(kwargs, defParameters):
    for k in kwargs:
        defParameters[k] = kwargs[k]
    return defParameters


if __name__ == "__main__":
    pass
