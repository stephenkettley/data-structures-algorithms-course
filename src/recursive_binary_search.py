def recursive_binary_search(list: list, target: int) -> bool:
    """Recursive binary search algorithm.

    Args:
        list (list): list of numbers being searched through.
        target (int): target number being searched for.

    Returns:
        bool: true/false on whether the number was found or not.

    """
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1 :], target)
            else:
                return recursive_binary_search(list[: midpoint - 1], target)


def verify(result: bool) -> None:
    """Verify the result of a recursive binary search algorithm.

    Args:
        result (bool): true/false result from algorithm to be printed.

    """

    print("Target found:", result)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = recursive_binary_search(nums, 14)
verify(result)
