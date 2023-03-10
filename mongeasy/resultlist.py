"""
This module contains the ResultList class that adds extra features to lists.

MIT License

Copyright (c) 2023 Joakim Wassberg

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation 
files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, 
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom 
the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import functools
import random


class ResultList(list):
    """
    Extends the list class with methods to retrieve the first or last value,
    or None if the list is empty, and additional methods for filtering,
    mapping, reducing, sorting, grouping, and selecting a random element.
    This class is used as a return value for returned documents
    """

    def first_or_none(self):
        """
        Return the first value or None if list is empty
        :return: First list element or None
        """
        return self[0] if len(self) > 0 else None
    
    def first(self):
        """
        Return the first value or None if list is empty
        Synonym for first_or_none
        :return: First list element or None
        """
        return self.first_or_none()

    def last_or_none(self):
        """
       Return the last value or None if list is empty
       :return: Last list element or None
       """
        return self[-1] if len(self) > 0 else None

    def last(self):
        """
        Return the last value or None if list is empty
        Synonym for last_or_none
        :return: Last list element or None
        """
        return self.last_or_none()
    
    
    def filter(self, predicate):
        """
        Return a new ResultList containing only elements that match a given predicate function
        :param predicate: A function that takes an element and returns a boolean value
        :return: A new ResultList containing only matching elements
        """
        return ResultList(filter(predicate, self))

    def map(self, mapper):
        """
        Apply a given function to each element in the list and return a new ResultList containing the results
        :param mapper: A function that takes an element and returns a new value
        :return: A new ResultList containing the results of applying the mapper function to each element
        """
        return ResultList(map(mapper, self))

    def reduce(self, reducer, initial=None):
        """
        Reduce the list to a single value using a given reducer function
        :param reducer: A function that takes two elements and returns a single value
        :param initial: An optional initial value to start the reduction
        :return: The final reduced value
        """
        if initial is not None:
            return functools.reduce(reducer, self, initial)
        else:
            return functools.reduce(reducer, self)

    def sort(self, key=None, reverse=False):
        """
        Sort the list in place using a given sorting function
        :param key: A function that takes an element and returns a value to sort by
        :param reverse: A boolean indicating whether to sort in descending order (default is ascending)
        :return: None
        """
        super().sort(key=key, reverse=reverse)

    def group_by(self, keyfunc):
        """
        Group the elements in the list by a given key function and return a dictionary where the keys are the group keys
        and the values are lists of elements in that group.
        :param keyfunc: A function that takes an element and returns a key to group by
        :return: A dictionary of group keys and lists of elements in each group
        """
        groups = {}
        for elem in self:
            key = keyfunc(elem)
            if key in groups:
                groups[key].append(elem)
            else:
                groups[key] = [elem]
        return groups

    def random(self):
        """
        Return a random element from the list
        :return: A random element from the list
        """
        return random.choice(self)
