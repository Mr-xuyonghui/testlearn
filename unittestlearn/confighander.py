from configparser import ConfigParser
import yaml
class ConfigHander(ConfigParser):
    def __init__(self,file):
        super().__init__()
        self.file = file
        self.read(file,encoding='utf-8')
    def write_key(self,section,key,value):
        self.add_section(section)
        self.set(section,key,value)
        with open(self.file,'a',encoding='utf-8') as f:
            self.write(f)

#yaml读取和写入
def get_yml_data(file,key):
    with open(file,'r',encoding='utf-8') as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        return data[key]

def write_yml_data(file,case):
    with open(file, 'a', encoding='utf-8') as f1:
        yaml.dump(case, f1, allow_unicode=True)
