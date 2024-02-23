from ..utils import *


class deleteMessage:
    
    
    """
    Use this method to delete multiple messages simultaneously. If some of the specified messages can't be found, they are skipped. Returns True on success.
    
    
    Parameters :
    
        chat_id (Integer or String) => Yes : Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        
        message_ids (Array of Integer) => Yes : Identifiers of 1-100 messages to delete. See deleteMessage for limitations on which messages can be deleted
    
    """
    
    async def delete_message(
        self,
        chat_id : Union[str,int],
        message_ids : int,
        *,
        api: str = None,
        result: bool = None
    ):
        await Request(
            'post',
            url=(api or self.url) + "/deleteMessage",
            json={
                "chat_id" : chat_id,
                "message_id" : message_ids,
            },
            result=result if result is not None else self.result
        )