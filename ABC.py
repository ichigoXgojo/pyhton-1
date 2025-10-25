from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    
 def print(self,x):
        print("passed value:", x )

 @abstractmethod
 def task(self):   
    
    print("we are in MyAbstractClass class task")

class test_class(MyAbstractClass):
    def task(self):
        print(" we are inside my test_class")

test_obj = test_class()
test_obj.task()
test_obj.print(100)  

