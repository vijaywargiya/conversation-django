from django.core.validators import RegexValidator
from jinja2 import Template

from cartloop.models import Chat, Conversation


class ChatController:
    """
    Chat controller. Renders the chat payload.
    """
    payload_validator = RegexValidator(r'^[0-9a-zA-Z:{}$%_\-\/~@#^&*()!?. ]*$',
                                       'Invalid Payload')

    @staticmethod
    def render_all(conversation: Conversation) -> [Chat]:
        """
        render all the chats belonging to a conversation

        Args:
            conversation:

        Returns:
            [Chat]: rendered chats
        """
        return [ChatController.render_chat(chat, conversation) for chat in conversation.chat_set.all()]

    @staticmethod
    def render_chat(chat: Chat, conversation: Conversation) -> Chat:
        """
        Render a chat. Uses jinja 2.

        Args:
            chat: Chat object to be rendered
            conversation: Conversation object to be used to get data for rendering

        Returns:
            [Chat]:
        """
        template = Template(chat.payload)
        chat.payload = template.render(operator=conversation.operator, store=conversation.store,
                                       client=conversation.client, user=chat.user)
        return chat
