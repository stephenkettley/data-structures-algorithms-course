def linear_search(list: list, target: int) -> int | None:
    """Linear search of a target number in a list of numbers.

    Args:
        list (list): list of numbers to be searched.
        target (int): number being searched for.

    Returns:
        int: position of target number, returns None if not found.

    """

    for i in range(len(list)):
        if list[i] == target:
            return i

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

result = linear_search(nums, 6)
verify(result)
