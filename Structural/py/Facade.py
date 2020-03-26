class SubSystem1:
    def operation1(self):
        print("Subsystem 1 operation 1")

    def operation2(self):
        print("Subsystem 1 operation 2")


class SubSystem2:
    def operation1(self):
        print("Subsystem 2 operation 1")

    def operation2(self):
        print("Subsystem 2 operation 2")


class Facade:
    def __init__(self):
        self._subsystem1 = SubSystem1()
        self._subsystem2 = SubSystem2()

    def operation(self):
        self._subsystem1.operation1()
        self._subsystem1.operation1()
        self._subsystem2.operation1()
        self._subsystem2.operation2()


def main():
    facade = Facade()
    facade.operation()


if __name__ == '__main__':
    main()
