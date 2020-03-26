import abc


class FlyWeight(metaclass=abc.ABCMeta):
    def __init__(self):
        self.intrinsic_state = None

    @abc.abstractmethod
    def operation(self):
        pass


class ConcreteFlyWeight(FlyWeight):
    def operation(self):
        print("Some operation")


class FlyWeightFactory:
    def __init__(self):
        self._flyweights = {}

    def get_flyweights(self, key):
        try:
            flyweight = self._flyweights[key]
        except KeyError:
            flyweight = ConcreteFlyWeight()
            self._flyweights[key] = flyweight

        return flyweight


def main():
    flyweight_factory = FlyWeightFactory()
    concrete_flyweight = flyweight_factory.get_flyweights("key")
    concrete_flyweight2 = flyweight_factory.get_flyweights("key")
    concrete_flyweight3 = flyweight_factory.get_flyweights("key1")
    # print(concrete_flyweight)
    # print(concrete_flyweight2)
    # print(concrete_flyweight3)
    concrete_flyweight.operation()
    concrete_flyweight2.operation()


if __name__ == '__main__':
    main()
