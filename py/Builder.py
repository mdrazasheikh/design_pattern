import abc


class Product:
    def __init__(self):
        self._part_a = None
        self._part_b = None

    def set_part_a(self, part_a):
        self._part_a = part_a

    def set_part_b(self, part_b):
        self._part_b = part_b


class Builder(metaclass=abc.ABCMeta):
    def __init__(self):
        self.product = Product()

    @abc.abstractmethod
    def build_part_a(self):
        pass

    @abc.abstractmethod
    def build_part_b(self):
        pass


class ConcreteBuilder1(Builder):
    def build_part_a(self):
        print("Builder 1 : Part A is built")

    def build_part_b(self):
        print("Builder 1 : Part B is built")


class ConcreteBuilder2(Builder):
    def build_part_a(self):
        print("Builder 2 : Part A is built")

    def build_part_b(self):
        print("Builder 2 : Part B is built")


class Director:
    def __init__(self):
        self._builder = None

    def set_product_builder(self, builder: Builder):
        self._builder = builder

    def build_product(self):
        self._builder.build_part_a()
        self._builder.build_part_b()


def main():
    director = Director()
    director.set_product_builder(ConcreteBuilder1())
    director.build_product()
    director.set_product_builder(ConcreteBuilder2())
    director.build_product()


if __name__ == "__main__":
    main()
