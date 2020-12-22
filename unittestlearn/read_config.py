from unittestlearn import data_for_config
from unittestlearn.configHander import *
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
# with open(file,'r',encoding='utf-8') as f:
#     data = yaml.load(f,Loader=yaml.FullLoader)
# print(data)
# print("获取host的值：",data['host'])
# print("获取level的值：",data['level'])
# print("获取user数据中的某个值：",data['user'][0])
#
# case={'case':{
#     'name':'xuyonghui',
#     'age': 25
# }
# }

print(get_yml_data(file,'host'))

# #写入数据到yaml文件中
# with open(file,'a',encoding='utf-8') as f1:
#     yaml.dump(case,f1,allow_unicode=True)
#
#



ini_file=os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.ini')
# #读取ini格式配置文件
# config=ConfigParser()
# #置顶读取的文件
# config.read(ini_file,encoding='utf-8')
# #获取所有的setion
# print("打印所有的section",config.sections())
# #获取某个section下的所有key
# print("打印某个section下的所有options",config.options('user'))
# #获取某个section下的key-value
# print("打印某个section下的key-value",config.items('user'))
# #获取某个section中的parmaters
# #第一种方式获取
# a=config.get('user','name')
# #第二种方式获取
# b=config['user']['name']
# #c=config.getint('user','age')
# c=config.getfloat('user','age')
#
# print('a的值为{}，类型为{}'.format(a,type(a)))
# print('b的值为{}，类型为{}'.format(b,type(b)))
# print('c的值为{}，类型为{}'.format(c,type(c)))
# config.add_section('child2')
# config.set('child2','name','xudaxian')
# #config添加section是在原基础上添加的，这里需要用w，去覆盖现有的section，避免重复
# with open(ini_file,'w',encoding='utf-8') as f2:
#     config.write(f2)



config =ConfigHander(ini_file)
print(config.get('useraccout','name'))
#config.write_key('child3','name','xxx')git