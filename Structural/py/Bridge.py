import abc


class AbstractInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def some_functionality(self):
        pass


class Bridge(AbstractInterface):

    def __init__(self):
        self._implementation = None

    def some_functionality(self):
        raise NotImplemented()


class ImplementationInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def another_functionality(self):
        pass


class Linux(ImplementationInterface):
    def another_functionality(self):
        return "Linux"


class Windows(ImplementationInterface):
    def another_functionality(self):
        return "Windows"


class UseCase(Bridge):
    def __init__(self, implementation: ImplementationInterface):
        self._implementation = implementation

    def some_functionality(self):
        return self._implementation.another_functionality()


def main():
    use_case_1 = UseCase(Linux())
    print(use_case_1.some_functionality())

    use_case_2 = UseCase(Windows())
    print(use_case_2.some_functionality())


if __name__ == '__main__':
    main()
