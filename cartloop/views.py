from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from cartloop.models import Conversation, Chat, Client, User, Store, Operator, DiscountCode
from cartloop.serializers import ChatSerializer, UserSerializer, StoreSerializer, \
    OperatorSerializer, DiscountCodeSerializer, ClientSerializer, ConversationSerializer


class ChatViewSet(ModelViewSet):
    """
    Exposes endpoints for chat
    """

    serializer_class = ChatSerializer
    queryset = Chat.objects.all()


class ConversationViewSet(ModelViewSet):
    """
    Exposes endpoints for conversation
    """

    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all()

    def retrieve(self, request, pk=None):
        """
        retrieve conversation endpoint

        Args:
            request:
            pk:

        Returns:
            Response:
        """
        conversation = Conversation.objects.get(pk=pk)
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data)


class UserViewSet(ModelViewSet):
    """
    Exposes endpoints for user
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()


class ClientViewSet(ModelViewSet):
    """
    Exposes endpoints for client
    """

    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class StoreViewSet(ModelViewSet):
    """
    Exposes endpoints for store
    """

    serializer_class = StoreSerializer
    queryset = Store.objects.all()


class OperatorViewSet(ModelViewSet):
    """
    Exposes endpoints for operator
    """

    serializer_class = OperatorSerializer
    queryset = Operator.objects.all()


class DiscountCodeViewSet(ModelViewSet):
    """
    Exposes endpoints for discount code
    """

    serializer_class = DiscountCodeSerializer
    queryset = DiscountCode.objects.all()
