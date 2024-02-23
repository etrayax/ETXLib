from .utils import DictType
from ETXLib import types
from typing import List

class Message(DictType):
    
    """
    
    This object represents a message.

    Parameters : 
        
        message_id (Integer) : Unique message identifier inside this chat
        
        message_thread_id (Integer) => Optional : Unique identifier of a message thread to which the message belongs; for supergroups only
        
        from ("types.User") => Optional :  Sender of the message; empty for messages sent to channels. For backward compatibility, the field contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat.
        
        sender_chat ("types.Chat") => Optional : Sender of the message, sent on behalf of a chat. For example, the channel itself for channel posts, the supergroup itself for messages from anonymous group administrators, the linked channel for messages automatically forwarded to the discussion group. For backward compatibility, the field from contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat.
        
        sender_boost_count (Integer) => Optional :  If the sender of the message boosted the chat, the number of boosts added by the user
        
        date (Integer) : Date the message was sent in Unix time. It is always a positive number, representing a valid date.
        
        chat ("types.Chat") : Chat the message belongs to
        
        forward_origin ("types.MessageOrigin") => Optional : Information about the original message for forwarded messages
        
        is_topic_message (True) => Optional : True, if the message is sent to a forum topic
        
        is_automatic_forward (True) => Optional : True, if the message is a channel post that was automatically forwarded to the connected discussion group
        
        reply_to_message ("types.Message") => Optional : For replies in the same chat and message thread, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
        
        external_reply ("types.ExternalReplyInfo") => Optional : Information about the message that is being replied to, which may come from another chat or forum topic

        quote ("types.TextQuote") => Optional : For replies that quote part of the original message, the quoted part of the message

        reply_to_story ("types.Story") => Optional : For replies to a story, the original story

        via_bot ("types.User") => Optional : Bot through which the message was sent

        edit_date (Integer) => Optional : Date the message was last edited in Unix time

        has_protected_content (True) => Optional : True, if the message can't be forwarded

        media_group_id (String) => Optional : The unique identifier of a media message group this message belongs to

        author_signature (String) => Optional : Signature of the post author for messages in channels, or the custom title of an anonymous group administrator

        text (String) => Optional : For text messages, the actual UTF-8 text of the message

        entities (List["types.MessageEntity"]) => Optional : For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text

        link_preview_options ("types.LinkPreviewOptions") => Optional : Options used for link preview generation for the message, if it is a text message and link preview options were changed

        animation ("types.Animation") => Optional : Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set

        audio ("types.Audio") => Optional : Message is an audio file, information about the file

        document ("types.Document") => Optional : Message is a general file, information about the file

        photo ("types.Array") => of PhotoSize	Optional : Message is a photo, available sizes of the photo

        sticker ("types.Sticker") => Optional : Message is a sticker, information about the sticker

        story ("types.Story") => Optional : Message is a forwarded story

        video ("types.Video") => Optional : Message is a video, information about the video

        video_note ("types.VideoNote") => Optional : Message is a video note, information about the video message

        voice ("types.Voice") => Optional : Message is a voice message, information about the file

        caption (String) => Optional : Caption for the animation, audio, document, photo, video or voice

        caption_entities (List["types.MessageEntity"]) =>	Optional : For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption

        has_media_spoiler (True) => Optional : True, if the message media is covered by a spoiler animation

        contact ("types.Contact") => Optional : Message is a shared contact, information about the contact

        dice ("types.Dice") => Optional : Message is a dice with random value

        game ("types.Game") => Optional : Message is a game, information about the game. More about games »

        poll ("types.Poll") => Optional : Message is a native poll, information about the poll

        venue ("types.Venue") => Optional : Message is a venue, information about the venue. For backward compatibility, when this field is set, the location field will also be set

        location ("types.Location") => Optional : Message is a shared location, information about the location

        new_chat_members (List["types.User"]) =>	Optional : New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)

        left_chat_member ("types.User") => Optional : A member was removed from the group, information about them (this member may be the bot itself)

        new_chat_title (str) => Optional : A chat title was changed to this value

        new_chat_photo (List["types.PhotoSize"]) => Optional : A chat photo was change to this value

        delete_chat_photo (True) => Optional : Service message: the chat photo was deleted

        group_chat_created (True) => Optional : Service message: the group has been created

        supergroup_chat_created (True) => Optional : Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.

        channel_chat_created (True) => Optional : Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel.

        message_auto_delete_timer_changed ("types.MessageAutoDeleteTimerChanged") => Optional : Service message: auto-delete timer settings changed in the chat

        migrate_to_chat_id (Integer) => Optional : The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.

        migrate_from_chat_id (Integer) => Optional : The supergroup has been migrated from a group with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.

        pinned_message ("types.MaybeInaccessibleMessage") => Optional : Specified message was pinned. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.

        invoice ("types.Invoice") => Optional : Message is an invoice for a payment, information about the invoice. More about payments »

        successful_payment ("types.SuccessfulPayment") => Optional : Message is a service message about a successful payment, information about the payment. More about payments »

        users_shared ("types.UsersShared") => Optional : Service message: users were shared with the bot

        chat_shared ("types.ChatShared") => Optional : Service message: a chat was shared with the bot

        connected_website ("types.String") => Optional : The domain name of the website on which the user has logged in. More about Telegram Login »

        write_access_allowed ("types.WriteAccessAllowed") => Optional : Service message: the user allowed the bot to write messages after adding it to the attachment or side menu, launching a Web App from a link, or accepting an explicit request from a Web App sent by the method requestWriteAccess

        passport_data ("types.PassportData") => Optional : Telegram Passport data

        proximity_alert_triggered ("types.ProximityAlertTriggered") => Optional : Service message. A user in the chat triggered another user's proximity alert while sharing Live Location.

        boost_added ("types.ChatBoostAdded") => Optional : Service message: user boosted the chat

        forum_topic_created ("types.ForumTopicCreated") => Optional : Service message: forum topic created

        forum_topic_edited ("types.ForumTopicEdited") => Optional : Service message: forum topic edited

        forum_topic_closed ("types.ForumTopicClosed") => Optional : Service message: forum topic closed

        forum_topic_reopened ("types.ForumTopicReopened") => Optional : Service message: forum topic reopened

        general_forum_topic_hidden ("types.GeneralForumTopicHidden") => Optional : Service message: the 'General' forum topic hidden

        general_forum_topic_unhidden ("types.GeneralForumTopicUnhidden") => Optional : Service message: the 'General' forum topic unhidden

        giveaway_created ("types.GiveawayCreated") => Optional : Service message: a scheduled giveaway was created

        giveaway ("types.Giveaway") => Optional : The message is a scheduled giveaway message

        giveaway_winners ("types.GiveawayWinners") => Optional : A giveaway with public winners was completed

        giveaway_completed ("types.GiveawayCompleted") => Optional : Service message: a giveaway without public winners was completed

        video_chat_scheduled ("types.VideoChatScheduled") => Optional : Service message: video chat scheduled

        video_chat_started ("types.VideoChatStarted") => Optional : Service message: video chat started

        video_chat_ended ("types.VideoChatEnded") => Optional : Service message: video chat ended

        video_chat_participants_invited ("types.VideoChatParticipantsInvited") => Optional : Service message: new participants invited to a video chat

        web_app_data ("types.WebAppData") => Optional : Service message: data sent by a Web App

        reply_markup ("types.InlineKeyboardMarkup") => Optional : Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons.


    """
    
    def __init__(self,
        message_id : int = None,
        message_thread_id : int = None,
        _from : "types.User" = None,
        sender_chat : "types.Chat" = None,
        sender_boost_count : int = None,
        date : int = None,
        chat : "types.Chat" = None,
        forward_origin : "types.MessageOrigin" = None,
        is_topic_message : bool = None,
        is_automatic_forward : bool = None,
        reply_to_message : "types.Message" = None,
        external_reply : "types.ExternalReplyInfo" = None,
        quote : "types.TextQuote" = None,
        reply_to_story : "types.Story" = None,
        via_bot : "types.User" = None,
        edit_date : int = None,
        has_protected_content : bool = None,
        media_group_id : str = None,
        author_signature : str = None,
        text : str = None,
        entities : List["types.MessageEntity"] = None,
        link_preview_options : "types.LinkPreviewOptions" = None,
        animation : "types.Animation" = None,
        audio : "types.Audio" = None,
        document : "types.Document" = None,
        photo : "types.Array" = None,
        sticker : "types.Sticker" = None,
        story : "types.Story" = None,
        video : "types.Video" = None,
        video_note : "types.VideoNote" = None,
        voice : "types.Voice" = None,
        caption : str = None,
        caption_entities : List["types.MessageEntity"] = None,
        has_media_spoiler : bool = None,
        contact : "types.Contact" = None,
        dice : "types.Dice" = None,
        game : "types.Game" = None,
        poll : "types.Poll" = None,
        venue : "types.Venue" = None,
        location : "types.Location" = None,
        new_chat_members : List["types.User"] = None,
        left_chat_member : "types.User" = None,
        new_chat_title : str = None,
        new_chat_photo : List["types.PhotoSize"] = None,
        delete_chat_photo : bool = None,
        group_chat_created : bool = None,
        supergroup_chat_created : bool = None,
        channel_chat_created : bool = None,
        message_auto_delete_timer_changed : "types.MessageAutoDeleteTimerChanged" = None,
        migrate_to_chat_id : int = None,
        migrate_from_chat_id : int = None,
        pinned_message : "types.MaybeInaccessibleMessage" = None,
        invoice : "types.Invoice" = None,
        successful_payment : "types.SuccessfulPayment" = None,
        users_shared : "types.UsersShared" = None,
        chat_shared : "types.ChatShared" = None,
        connected_website : "types.String" = None,
        write_access_allowed : "types.WriteAccessAllowed" = None,
        passport_data : "types.PassportData" = None,
        proximity_alert_triggered : "types.ProximityAlertTriggered" = None,
        boost_added : "types.ChatBoostAdded" = None,
        forum_topic_created : "types.ForumTopicCreated" = None,
        forum_topic_edited : "types.ForumTopicEdited" = None,
        forum_topic_closed : "types.ForumTopicClosed" = None,
        forum_topic_reopened : "types.ForumTopicReopened" = None,
        general_forum_topic_hidden : "types.GeneralForumTopicHidden" = None,
        general_forum_topic_unhidden : "types.GeneralForumTopicUnhidden" = None,
        giveaway_created : "types.GiveawayCreated" = None,
        giveaway : "types.Giveaway" = None,
        giveaway_winners : "types.GiveawayWinners" = None,
        giveaway_completed : "types.GiveawayCompleted" = None,
        video_chat_scheduled : "types.VideoChatScheduled" = None,
        video_chat_started : "types.VideoChatStarted" = None,
        video_chat_ended : "types.VideoChatEnded" = None,
        video_chat_participants_invited : "types.VideoChatParticipantsInvited" = None,
        web_app_data : "types.WebAppData" = None,
        reply_markup : "types.InlineKeyboardMarkup" = None,
    ):

        self.message_id = message_id
        self.message_thread_id = message_thread_id
        self.from_user = _from
        self.sender_chat = sender_chat
        self.sender_boost_count = sender_boost_count
        self.date = date
        self.chat = chat
        self.forward_origin = forward_origin
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.external_reply = external_reply
        self.quote = quote
        self.reply_to_story = reply_to_story
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.text = text
        self.entities = entities
        self.link_preview_options = link_preview_options
        self.animation = animation
        self.audio = audio
        self.document = document
        self.photo = photo
        self.sticker = sticker
        self.story = story
        self.video = video
        self.video_note = video_note
        self.voice = voice
        self.caption = caption
        self.caption_entities = caption_entities
        self.has_media_spoiler = has_media_spoiler
        self.contact = contact
        self.dice = dice
        self.game = game
        self.poll = poll
        self.venue = venue
        self.location = location
        self.new_chat_members = new_chat_members
        self.left_chat_member = left_chat_member
        self.new_chat_title = new_chat_title
        self.new_chat_photo = new_chat_photo
        self.delete_chat_photo = delete_chat_photo
        self.group_chat_created = group_chat_created
        self.supergroup_chat_created = supergroup_chat_created
        self.channel_chat_created = channel_chat_created
        self.message_auto_delete_timer_changed = message_auto_delete_timer_changed
        self.migrate_to_chat_id = migrate_to_chat_id
        self.migrate_from_chat_id = migrate_from_chat_id
        self.pinned_message = pinned_message
        self.invoice = invoice
        self.successful_payment = successful_payment
        self.users_shared = users_shared
        self.chat_shared = chat_shared
        self.connected_website = connected_website
        self.write_access_allowed = write_access_allowed
        self.passport_data = passport_data
        self.proximity_alert_triggered = proximity_alert_triggered
        self.boost_added = boost_added
        self.forum_topic_created = forum_topic_created
        self.forum_topic_edited = forum_topic_edited
        self.forum_topic_closed = forum_topic_closed
        self.forum_topic_reopened = forum_topic_reopened
        self.general_forum_topic_hidden = general_forum_topic_hidden
        self.general_forum_topic_unhidden = general_forum_topic_unhidden
        self.giveaway_created = giveaway_created
        self.giveaway = giveaway
        self.giveaway_winners = giveaway_winners
        self.giveaway_completed = giveaway_completed
        self.video_chat_scheduled = video_chat_scheduled
        self.video_chat_started = video_chat_started
        self.video_chat_ended = video_chat_ended
        self.video_chat_participants_invited = video_chat_participants_invited
        self.web_app_data = web_app_data
        self.reply_markup = reply_markup

        self.update(locals())
        
