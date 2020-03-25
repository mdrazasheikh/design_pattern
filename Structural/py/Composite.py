import abc


class Component(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def operation(self):
        pass


class Composite(Component):
    def __init__(self):
        self._children = set()

    def operation(self):
        print("here")
        print(self._children)
        for child in self._children:
            child.operation()

    def add(self, component: Component):
        self._children.add(component)

    def remove(self, component: Component):
        self._children.discard(component)


class Leaf(Component):
    def operation(self):
        print("Leaf")


class Leaf2(Component):
    def operation(self):
        print("Leaf 2")


def main():
    composite = Composite()
    composite.add(Leaf())
    composite.add(Leaf2())
    composite.operation()


if __name__ == '__main__':
    main()
