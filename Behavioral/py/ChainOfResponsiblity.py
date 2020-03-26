from __future__ import annotations
import abc
import typing


class Handler(abc.ABC):

    @abc.abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    def handle(self, request) -> typing.Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request: typing.Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class MonkeyHandler(AbstractHandler):
    def handle(self, request: typing.Any) -> str:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: typing.Any) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: typing.Any) -> str:
        if request == "Bone":
            return f"Dog: I'll chew the {request}"
        else:
            return super().handle(request)


def main():
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()
    monkey.set_next(squirrel).set_next(dog)

    print("Chain: Monkey > Squirrel > Dog")

    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"Client: Who want a {food} ?")
        result = monkey.handle(food)
        if result:
            print(f"{result}")
        else:
            print(f"{food} was untouched")

    print("\n")
    print("Chain: Squirrel > Dog")

    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"Client: Who want a {food} ?")
        result = squirrel.handle(food)
        if result:
            print(f"{result}")
        else:
            print(f"{food} was untouched")


if __name__ == '__main__':
    main()
