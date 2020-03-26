from __future__ import annotations
from abc import ABC, abstractmethod
from random import sample
from string import ascii_letters, digits
from datetime import datetime


class Originator:
    _state = None

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: My initial state is: {self._state}")

    def do_something(self) -> None:
        print("Originator: I'm doing something important")
        self._state = self._generate_random_string(30)
        print(f"Originator: And my state has changes to {self._state}")

    def _generate_random_string(self, length: int = 10):
        return "".join(sample(ascii_letters, length))

    def save(self) -> Memento:
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento):
        self._state = memento.get_state()
        print(f"Originator: My state has change to: {self._state}")


class Memento(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass

    @abstractmethod
    def get_state(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str):
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        return self._state

    def get_name(self) -> str:
        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        return self._date


class Caretaker:
    def __init__(self, originator: Originator):
        self._originator = originator
        self._mementos = []

    def backup(self):
        print("\nCaretaker: Serving originator's state ...")
        self._mementos.append(self._originator.save())

    def undo(self):
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self):
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())


def main():
    originator = Originator("Super-duper-super-puper-super")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    print("")
    caretaker.show_history()

    print("\nClient: Now lets rollback\n")
    caretaker.undo()

    print("\nClient: Once more")
    caretaker.undo()


if __name__ == '__main__':
    main()
