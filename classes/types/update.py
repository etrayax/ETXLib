from .utils import TeleObj

class Update(TeleObj):
    
    
    """
    
    This object represents an incoming update.
    At most one of the optional parameters can be present in any given update.
    
    
    
    update_id :
    
        - Integer	
        - The update's unique identifier. Update identifiers start from a certain positive number and increase sequentially. This ID becomes especially handy if you're using webhooks, since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially.
    
    message	:
    
        - Message	
        - Optional. New incoming message of any kind - text, photo, sticker, etc.
    
    edited_message :
    
        - Message	
        - Optional. New version of a message that is known to the bot and was edited
        
    channel_post :
    
        - Message
        - Optional. New incoming channel post of any kind - text, photo, sticker, etc.
        
    edited_channel_post :
    
        - Message
        - Optional. New version of a channel post that is known to the bot and was edited
        
    inline_query :
    
        - InlineQuery
        - Optional. New incoming inline query
    
    chosen_inline_result :
    
        - ChosenInlineResult
        - Optional. The result of an inline query that was chosen by a user and sent to their chat partner. Please see our documentation on the feedback collecting for details on how to enable these updates for your bot.
        
    callback_query :
    
        - CallbackQuery	
        - Optional. New incoming callback query
        
    shipping_query :
    
        - ShippingQuery	
        - Optional. New incoming shipping query. Only for invoices with flexible price
        
    pre_checkout_query :
    
        - PreCheckoutQuery	
        - Optional. New incoming pre-checkout query. Contains full information about checkout
        
    poll :
    
        - Poll	
        - Optional. New poll state. Bots receive only updates about stopped polls and polls, which are sent by the bot
        
    poll_answer :
    
        - PollAnswer
        - Optional. A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself.
        
    my_chat_member :
    
        - ChatMemberUpdated	
        - Optional. The bot's chat member status was updated in a chat. For private chats, this update is received only when the bot is blocked or unblocked by the user.
        
    chat_member	ChatMemberUpdated : 
    
        - Optional. 
        - A chat member's status was updated in a chat. The bot must be an administrator in the chat and must explicitly specify "chat_member" in the list of allowed_updates to receive these updates.
        
    chat_join_request :
    
        - ChatJoinRequest
        - Optional. A request to join the chat has been sent. The bot must have the can_invite_users administrator right in the chat to receive these updates.
    
    """
    
    def __init__(
        self,
        update_id = None,
        message = None,
        edited_message = None,
        channel_post = None,
        edited_channel_post = None,
        inline_query = None,
        chosen_inline_result = None,
        callback_query = None,
        shipping_query = None,
        pre_checkout_query = None,
        poll = None,
        poll_answer = None,
        my_chat_member = None,
        chat_member = None,
        chat_join_request = None,
    ) -> dict:
        self.update(locals())
    
    

    
    