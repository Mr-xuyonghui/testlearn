class Anaimal():
    color = 'red'
    def run(self):
        print("animal is runing")

if __name__ == '__main__':
    def go(self,name):
        """
        定义类的实例方法
        必须有self，和在class中定义一致
        """
        print("{name} is going".format(name=name))
    def eat(self,name):
        """
        定义类的实例方法
        必须有self，和在class中定义一致
        """
        print("{name} is eating".format(name=name))
    cat = type('Cat',(Anaimal,),{'color':'red','go':go,'eat':eat})
    c =cat()
    print(c.color)
    c.run()
    c.go('xiaobai')
    c.eat('xiaobai')