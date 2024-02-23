from .utils import DictType, List, types

class InlineKeyboardMarkup(DictType):
    
    """
    
    This object represents an inline keyboard that appears right next to the message it belongs to.

    Parameters : 

        inline_keyboard (List[List["types.InlineKeyboardButton"]]) : Array of button rows, each represented by an Array of InlineKeyboardButton objects
    
    """
    
    def __init__(
        self,
        inline_keyboard : List[List["types.InlineKeyboardButton"]] = None
    ) -> dict:
        
        self.inline_keyboard : List[List["types.InlineKeyboardButton"]] = inline_keyboard
        
        self.update(locals())


