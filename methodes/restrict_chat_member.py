from ..utils import *

class restrictChatMember:
    
    """
    
    Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate administrator rights. Pass True for all permissions to lift restrictions from a user. Returns True on success.
    
    Parameters:
    
        chat_id (Integer or String) => Yes : Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        
        user_id	(Integer) => Yes : Unique identifier of the target user
            
        permissions (ChatPermissions) => Yes : A JSON-serialized object for new user permissions
            
        use_independ(Boolean) ent_chat_permissions => Optional : Pass True if chat permissions are set independently. Otherwise, the can_send_other_messages and can_add_web_page_previews permissions will imply the can_send_messages, can_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, and can_send_voice_notes permissions; the can_send_polls permission will imply the can_send_messages permission.
            
        until_date (Integer) => Optional : Date when restrictions will be lifted for the user; Unix time. If user is restricted for more than 366 days or less than 30 seconds from the current time, they are considered to be restricted forever
    
    """
    
    async def restrict_chat_member(
        self,
        chat_id : Union[str,int],
        user_id : int,
        permissions = None,
        use_independent_chat_permissions : bool = None,
        until_date : int = None,
        *,
        api: str = None,
        result: bool = None
    ):
        return await Request(
            'post',
            url=(api or self.url) + "/restrictChatMember",
            json={
                "chat_id" : chat_id,
                "user_id" : user_id,
                "permissions" : permissions,
                "use_independent_chat_permissions" : use_independent_chat_permissions,
                "until_date" : until_date,
            },
            result=result if result is not None else self.result
        )