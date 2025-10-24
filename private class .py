class myclass: 

    __private_var = 27

    def __privmath(self):
        print("i'm private math method")

    def hello(self):
        print("private variable:", self.__private_var)

foo = myclass()
foo.hello() 
foo._myclass__privmath()  