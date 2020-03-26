from __future__ import annotations
import abc


class Command(abc.ABC):
    @abc.abstractmethod
    def execute(self):
        pass


class SingleCommand(Command):
    def __init__(self, payload: str):
        self._payload = payload

    def execute(self):
        print(f"SimpleCommand: See, I can do simple things like printing "f"({self._payload})")


class Receiver:
    def do_something(self, a: str) -> None:
        print(f"Receiver: Working on {a}")

    def do_something_else(self, b: str):
        print(f"Receiver: Also Working on {b}")


class ComplexCommand(Command):
    def __init__(self, receiver: Receiver, a: str, b: str):
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self):
        print("ComplexCommand: Complex stuff should be done by a receiver object")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self):
        print("Invoker: Does anybody want something done before we begin?")

        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: Doing something very important")

        print("Invoker: Does anybody want anything done before we finish?")

        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


def main():
    invoker = Invoker()
    invoker.set_on_start(SingleCommand("Say Hi !!"))
    invoker.set_on_finish(ComplexCommand(Receiver(), "Send mail", "Save report"))
    invoker.do_something_important()


if __name__ == '__main__':
    main()
