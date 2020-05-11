from abc import ABCMeta, abstractmethod


# pythonでいうinterfaceもどき
class IValue(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, values):
        pass
