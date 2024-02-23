from .utils import DictType, types

class Update(DictType):
    
    
    """
    
    This object represents an incoming update.
    At most one of the optional parameters can be present in any given update.
    
    
    Parameters :
    
        update_id (Integer) => Required : The update's unique identifier. Update identifiers start from a certain positive number and increase sequentially. This ID becomes especially handy if you're using webhooks, since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially.
        
        message	(Message) => Optional : New incoming message of any kind - text, photo, sticker, etc.
        
        edited_message ("types.Message") => Optional : New version of a message that is known to the bot and was edited
            
        channel_post ("types.Message") => Optional : New incoming channel post of any kind - text, photo, sticker, etc.
            
        edited_channel_post ("types.Message") => Optional : New version of a channel post that is known to the bot and was edited
            
        inline_query ("types.InlineQuery") => Optional : New incoming inline query
        
        chosen_inline_result ("types.ChosenInlineResult") => Optional : The result of an inline query that was chosen by a user and sent to their chat partner. Please see our documentation on the feedback collecting for details on how to enable these updates for your bot.
            
        callback_query ("types.CallbackQuery") => Optional : New incoming callback query
            
        shipping_query ("types.ShippingQuery") => Optional : New incoming shipping query. Only for invoices with flexible price
            
        pre_checkout_query ("types.PreCheckoutQuery") => Optional : New incoming pre-checkout query. Contains full information about checkout
            
        poll ("types.Poll") => Optional : New poll state. Bots receive only updates about stopped polls and polls, which are sent by the bot
            
        poll_answer ("types.PollAnswer") => Optional : A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself.
            
        my_chat_member ("types.ChatMemberUpdated") => Optional : The bot's chat member status was updated in a chat. For private chats, this update is received only when the bot is blocked or unblocked by the user.
            
        chat_member	("types.ChatMemberUpdated") => Optional : A chat member's status was updated in a chat. The bot must be an administrator in the chat and must explicitly specify "chat_member" in the list of allowed_updates to receive these updates.
            
        chat_join_request ("types.ChatJoinRequest") => Optional : A request to join the chat has been sent. The bot must have the can_invite_users administrator right in the chat to receive these updates.
    
    """
    
    def __init__(
        self,
        update_id : int = None,
        message : "types.Message" = None,
        edited_message : "types.Message" = None,
        channel_post : "types.Message" = None,
        edited_channel_post : "types.Message" = None,
        inline_query : "types.InlineQuery" = None,
        chosen_inline_result : "types.ChosenInlineResult" = None,
        callback_query : "types.CallbackQuery" = None,
        shipping_query : "types.ShippingQuery" = None,
        pre_checkout_query : "types.PreCheckoutQuery" = None,
        poll : "types.Poll" = None,
        poll_answer : "types.PollAnswer" = None,
        my_chat_member : "types.ChatMemberUpdated" = None,
        chat_member : "types.ChatMemberUpdated" = None,
        chat_join_request : "types.ChatJoinRequest" = None,
    ) -> dict:
        
        self.update_id : int = update_id
        self.message : "types.Message" = message
        self.edited_message : "types.Message" = edited_message
        self.channel_post : "types.Message" = channel_post
        self.edited_channel_post : "types.Message" = edited_channel_post
        self.inline_query : "types.InlineQuery" = inline_query
        self.chosen_inline_result : "types.ChosenInlineResult" = chosen_inline_result
        self.callback_query : "types.CallbackQuery" = callback_query
        self.shipping_query : "types.ShippingQuery" = shipping_query
        self.pre_checkout_query : "types.PreCheckoutQuery" = pre_checkout_query
        self.poll : "types.Poll" = poll
        self.poll_answer : "types.PollAnswer" = poll_answer
        self.my_chat_member : "types.ChatMemberUpdated" = my_chat_member
        self.chat_member : "types.ChatMemberUpdated" = chat_member
        self.chat_join_request : "types.ChatJoinRequest" = chat_join_request
        
        self.update(locals())