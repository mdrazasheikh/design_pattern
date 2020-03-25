import abc


class Component(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def operation(self):
        pass


class Decorator(Component, metaclass=abc.ABCMeta):
    def __init__(self, component: Component):
        self._component = component

    @abc.abstractmethod
    def operation(self):
        pass


class ConcreteDecoratorA(Decorator):
    def operation(self):
        print("Logic from decorator A")
        self._component.operation()


class ConcreteDecoratorB(Decorator):
    def operation(self):
        print("Logic from decorator B")
        self._component.operation()


class ConcreteComponent(Component):
    def operation(self):
        print("Final logic")


def main():
    concrete_component = ConcreteComponent()
    concrete_component_a = ConcreteDecoratorA(concrete_component)
    concrete_component_b = ConcreteDecoratorB(concrete_component_a)
    concrete_component_b.operation()


if __name__ == '__main__':
    main()
