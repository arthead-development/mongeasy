from mongeasy.base_dict import BaseDict
from copy import copy


class SubDocument(dict):
    def __init__(self, *args, **kwargs):
        super().__init__()
        # Handle positional arguments
        if len(args) == 1 and isinstance(args[0], dict):
            as_dict = copy(args[0])
        elif len(args) == 0:
            as_dict = copy(kwargs)
        else:
            raise TypeError(f'Document() takes 1 positional argument or keyword arguments but {len(args) + len(kwargs)} were given')

        self.__dict__.update(as_dict)