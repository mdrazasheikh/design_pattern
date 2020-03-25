class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instances = None

    def __call__(cls, *args, **kwargs):
        if cls._instances is None:
            cls._instances = super().__call__(*args, **kwargs)

        return cls._instances


class TestClass(metaclass=Singleton):
    pass


def main():
    c1 = TestClass()
    c2 = TestClass()

    # assert c1 is c2

    if c1 is c2:
        print("same")
    else:
        print("different")


if __name__ == '__main__':
    main()
