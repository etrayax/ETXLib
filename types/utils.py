from ETXLib import types
from typing import List, Union

class DictType(dict):
    def update(self, value):
        value.pop("self")
        super().update(value)
        