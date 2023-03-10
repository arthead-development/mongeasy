"""
This module contains misc util functions.

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
from typing import Union
from .resultlist import ResultList

def snake_to_pascal(s: str):
    """
    Convert a snake_case string to PascalCase.

    Example:
    snake_to_pascal('my_snake_string') -> 'MySnakeString'
    """
    words = s.split('_')
    return ''.join(w.capitalize() for w in words)


def pascal_to_snake(s: str):
    """
    Convert a PascalCase string to snake_case.

    Example:
    pascal_to_snake('MyPascalString') -> 'my_pascal_string'
    """
    result = ''
    for i, c in enumerate(s):
        if i == 0:
            result += c.lower()
        elif c.isupper():
            result += '_' + c.lower()
        else:
            result += c
    return result

def create_subdocuments(doc_obj: Union[dict, list], subdocument_class, list_class) -> Union[dict, ResultList]:
    """
    Recursively traverses a dictionary and creates subdocument objects for nested dictionaries
    and ResultList objects for nested lists.
    :param doc_obj: dict or list, the dictionary or list to traverse
    :param subdocument_class: the subdocument class to use
    :param list_class: the ResultList class to use
    :return: dict or list, the modified dictionary or list with subdocument and ResultList objects
    """
    if isinstance(doc_obj, dict):
        for key, value in doc_obj.items():
            if isinstance(value, dict):
                doc_obj[key] = subdocument_class(**value)
                create_subdocuments(doc_obj[key], subdocument_class, list_class)
            elif isinstance(value, list):
                doc_obj[key] = list_class([subdocument_class(**v) if isinstance(v, dict) else v for v in value])
                create_subdocuments(doc_obj[key], subdocument_class, list_class)
    elif isinstance(doc_obj, list):
        for i in range(len(doc_obj)):
            value = doc_obj[i]
            if isinstance(value, dict):
                doc_obj[i] = subdocument_class(**value)
                create_subdocuments(doc_obj[i], subdocument_class, list_class)
            elif isinstance(value, list):
                doc_obj[i] = list_class([subdocument_class(**v) if isinstance(v, dict) else v for v in value])
                create_subdocuments(doc_obj[i], subdocument_class, list_class)
    return doc_obj