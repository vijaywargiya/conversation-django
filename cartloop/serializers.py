from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from cartloop.controllers.ChatController import ChatController
from cartloop.models import Chat, Conversation, User, Client, Operator, DiscountCode, Store


class ChatSerializer(ModelSerializer):
    """
    Serializer for routine block endpoint
    """
    status = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    conversation_id = serializers.IntegerField(source="conversation.id")
    user_id = serializers.IntegerField(source="user.id")
    payload = serializers.CharField(max_length=300, validators=[ChatController.payload_validator])

    class Meta:
        model = Chat
        fields = ('conversation_id', 'user_id', 'payload', 'created_at', 'status')

    def create(self, validated_data):
        instance = Chat(user_id=validated_data['user']['id'],
                        conversation_id=validated_data['conversation']['id'],
                        payload=validated_data['payload'])
        instance.save()
        return instance


class ConversationSerializer(ModelSerializer):
    """
    Serializer for routine block endpoint
    """
    conversation_id = serializers.IntegerField(source="id", read_only=True)

    store_id = serializers.IntegerField(source="store.id")
    operator_id = serializers.IntegerField(source="operator.id")
    client_id = serializers.IntegerField(source="client.id")

    operator_group = serializers.CharField(source="operator.group", read_only=True)
    chats = serializers.SerializerMethodField('get_chats', read_only=True)

    class Meta:
        model = Conversation
        fields = ('conversation_id', 'store_id', 'operator_id', 'client_id', 'operator_group', 'chats')

    def create(self, validated_data):
        instance = Conversation(store_id=validated_data['store']['id'],
                                operator_id=validated_data['operator']['id'],
                                client_id=validated_data['client']['id'])
        instance.save()
        return instance

    def get_chats(self, obj):
        rendered_chats = ChatController.render_all(obj)
        serializer = ChatSerializer(rendered_chats, many=True)
        return serializer.data


class UserSerializer(ModelSerializer):
    """
    Serializer for routine block endpoint
    """

    class Meta:
        model = User
        fields = ('__all__')


class StoreSerializer(ModelSerializer):
    """
    Serializer for routine block endpoint
    """

    class Meta:
        model = Store
        fields = ('__all__')


class OperatorSerializer(ModelSerializer):
    """
    Serializer for routine block endpoint
    """

    class Meta:
        model = Operator
        fields = ('__all__')


class DiscountCodeSerializer(ModelSerializer):
    """
    Serializer for routine block endpoint
    """
    store_id = serializers.IntegerField(source="store.id")

    class Meta:
        model = DiscountCode
        fields = ('id', 'store_id', 'value', 'created_at')

    def create(self, validated_data):
        instance = DiscountCode(store_id=validated_data['store']['id'],
                                value=validated_data['value'])
        instance.save()
        return instance


class ClientSerializer(ModelSerializer):
    """
    Serializer for routine block endpoint
    """

    class Meta:
        model = Client
        fields = ('__all__')
