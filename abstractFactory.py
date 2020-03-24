import abc


class AbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_product_a(self):
        pass

    @abc.abstractmethod
    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()


class AbstractProductA(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def info_a(self):
        pass


class AbstractProductB(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def info_b(self):
        pass


class ConcreteProductA1(AbstractProductA):
    def info_a(self):
        print("This is product A1")


class ConcreteProductA2(AbstractProductA):
    def info_a(self):
        print('This is product A2')


class ConcreteProductB1(AbstractProductB):
    def info_b(self):
        print("This is product B1")


class ConcreteProductB2(AbstractProductB):
    def info_b(self):
        print("This is product B2")


def main():
    create_product(ConcreteFactory1())
    create_product(ConcreteFactory2())


def create_product(factory: AbstractFactory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    product_a.info_a()
    product_b.info_b()


if __name__ == "__main__":
    main()
