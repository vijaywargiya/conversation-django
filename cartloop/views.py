from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from cartloop.models import Conversation, Chat, Client, User, Store, Operator, DiscountCode
from cartloop.serializers import ChatSerializer, UserSerializer, StoreSerializer, \
    OperatorSerializer, DiscountCodeSerializer, ClientSerializer, ConversationSerializer


class ChatViewSet(ModelViewSet):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()


class ConversationViewSet(ModelViewSet):
    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all()

    def retrieve(self, request, pk=None):
        conversation = Conversation.objects.get(pk=pk)
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data)


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class StoreViewSet(ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()


class OperatorViewSet(ModelViewSet):
    serializer_class = OperatorSerializer
    queryset = Operator.objects.all()


class DiscountCodeViewSet(ModelViewSet):
    serializer_class = DiscountCodeSerializer
    queryset = DiscountCode.objects.all()
