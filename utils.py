from typing import Any

class ObjType:
    
    def __init__(self, obj: dict) -> None:
        self.__data = obj
        
    def __getattribute__(self, __name: str) -> Any:
        
        obj = object.__getattribute__(self, '_ObjType__data').get(__name)
            
        if isinstance(obj, dict):
            return ObjType(obj)

        else:
            return obj
        
    def __getitem__(self, __name: str):
        
        obj = object.__getattribute__(self, '_ObjType__data').get(__name)
            
        if isinstance(obj, dict):
            return ObjType(obj)

        else:
            return obj
        
    def __str__(self) -> str:
        return f"{object.__getattribute__(self, '_ObjType__data')}"

