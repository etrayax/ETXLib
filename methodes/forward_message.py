from ETXLib.Request import Request
from typing import Union

class forwardMessage:
    
    """
    
    Use this method to copy messages of any kind. Service messages, giveaway messages, giveaway winners messages, and invoice messages can't be copied. A quiz poll can be copied only if the value of the field correct_option_id is known to the bot. The method is analogous to the method forwardMessage, but the copied message doesn't have a link to the original message. Returns the MessageId of the sent message on success.
    
        
    Parameters :
    
        chat_id (Integer or String) => Required : Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            
        message_thread_id (Integer) => Optional : Unique identifier for the target message thread (topic) of the forum; for forum :supergroups only
            
        from_chat_id (Integer or String) => Optional : Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)
            
        disable_notification (Boolean) => Optional : Sends the message silently. Users will receive a notification with no sound.
            
        protect_content (Boolean) => Optional : Protects the contents of the forwarded message from forwarding and saving
            
        message_id (Integer) => Optional : Message identifier in the chat specified in from_chat_id
    """
    
    
    async def forward_message(
        self,
        chat_id : Union[str, int],
        message_thread_id : int = None,
        from_chat_id : Union[str, int] = None,
        disable_notification : bool = None,
        protect_content : bool = None,
        message_id : int = None,
        *,
        api: str = None,
        result: bool = None
    ):
        await Request(
            'post',
            url=(api or self.url) + "/forwardMessage",
            json={
                "chat_id" : chat_id,
                "message_thread_id" : message_thread_id,
                "from_chat_id" : from_chat_id,
                "message_id" : message_id,
                "disable_notification" : disable_notification,
                "protect_content" : protect_content,
            },
            result=result if result is not None else self.result
        )