#!/usr/bin/python3
"""
class VerboseList
"""


class VerboseList(list):
    """
    A class that inherits from list and provides verbose
    messages on modifications.
    """

    def __init__(self, iterable=None):
        """
        Initializes the VerboseList object.

        Args:
            iterable: An optional iterable to populate the list initially.
        """
        super().__init__(iterable)

    def append(self, value):
        """
        Appends an element to the list and prints a message.

        Args:
            value: The element to be appended.
        """
        super().append(value)
        print(f"Added [{value}] to the list")

    def extend(self, iterable):
        """
        Extends the list with elements from an iterable and prints a message.

        Args:
            iterable: An iterable containing the elements to be added.
        """
        num_added = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{num_added}] items.")

    def remove(self, value):
        """
        Removes the first item from the list with the specified
        value and prints a message.

        Args:
            value: The value of the element to be removed.

        Raises:
            ValueError: If the value is not found in the list.
        """
        if value in self:
            super().remove(value)
            print(f"Removed [{value}] from the list.")

    def pop(self, index=-1):
        removed_element = super().pop(index)
        print(f"Popped [{removed_element}] from the list.")
