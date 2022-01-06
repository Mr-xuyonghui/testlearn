"""被装饰函数没有参数没有返回值"""


def set_func(fun):
    def call_func():
        print("-----闭包函数----")
        print("参数fun的值为{} ".format(fun))
        fun()

    return call_func


@set_func
def myDef():
    print("----runing----")


"""
被装饰函数有参数没有返回值
内部函数形参需要要被装饰函数形参一致，内部函数调用被装饰函数也需要一致
"""


def set_func_01(fun):
    def call_func_01(num, *args, **keyword):
        print("-----闭包函数----")
        print("参数fun的值为{} ".format(fun))
        print("被装饰函数参数为{}".format(num))
        fun(num, *args, **keyword)

    return call_func_01


@set_func_01
def myDef_01(num, *args, **keyword):
    print("----runing----")


"""
被装饰函数有参数有返回值
内层函数需要return被装饰函数的调用过程
"""


def set_func_02(fun):
    def call_func_02(num, *args, **keyword):
        print("-----闭包函数----")
        print("参数fun的值为{} ".format(fun))
        print("被装饰函数参数为{}".format(num))
        return fun(num, *args, **keyword)

    return call_func_02


@set_func_02
def myDef_02(num, *args, **keyword):
    print("----runing----")
    return num


"""
被装饰函数没有参数有返回值，内场函数需要返回被装饰函数调用过程
"""


def set_func_03(fun):
    def call_func_03():
        print("-----闭包函数----")
        print("参数fun的值为{} ".format(fun))
        return fun()

    return call_func_03


@set_func_03
def myDef_03():
    print("----runing----")
    return 30


"""
有参数的函数装饰器，需要定义三层函数，且必须有返回值
"""


def set_para(para, *args, **keyword):
    print("---这是第一层功函数----")
    print("这是第一层函数的para参数:{}".format(para))
    print("这是第一层函数的args参数:{}".format(args))
    print("这是第一层函数的keyword参数:{}".format(keyword))

    def set_func_04(fun):
        print("-----这是第二层函数-----")

        def call_func_04():
            print("----这是第三层函数----")
            print("参数fun的值为{} ".format(fun))
            return fun()

        return call_func_04

    return set_func_04


@set_para('10', 'python')
def myDef_04():
    print("----runing----")
    return 30


class Decorator:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, num, *args, **keyword):
        res = self.fun(num, *args, **keyword)
        return res


@Decorator
def myDef_06(num, *args, **keyword):
    print('-----runing----')
    return num


class Decorator_01:
    #接受装饰器参数
    def __init__(self, para):
        self.para = para
    #接受被装饰函数
    def __call__(self, fun):
        print("类定义装饰器参数为：{}".format(self.para))
        #调用被被装饰函数
        def wapper(num, *args, **keyword):
            res = fun(num, *args, **keyword)
            return res
        return wapper


@Decorator_01("hello")
def myDef_07(num, *args, **keyword):
    print('-----runing----')
    return num


#if __name__ == "__main__":
    # #没有参数和返回值
    # myDef()
    # #有参数没有返回值
    # myDef_01(10)
    # #有参数有返回值
    # print(myDef_02(20))
    # #没有参数有返回值
    # print(myDef_03())
    # #多个装饰器
    # print(myDef_04())
    #无参数了定义装饰器
    # print(myDef_06(50))
    #有参数类定义装饰器
    #print(myDef_07('60'))