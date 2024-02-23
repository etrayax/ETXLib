from .utils import DictType
from ETXLib import types
from typing import List

class Chat(DictType):
    
    """
    
    This object represents a chat.

    Parameters : 

        id (Integer) : Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.

        type (String) : Type of chat, can be either “private”, “group”, “supergroup” or “channel”

        title (String) => Optional : Title, for supergroups, channels and group chats

        username (String) => Optional : Username, for private chats, supergroups and channels if available

        first_name (String) => Optional : First name of the other party in a private chat

        last_name (String) => Optional : Last name of the other party in a private chat

        is_forum (True) => Optional : True, if the supergroup chat is a forum (has topics enabled)

        photo ("types.ChatPhoto") => Optional : Chat photo. Returned only in getChat.

        active_usernames (List[str]) => Optional : If non-empty, the list of all active chat usernames; for private chats, supergroups and channels. Returned only in getChat.

        available_reactions (List["types.ReactionType"]) => Optional : List of available reactions allowed in the chat. If omitted, then all emoji reactions are allowed. Returned only in getChat.

        accent_color_id (Integer) => Optional : Identifier of the accent color for the chat name and backgrounds of the chat photo, reply header, and link preview. See accent colors for more details. Returned only in getChat. Always returned in getChat.

        background_custom_emoji_id (String) => Optional : Custom emoji identifier of emoji chosen by the chat for the reply header and link preview background. Returned only in getChat.

        profile_accent_color_id (Integer) => Optional : Identifier of the accent color for the chat's profile background. See profile accent colors for more details. Returned only in getChat.

        profile_background_custom_emoji_id (String) => Optional : Custom emoji identifier of the emoji chosen by the chat for its profile background. Returned only in getChat.

        emoji_status_custom_emoji_id (String) => Optional : Custom emoji identifier of the emoji status of the chat or the other party in a private chat. Returned only in getChat.

        emoji_status_expiration_date (Integer) => Optional : Expiration date of the emoji status of the chat or the other party in a private chat, in Unix time, if any. Returned only in getChat.

        bio (String) => Optional : Bio of the other party in a private chat. Returned only in getChat.

        has_private_forwards (True) => Optional : True, if privacy settings of the other party in the private chat allows to use tg://user?id=<user_id> links only in chats with the user. Returned only in getChat.

        has_restricted_voice_and_video_messages (True) => Optional : True, if the privacy settings of the other party restrict sending voice and video note messages in the private chat. Returned only in getChat.

        join_to_send_messages (True) => Optional : True, if users need to join the supergroup before they can send messages. Returned only in getChat.

        join_by_request (True) => Optional : True, if all users directly joining the supergroup need to be approved by supergroup administrators. Returned only in getChat.

        description (String) => Optional : Description, for groups, supergroups and channel chats. Returned only in getChat.

        invite_link (String) => Optional : Primary invite link, for groups, supergroups and channel chats. Returned only in getChat.

        pinned_message ("types.Message") => Optional : The most recent pinned message (by sending date). Returned only in getChat.

        permissions ("types.ChatPermissions") => Optional : Default chat member permissions, for groups and supergroups. Returned only in getChat.

        slow_mode_delay (Integer) => Optional : For supergroups, the minimum allowed delay between consecutive messages sent by each unprivileged user; in seconds. Returned only in getChat.

        unrestrict_boost_count (Integer) => Optional : For supergroups, the minimum number of boosts that a non-administrator user needs to add in order to ignore slow mode and chat permissions. Returned only in getChat.

        message_auto_delete_time (Integer) => Optional : The time after which all messages sent to the chat will be automatically deleted; in seconds. Returned only in getChat.

        has_aggressive_anti_spam_enabled (True) => Optional : True, if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators. Returned only in getChat.

        has_hidden_members (True) => Optional : True, if non-administrators can only get the list of bots and administrators in the chat. Returned only in getChat.

        has_protected_content (True) => Optional : True, if messages from the chat can't be forwarded to other chats. Returned only in getChat.

        has_visible_history (True) => Optional : True, if new chat members will have access to old messages; available only to chat administrators. Returned only in getChat.

        sticker_set_name (str) => Optional : For supergroups, name of group sticker set. Returned only in getChat.

        can_set_sticker_set (True) => Optional : True, if the bot can change the group sticker set. Returned only in getChat.

        custom_emoji_sticker_set_name (List[str]) => Optional : For supergroups, the name of the group's custom emoji sticker set. Custom emoji from this set can be used by all users and bots in the group. Returned only in getChat.

        linked_chat_id (Integer) => Optional : Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier. Returned only in getChat.

        location ("types.ChatLocation") => Optional : For supergroups, the location to which the supergroup is connected. Returned only in getChat.



    """
    
    def __init__(self,
        id : int = None,
        type : str = None,
        title : str = None,
        username : str = None,
        first_name : str = None,
        last_name : str = None,
        is_forum : bool = None,
        photo : "types.ChatPhoto" = None,
        active_usernames : List[str] = None,
        available_reactions : List["types.ReactionType"] = None,
        accent_color_id : int = None,
        background_custom_emoji_id : str = None,
        profile_accent_color_id : int = None,
        profile_background_custom_emoji_id : str = None,
        emoji_status_custom_emoji_id : int = None,
        emoji_status_expiration_date : str = None,
        bio : str = None,
        has_private_forwards : bool = None,
        has_restricted_voice_and_video_messages : bool = None,
        join_to_send_messages : bool = None,
        join_by_request : bool = None,
        description : str = None,
        invite_link : str = None,
        pinned_message : "types.Message" = None,
        permissions : "types.ChatPermissions" = None,
        slow_mode_delay : int = None,
        unrestrict_boost_count : int = None,
        message_auto_delete_time : int = None,
        has_aggressive_anti_spam_enabled : bool = None,
        has_hidden_members : bool = None,
        has_protected_content : bool = None,
        has_visible_history : bool = None,
        sticker_set_name : str = None,
        can_set_sticker_set : bool = None,
        custom_emoji_sticker_set_name : List[str] = None,
        linked_chat_id : int = None,
        location : "types.ChatLocation" = None,
    ):
        
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_forum = is_forum
        self.photo = photo
        self.active_usernames = active_usernames
        self.available_reactions = available_reactions
        self.accent_color_id = accent_color_id
        self.background_custom_emoji_id = background_custom_emoji_id
        self.profile_accent_color_id = profile_accent_color_id
        self.profile_background_custom_emoji_id = profile_background_custom_emoji_id
        self.emoji_status_custom_emoji_id = emoji_status_custom_emoji_id
        self.emoji_status_expiration_date = emoji_status_expiration_date
        self.bio = bio
        self.has_private_forwards = has_private_forwards
        self.has_restricted_voice_and_video_messages = has_restricted_voice_and_video_messages
        self.join_to_send_messages = join_to_send_messages
        self.join_by_request = join_by_request
        self.description = description
        self.invite_link = invite_link
        self.pinned_message = pinned_message
        self.permissions = permissions
        self.slow_mode_delay = slow_mode_delay
        self.unrestrict_boost_count = unrestrict_boost_count
        self.message_auto_delete_time = message_auto_delete_time
        self.has_aggressive_anti_spam_enabled = has_aggressive_anti_spam_enabled
        self.has_hidden_members = has_hidden_members
        self.has_protected_content = has_protected_content
        self.has_visible_history = has_visible_history
        self.sticker_set_name = sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set
        self.custom_emoji_sticker_set_name = custom_emoji_sticker_set_name
        self.linked_chat_id = linked_chat_id
        self.location = location
        
        self.update(locals())