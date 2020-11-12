from django.core.validators import RegexValidator
from jinja2 import Template

from cartloop.models import Chat, Conversation


class ChatController:
    payload_validator = RegexValidator(r'^[0-9a-zA-Z:{}$%_\-\/~@#^&*()!?. ]*$',
                                       'Invalid Payload')

    @staticmethod
    def render_all(conversation: Conversation):
        return [ChatController.render_chat(chat, conversation) for chat in conversation.chat_set.all()]

    @staticmethod
    def render_chat(chat: Chat, conversation: Conversation):
        template = Template(chat.payload)
        chat.payload = template.render(operator=conversation.operator, store=conversation.store,
                                       client=conversation.client, user=chat.user)
        return chat
