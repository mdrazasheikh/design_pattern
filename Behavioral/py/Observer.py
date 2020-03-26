from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ConcreteSubject(Subject):
    _state: int = None
    _observer: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer")
        self._observer.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observer.remove(observer)
        print("Subject: Detached an observer")

    def notify(self) -> None:
        for observer in self._observer:
            observer.update(self)

    def some_business_logic(self):
        print("\nSubject: I am doing something important")
        self._state = randrange(0, 10)

        print(f"Subject: My state has changed to {self._state}")
        self.notify()


class Observer(ABC):
    def update(self, subject: Subject):
        pass


class ConcreteObserverA(Observer):
    def update(self, subject: Subject):
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to an event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject):
        if subject._state == 3 and subject._state >= 2:
            print("ConcreteObserverB: Reacted to an event")


def main():
    subject = ConcreteSubject()
    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()


if __name__ == '__main__':
    main()
