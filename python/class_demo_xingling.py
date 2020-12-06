#初始化菱形问题
#Phone类和Computer类都继承了Electrical类，HuaWei类既继承了Phone类又继承了Computer类，就形成了一个菱形的继承关系。
# class Electrical(object):
#
#     def __init__(self, name):
#         self.name = name
#         print('Electrical init')
#
#
# class Phone(Electrical):
#
#     def __init__(self, name, price):
#         Electrical.__init__(self, name)
#         self.price = price
#         print('Phone init')
#
#
# class Computer(Electrical):
#
#     def __init__(self, name, config):
#         Electrical.__init__(self, name)
#         self.config = config
#         print('Computer init')
#
#
# class HuaWei(Phone, Computer):
#
#     def __init__(self, name, price, config):
#         Phone.__init__(self, name, price)
#         Computer.__init__(self, name, config)
#         print('HuaWei init')
#
# h = HuaWei('huawei', 100, 'i7')
# print("huawei类的继承顺序",HuaWei.__mro__)
"""
在创建HuaWei类对象时，Electrical类的__init__方法执行了两遍，
也就是说在Phone类向上继承时执行了，
在Computer类向上继承时也执行了，
这显然是不应该发生的。
如何避免顶层父类中的某个方法被多次调用呢，
此时就需要super()来发挥作用了,super本质上是一个类，内部记录着MRO信息，
由于C3算法确保同一个类只会被搜寻一次，这样就避免了顶层父类中的方法被多次执行了，上面代码可以改为
"""


class Electrical(object):
    def __init__(self, name):
        self.name = name
        print('Electrical init')

class Phone(Electrical):
    def __init__(self, price, *args):
        super(Phone, self).__init__(*args)
        self.price = price
        print('Phone init')

#在Phone类和Computer类中给super()后的init方法传参数时，应使用*args
#因为HuaWei有三个参数，但是Phone类和Computer类都只有两个参数，所以参数个数不正确会报错
class Computer(Electrical):
    def __init__(self, config, *args):
        super(Computer, self).__init__(*args)
        self.config = config
        print('Computer init')

class HuaWei(Phone, Computer):
    def __init__(self, name, price, config):
        #super(HuaWei, self).__init__(name, price, config)
        # 继承的时候如根据继承的顺序入参，父类入参使用多少个参数，继承传递参数就相应减少多少个参数
        # 子类的入参顺序需与调用父类参数对应
        # 先调用phone父类，其参数为price,spuer时price应该在前面
        super(HuaWei, self).__init__(price, config, name)
        print('HuaWei init')

print("通过spuer（）解决顶层类重复调用问题")
h = HuaWei('huawei', 100, 'i7')
print("name:",h.name)
print("price:",h.price)
print("cofig:",h.config)


class Electrical(object):

    def chat(self):
        print('Chat with friend in electrical!')

    def watch_movie(self):
        print('Watch movie in electrical!')

    def game(self):
        print('Play game in electrical!')


class Phone(Electrical):

    def game(self):
        print('Play game in phone!')


class Computer(Electrical):

    def watch_movie(self):
        print('Watch movie in computer!')

    def game(self):
        print('Play game in computer!')


class HuaWei(Phone, Computer):
    pass


h = HuaWei()
h.game()
h.watch_movie()
h.chat()