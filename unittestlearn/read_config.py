from unittestlearn import data_for_config
from unittestlearn.data_for_config import Test
import os
import yaml
print("通过导入py文件的配置配置，不用类")
print(data_for_config.name)
print(data_for_config.sex)
print(data_for_config.age)
print('*'*20)
print("通过py文件导入类名使用配置，调用类名.属性名")
print(Test.name_1)
print(Test.sex_1)
print(Test.age_1)
print('*'*20)
#读取yaml中的配置数据
file = os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.yml')
with open(file,'r',encoding='utf-8') as f:
    data = yaml.load(f,Loader=yaml.FullLoader)
print(data)
print("获取host的值：",data['host'])
print("获取level的值：",data['level'])
print("获取user数据中的某个值：",data['user'][0])