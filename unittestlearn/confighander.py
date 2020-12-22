import os

import yaml
from configparser import ConfigParser

class confighander(ConfigParser):
    def __init__(self,file):
        super().__init__()
        self.read(file,encoding='utf-8')

def read_yaml(file,encode='utf-8'):
    with open(file,encoding=encode) as f:
        return yaml.load(f.read(),Loader=yaml.FullLoader)

if __name__ == '__main__':
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.yml')
    file_1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
    config =confighander(file_1)
    a=config.get('useraccout','name')
    print(a)
    yaml_data= read_yaml(file)
    print(yaml_data['host'])