from ..utils import *

class setMessageReaction:
    
    """
    
    Use this method to change the chosen reactions on a message. Service messages can't be reacted to. Automatically forwarded messages from a channel to its discussion group have the same available reactions as messages in the channel. Returns True on success.
    
    Parameters:
    
        chat_id (Integer or String) => Yes : Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            
        message_id (Integer) => Yes : Identifier of the target message. If the message belongs to a media group, the reaction is set to the first non-deleted message in the group instead.

        reaction (Array of ReactionType) => Optional : New list of reaction types to set on the message. Currently, as non-premium users, bots can set up to one reaction per message. A custom emoji reaction can be used if it is either already present on the message or explicitly allowed by chat administrators.

        is_big (Boolean) => Optional : Pass True to set the reaction with a big animation
    
    """
    
    async def set_message_reaction(
        self,
        chat_id : Union[str, int],
        message_id : int,
        reaction = None,
        is_big : bool = None,
        *,
        api: str = None,
        result: bool = None
    ):
        return await Request(
            'post',
            url=(api or self.url) + "/setMessageReaction",
            json={
                "chat_id" : chat_id,
                "message_id" : message_id,
                "reaction" : reaction,
                "is_big" : is_big,
            },
            result=result if result is not None else self.result
        )