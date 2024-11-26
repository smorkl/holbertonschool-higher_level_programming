#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generates a Pascal's triangle of `n` rows.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list[list[int]]: A list of lists representing the Pascal's triangle.

    Raises:
        ValueError: If `n` is negative.

    Example:
        ```python
        pascal_triangle(5)
        ```
        Output:
        ```
        [[1],
         [1, 1],
         [1, 2, 1],
         [1, 3, 3, 1],
         [1, 4, 6, 4, 1]]
        ```
    """

    if n <= 0:
        raise ValueError("Number of rows must be positive")

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle