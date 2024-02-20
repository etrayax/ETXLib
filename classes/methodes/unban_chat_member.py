from ..utils import *

class unbanChatMember:
    
    """
        Use this method to unban a previously banned user in a supergroup or channel. The user will not return to the group or channel automatically, but will be able to join via link, etc. The bot must be an administrator for this to work. By default, this method guarantees that after the call the user is not a member of the chat, but will be able to join it. So if the user is a member of the chat they will also be removed from the chat. If you don't want this, use the parameter only_if_banned. Returns True on success.
        
        Parameters:
        
            chat_id (Integer or String) => Yes : Unique identifier for the target group or username of the target supergroup or channel (in the format @channelusername)
                
            user_id (Integer) => Yes : Unique identifier of the target user
            
            only_if_banned (Boolean) => Optional : Do nothing if the user is not banned
    """
    
    async def unban_chat_member(
        self,
        chat_id : Union[str, int],
        user_id : int,
        only_if_banned : bool = True,
        *,
        api: str = None,
        result: bool = None
    ):
        return await Request(
            'post',
            url=(api or self.url) + "/unbanChatMember",
            json={
                "chat_id" : chat_id,
                "user_id" : user_id,
                "only_if_banned" : only_if_banned,
            },
            result=result if result is not None else self.result
        )