from ..utils import *

class promoteChatMember:
    
    """
    
    Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Pass False for all boolean parameters to demote a user. Returns True on success.

    Parameters :

        chat_id	(Integer or String) => Yes: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            
        user_id (Integer) => Yes: Unique identifier of the target user
            
        is_anonymous (Boolean) => Optional: Pass True if the administrator's presence in the chat is hidden

        can_manage_chat (Boolean) => Optional: Pass True if the administrator can access the chat event log, boost list in channels, see channel members, report spam messages, see anonymous administrators : in supergroups and ignore slow mode. Implied by any other administrator privilege
            
        can_delete_messages (Boolean) => Optional: Pass True if the administrator can delete messages of other users
            
        can_manage_video_chats (Boolean) => Optional: Pass True if the administrator can manage video chats
            
        can_restrict_members (Boolean) => Optional: Pass True if the administrator can restrict, ban or unban chat members, or access supergroup statistics
            
        can_promote_members (Boolean) => Optional: Pass True if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted : , directly or indirectly (promoted by administrators that were appointed by him)
        
        can_change_info (Boolean) => Optional: Pass True if the administrator can change chat title, photo and other settings
            
        can_invite_users (Boolean) => Optional: Pass True if the administrator can invite new users to the chat
            
        can_post_messages (Boolean) => Optional: Pass True if the administrator can post messages in the channel, or access channel statistics; channels only
            
        can_edit_messages (Boolean) => Optional: Pass True if the administrator can edit messages of other users and can pin messages; channels only
            
        can_pin_messages (Boolean) => Optional: Pass True if the administrator can pin messages, supergroups only
            
        can_post_stories (Boolean) => Optional: Pass True if the administrator can post stories in the channel; channels only
            
        can_edit_stories (Boolean) => Optional: Pass True if the administrator can edit stories posted by other users; channels only
            
        can_delete_stories (Boolean) => Optional: Pass True if the administrator can delete stories posted by other users; channels only
            
        can_manage_topics (Boolean) => Optional: Pass True if the user is allowed to create, rename, close, and reopen forum topics, supergroups only
    """
    
    async def promote_chat_member(
        self,
        chat_id : Union[str, int],
        user_id : int,
        is_anonymous : bool = None,
        can_manage_chat : bool = None,
        can_delete_messages : bool = None,
        can_manage_video_chats : bool = None,
        can_restrict_members : bool = None,
        can_promote_members : bool = None,
        can_change_info : bool = None,
        can_invite_users : bool = None,
        can_post_messages : bool = None,
        can_edit_messages : bool = None,
        can_pin_messages : bool = None,
        can_post_stories : bool = None,
        can_edit_stories : bool = None,
        can_delete_stories : bool = None,
        can_manage_topics : bool = None,
        *,
        api: str = None,
        result: bool = None
    ):
        await Request(
            'post',
            url=(api or self.url) + "/promoteChatMember",
            json={
                "chat_id" : chat_id,
                "user_id" : user_id,
                "is_anonymous" : is_anonymous,
                "can_manage_chat" : can_manage_chat,
                "can_delete_messages" : can_delete_messages,
                "can_manage_video_chats" : can_manage_video_chats,
                "can_restrict_members" : can_restrict_members,
                "can_promote_members" : can_promote_members,
                "can_change_info" : can_change_info,
                "can_invite_users" : can_invite_users,
                "can_post_messages" : can_post_messages,
                "can_edit_messages" : can_edit_messages,
                "can_pin_messages" : can_pin_messages,
                "can_post_stories" : can_post_stories,
                "can_edit_stories" : can_edit_stories,
                "can_delete_stories" : can_delete_stories,
                "can_manage_topics" : can_manage_topics,
            },
            result=result if result is not None else self.result
        )