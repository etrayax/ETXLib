from .utils import TeleObj


class InlineKeyboardMarkup(TeleObj):
    
    """
    
    This object represents an inline keyboard that appears right next to the message it belongs to.

    inline_keyboard :
    
        - Array of Array of InlineKeyboardButton
        - Array of button rows, each represented by an Array of InlineKeyboardButton objects
    
    """
    
    def __init__(
        self,
        inline_keyboard = None
    ) -> dict:
        self.update(locals())


