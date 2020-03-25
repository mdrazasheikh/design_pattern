import abc


class AbstractAdaptee(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def request_a(self):
        pass

    @abc.abstractmethod
    def request_b(self):
        pass


class Adaptee(AbstractAdaptee):
    def request_a(self):
        return "Request to wrap a"

    def request_b(self):
        return "Request to wrap b"


class Target(metaclass=abc.ABCMeta):
    def __init__(self):
        self._adaptee = Adaptee()

    @abc.abstractmethod
    def request(self):
        pass


class Adapter(Target):
    def request(self):
        return self._adaptee.request_a() + " " + self._adaptee.request_b()


def main():
    adapter = Adapter()
    response = adapter.request()
    print(response)


if __name__ == '__main__':
    main()
