from types  import FunctionType, MethodType
from typing import Union

def get_handler_name(input_string: str):
    def normalizer():
        return "".join(l if l.islower() else "_" + l.lower() for l in input_string)
        
    return normalizer().removesuffix("handler").strip("_")

class BaseHandler:
    def __init__(self, func: Union[FunctionType, MethodType]) -> None:
        self.name = get_handler_name(self.__class__.__name__)
        self.func = func