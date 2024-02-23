
class CustomObject:
    
    def __init__(self, obj: dict) -> None:
        self.__data = obj
        
    def __getattr__(self, name: str):
        obj = self.__data.get(name)
        
        if isinstance(obj, dict):
            return CustomObject(obj)
        else:
            return obj
        
    def __getitem__(self, name: str):
        obj = self.__data.get(name)
        
        if isinstance(obj, dict):
            return CustomObject(obj)
        else:
            return obj
        
    def __str__(self) -> str:
        return f"{self.__data}"

