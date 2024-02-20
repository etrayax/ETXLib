from ..utils import *

class sendMessage:
    
    
    """
    
    Use this method to send text messages. On success, the sent Message is returned.


    Parameters:
    
        chat_id (Integer) => Yes : Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        
        message_thread_id (Integer) => Optional : Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
        
        text (String) => Yes : ext of the message to be sent, 1-4096 characters after entities parsing
        
        parse_mode (String) => Optional : Mode for parsing entities in the message text. See formatting options for more details.
        
        entities (Array of MessageEntity) => Optional : A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode
        
           
        disable_web_page_preview (Boolean) => Optional : Disables link previews for links in this message
           
        disable_notification (Boolean) => Optional : Sends the message silently. Users will receive a notification with no sound.
        
        protect_content (Boolean) => Optional : Protects the contents of the sent message from forwarding and saving
        
        reply_to_message_id (Integer) => Optional : If the message is a reply, ID of the original message
            
        allow_sending_without_reply (Boolean) => Optional : Pass True if the message should be sent even if the specified replied-to message is not found  
           
        reply_markup (Optional) => InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply : Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.        
           
    """
    
    async def send_message(
        self,
        chat_id : Union[str, int],
        text,
        message_thread_id : int = None,
        parse_mode : str = "html",
        entities = None,
        disable_web_page_preview : bool = None,
        disable_notification : bool = None,
        protect_content : bool = None,
        reply_to_message_id = None,
        allow_sending_without_reply : bool = None,
        reply_markup : List[Type["InlineKeyboardMarkup"]] = None,
        *,
        api: str = None,
        result: bool = None
    ):
        return await Request(
            'post',
            url=(api or self.url) + "/sendMessage",
            json={
                "chat_id" : chat_id,
                "message_thread_id" : message_thread_id,
                "text" : text,
                "parse_mode" : parse_mode,
                "entities" : entities,
                "disable_web_page_preview" : disable_web_page_preview,
                "disable_notification" : disable_notification,
                "protect_content" : protect_content,
                "reply_to_message_id" : reply_to_message_id,
                "allow_sending_without_reply" : allow_sending_without_reply,
                "reply_markup" : reply_markup,
            },
            result=result if result is not None else self.result
        )