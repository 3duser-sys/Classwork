from abc import ABC, abstractmethod

class Absclass(ABC):

    def print(self,x):
        print("Passed value: ", x)

    @abstractmethod
    def task(self):
        print("Nobody ruled better, were the Absclass taskers")

class test_class(Absclass):
    def task(self):
        print("Were so inside the test class task,")

test_obj = test_class()
test_obj.task()
test_obj.print(100)