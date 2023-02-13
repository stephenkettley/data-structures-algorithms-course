def binary_search(list: list, target: int) -> int | None:
    """Binary search algorithm.

    Args:
        list (list): list with numbers to be searched.
        target (int): target number.

    Return:
        int: position of the target number in the list. None if not found.

    """

    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2  # floor division
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None


def verify(index: int) -> None:
    """Verifies if number was found in a list or not.

    Args:
        index (int): index of target number.

    """
    if index is not None:
        print(f"Target found at index {index}")
    else:
        print("Target not found.")


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(nums, 1)
verify(result)
