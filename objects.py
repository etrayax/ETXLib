from typing import Any

class ETXDict:
    
    def __init__(self, object: dict) -> None:
        self.__data = object
        self._exclude = {
            "from_user" : "from"
        }
        
    def __getattribute__(self, name: str) -> "ETXDict":
        obj = object.__data.get(self._exclude(name) or name)
            
        if isinstance(obj, dict):
            return ETXDict(obj)

        else:
            return obj
        
    def __getitem__(self, name: str) -> "ETXDict":
        
        obj = object.__data.get(self._exclude(name) or name)
            
        if isinstance(obj, dict):
            return ETXDict(obj)

        else:
            return obj
        
    def __str__(self) -> str:
        return f"{object.__data}"

