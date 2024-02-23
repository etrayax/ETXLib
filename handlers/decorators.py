from typing import Callable
from .handlers import *

class OnMessage:
    def on_message(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self.add_handler(MessageHandler(func))
            return func
        return decorator

class OnEditedMessage:
    def on_edited_message(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self.add_handler(EditedMessageHandler(func))
            return func
        return decorator

class OnChannelPost:
    def on_channel_post(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self.add_handler(ChannelPostHandler(func))
            return func
        return decorator

class OnEditedChannelPost:
    def on_edited_channel_post(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self.add_handler(EditedChannelPostHandler(func))
            return func
        return decorator

class OnInlineQuery:
    def on_inline_query(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self.add_handler(InlineQueryHandler(func))
            return func
        return decorator

class OnChosenInlineResult:
    def on_chosen_inline_result(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self.add_handler(ChosenInlineResultHandler(func))
            return func
        return decorator

class OnCallbackQuery:
    def on_callback_query(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self.add_handler(CallbackQueryHandler(func))
            return func
        return decorator

class OnShippingQuery:
    def on_shipping_query(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self.add_handler(ShippingQueryHandler(func))
            return func
        return decorator

class OnPreCheckoutQuery:
    def on_pre_checkout_query(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self.add_handler(PreCheckoutQueryHandler(func))
            return func
        return decorator

class OnPoll:
    def on_poll(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self.add_handler(PollHandler(func))
            return func
        return decorator

class OnPollAnswer:
    def on_message(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self.add_handler(PollAnswerHandler(func))
            return func
        return decorator

class OnMyChatMember:
    def on_my_chat_member(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self.add_handler(MyChatMemberHandler(func))
            return func
        return decorator

class OnChatMember:
    def on_chat_member(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self.add_handler(ChatMemberHandler(func))
            return func
        return decorator

class OnChatJoinRequest:
    def on_chat_join_request(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self.add_handler(ChatJoinRequestHandler(func))
            return func
        return decorator