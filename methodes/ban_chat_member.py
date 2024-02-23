from ETXLib.Request import Request
from typing import Union

class banChatMember:
    
    """

    Use this method to ban a user in a group, a supergroup or a channel. In the case of supergroups and channels, the user will not be able to return to the chat on their own using invite links, etc., unless unbanned first. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.
    
    Parameters :
    
        chat_id (Integer or String) => Required : Unique identifier for the target group or username of the target supergroup or channel (in the format @channelusername)
            
        user_id (Integer) => Required : Unique identifier of the target user
            
        until_date (Integer) => Optional : Date when the user will be unbanned; Unix time. If user is banned for more than 366 days or less than 30 seconds from the current time they are considered to be banned forever. Applied for supergroups and channels only.
        
        revoke_messa(Boolean) ges => Optional : Pass True to delete all messages from the chat for the user that is being removed. If False, the user will be able to see messages in the group that were sent before the user was removed. Always True for supergroups and channels.
        
    """
    
    async def ban_chat_member(
        self,
        chat_id : Union[str, int],
        user_id : int,
        until_date : int = None,
        revoke_messages : bool = None,
        *,
        api: str = None,
        result: bool = None
    ):
        await Request(
            'post',
            url=(api or self.url) + "/banChatMember",
            json={
                "chat_id" : chat_id,
                "user_id" : user_id,
                "until_date" : until_date,
                "revoke_messages" : revoke_messages,
            },
            result=result if result is not None else self.result
        )