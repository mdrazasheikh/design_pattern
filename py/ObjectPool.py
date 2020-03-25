class Reusables:
    pass


class ReusablePool:
    def __init__(self, size):
        self._reusables = [Reusables() for _ in range(0, size)]
        # print(self._reusables)

    def acquire(self):
        res = self._reusables.pop()
        # print(self._reusables)
        return res

    def release(self, reusable):
        # print(self._reusables)
        self._reusables.append(reusable)
        # print(self._reusables)


def main():
    reusable_pool = ReusablePool(10)
    reusable = reusable_pool.acquire()
    # print(reusable)
    reusable_pool.release(reusable)


if __name__ == '__main__':
    main()
