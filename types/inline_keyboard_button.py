from .utils import DictType, types

class InlineKeyboardButton(DictType):
    
    """
    This object represents one button of an inline keyboard. You must use exactly one of the optional fields.


    Parameters : 
        
        text (String) => Required : Label text on the button
            
        url (String) => Optional : HTTP or tg:// URL to be opened when the button is pressed. Links tg://user?id=<user_id> can be used to mention a user by their ID without using a username, if this is allowed by their privacy settings.
        
        callback_data (String) => Optional : Data to be sent in a callback query to the bot when button is pressed, 1-64 bytes
            
        web_app ("types.WebAppInfo") => Optional : Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery . Available only in private chats between a user and the bot.
        
        login_url ("types.LoginUrl") => Optional : An HTTPS URL used to automatically authorize the user. Can be used as a replacement for the Telegram Login Widget.
            
        switch_inline_query (String) => Optional : If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. May be empty, in which case just the bot's username will be inserted.
            
        switch_inline_query_current_chat (String) => Optional : If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. May be empty, in which case only the bot's username will be inserted. This offers a quick way for the user to open your bot in inline mode in the same chat - good for selecting something from multiple options.
        
        switch_inline_query_chosen_chat ("types.SwitchInlineQueryChosenChat") => Optional : If set, pressing the button will prompt the user to select one of their chats of the specified type, open that chat and insert the bot's username and the specified inline query in the input field
        
        callback_game ("types.CallbackGame") => Optional : Description of the game that will be launched when the user presses the button.
            NOTE: This type of button must always be the first button in the first row.
            
        pay (Boolean) => Optional :  Specify True, to send a Pay button.
            NOTE: This type of button must always be the first button in the first row and can only be used in invoice messages.
    
    """
    
    def __init__(
        self,
        text : str = None,
        url : str = None,
        callback_data : str = None,
        web_app : "types.WebAppInfo" = None,
        login_url : "types.LoginUrl" = None,
        switch_inline_query : str = None,
        switch_inline_query_current_chat : str = None,
        switch_inline_query_chosen_chat : "types.SwitchInlineQueryChosenChat" = None,
        callback_game : "types.CallbackGame" = None,
        pay : bool = None,
    ) -> dict:
        
        self.text : str = text
        self.url : str = url
        self.callback_data : str = callback_data
        self.web_app : "types.WebAppInfo" = web_app
        self.login_url : "types.LoginUrl" = login_url
        self.switch_inline_query : str = switch_inline_query
        self.switch_inline_query_current_chat : str = switch_inline_query_current_chat
        self.switch_inline_query_chosen_chat : "types.SwitchInlineQueryChosenChat" = switch_inline_query_chosen_chat
        self.callback_game : "types.CallbackGame" = callback_game
        self.pay : bool = pay
        
        self.update(locals())
