# class Daolao():
#     t="这是一个变量"
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print("大佬的名字：{}".format(self.name))
#     @staticmethod
#     def show_2():
#         print("静态方法")
#     def show_3(self):
#         print("通过类调用方法")
#         self.show()
#     @classmethod
#     def show_4(cls):
#         print("这是一个类方法")
#         print(cls.t)
#
# dalao=Daolao("许永辉")
# dalao.show()
# #不能通过类调用实例方法
# #Daolao.show_3()
# dalao.show_3()
# #可以通过类调用静态方法
# Daolao.show_2()
# #通过实例调用类方法
# dalao.show_4()
# #通过类调用类方法
# Daolao.show_4()

#类方法
# class ClassTest(object):
#     __num = 0
#
#     @classmethod
#     def addNum(cls):
#         cls.__num += 1
#
#     @classmethod
#     def getNum(cls):
#         return cls.__num
#
#     # 这里我用到魔术函数__new__，主要是为了在创建实例的时候调用人数累加的函数。
#     def __new__(self):
#         ClassTest.addNum()
#         return super(ClassTest, self).__new__(self)
#
#
# class Student(ClassTest):
#     def __init__(self):
#         self.name = ''
#
# a = Student()
# b = Student()
# print(ClassTest.getNum())


class Praent():
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
    def show(self):
        print("全名",self.firstname+self.lastname)

class Son(Praent):
    def __init__(self,firstname,lastname,habby):
        #通过super()继承不用self
        #super().__init__(firstname,lastname)
        Praent.__init__(self,firstname,lastname)
        self.habby=habby
    def show_name(self):
        print("调用父类的show")
        super().show()
    def show_habby(self):
        print("habby: ",self.habby)

son=Son("许","永辉","游戏")
son.show_name()
son.show_habby()