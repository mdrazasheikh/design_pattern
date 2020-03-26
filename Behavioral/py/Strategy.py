from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def do_some_business_logic(self):
        print("Context: Sorting data using the strategy(not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))


class Strategy(ABC):
    def do_algorithm(self, data: List):
        pass


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List):
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List):
        return reversed(sorted(data))


def main():
    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting")
    context.do_some_business_logic()
    print()

    print("Client: Strategy is set to reverse sorting")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()


if __name__ == '__main__':
    main()
