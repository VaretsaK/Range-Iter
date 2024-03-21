from typing import Iterator


class RangeIter:
    """
    Custom iterator that iterates over a range of integers.

    Args:
        start (int): The starting value of the range.
        end (int): The ending value of the range.
        step (int, optional): The step size. Defaults to 1.

    Raises:
        ValueError: If step is zero.

    Yields:
        int: The next integer in the range.
    """
    def __init__(self, start: int, end: int, step: int = 1) -> None:
        """
        Initialize the RangeIter object.

        Args:
            start (int): The starting value of the range.
            end (int): The ending value of the range.
            step (int, optional): The step size. Defaults to 1.
        """
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self) -> Iterator[int]:
        """
        Make the RangeIter object iterable.

        Returns:
            Iterator[int]: Iterator object.
        """
        return self

    def __next__(self) -> int:
        """
        Get the next integer in the range.

        Returns:
            int: The next integer in the range.

        Raises:
            StopIteration: When the end of the range is reached.
            ValueError: If step is zero.
        """
        if self.step == 0:
            raise ValueError("arg 3 must not be zero")

        elif self.step > 0:
            if self.current >= self.end:
                raise StopIteration

        elif self.step < 0:
            if self.end >= self.current:
                raise StopIteration

        value = self.current
        self.current += self.step
        return value


def main() -> None:
    """
    Main function to demonstrate the usage of RangeIter.
    """
    test_range = RangeIter(1, 11)

    for item in test_range:
        print(item)


if __name__ == '__main__':
    main()
