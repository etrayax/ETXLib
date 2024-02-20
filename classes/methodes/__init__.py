from .set_webhook import setWebhook
from .send_message import sendMessage
from .delete_message import deleteMessage
from .set_message_reaction import setMessageReaction
from .restrict_chat_member import restrictChatMember
from .unban_chat_member import unbanChatMember
from .promote_chat_member import promoteChatMember
from .ban_chat_member import banChatMember
from .copy_message    import copyMessage
from .forward_message import forwardMessage
from .delete_webhook import deleteWebhook

class Methodes(
    setWebhook,
    sendMessage,
    deleteMessage,
    setMessageReaction,
    restrictChatMember,
    unbanChatMember,
    promoteChatMember,
    banChatMember,
    copyMessage,
    forwardMessage,
    deleteWebhook
):
    pass