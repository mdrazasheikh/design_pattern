import abc


class Subject(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def request(self):
        pass


class RealSubject(Subject):
    def request(self):
        print("From the real subject")


class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self):
        self._real_subject.request()


def main():
    proxy = Proxy(RealSubject())
    proxy.request()


if __name__ == '__main__':
    main()
