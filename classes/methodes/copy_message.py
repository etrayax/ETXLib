from ..utils import *


class copyMessage:
    
    """
    
    Use this method to copy messages of any kind. Service messages, giveaway messages, giveaway winners messages, and invoice messages can't be copied. A quiz poll can be copied only if the value of the field correct_option_id is known to the bot. The method is analogous to the method forwardMessage, but the copied message doesn't have a link to the original message. Returns the MessageId of the sent message on success.
    
        
    Parameters :
    
        chat_id (Integer or String) => Yes : Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            
        message_thread_id (Integer) => Optional : Unique identifier for the target message thread (topic) of the forum; for forum supergroups :
         only
        
        from_chat_id (Integer or String) => Yes : Unique identifier for the chat where the original message was sent (or channel username :
         in the format @channelusername)
        
        message_id (Integer) => Yes : Message identifier in the chat specified in from_chat_id
        
        caption (String) => Optional : New caption for media, 0-1024 characters after entities parsing. If not specified, the original :
         caption is kept

        parse_mode (String) => Optional : Mode for parsing entities in the new caption. See formatting options for more details.

        caption_entities (Array of MessageEntity) => Optional : A JSON-serialized list of special entities that appear in the new caption :, which can be specified instead of parse_mode
        
        disable_notification (Boolean) => Optional : Sends the message silently. Users will receive a notification with no sound.
        
        protect_content (Boolean) => Optional : Protects the contents of the sent message from forwarding and saving
        
        reply_parameters (ReplyParameters) => Optional : Description of the message to reply to
        
        reply_markup (InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply) => Optional : Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    """
    
    
    async def copy_message(
        self,
        chat_id : Union[str, int],
        message_thread_id : int = None,
        from_chat_id : Union[str, int] = None,
        message_id : int = None,
        caption : str = None,
        parse_mode : str = None,
        caption_entities = None,
        disable_notification : bool = None,
        protect_content : bool = None,
        reply_parameters = None,
        reply_markup = None,
        *,
        api: str = None,
        result: bool = None
    ):
        await Request(
            'post',
            url=(api or self.url) + "/copyMessage",
            json={
                "chat_id" : chat_id,
                "message_thread_id" : message_thread_id,
                "from_chat_id" : from_chat_id,
                "message_id" : message_id,
                "caption" : caption,
                "parse_mode" : parse_mode,
                "caption_entities" : caption_entities,
                "disable_notification" : disable_notification,
                "protect_content" : protect_content,
                "reply_parameters" : reply_parameters,
                "reply_markup" : reply_markup,
            },
            result=result if result is not None else self.result
        )