

class TeleObj(dict):
    
    def update(self, value):
        value.pop("self")
        super().update(value)