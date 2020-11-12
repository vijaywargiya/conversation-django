from django.db import models

from cartloop.constants import ChatStatus, OperatorGroup


class Client(models.Model):
    """
    Client Model
    """
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=100)


class Operator(models.Model):
    """
    Operator Model
    """
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=100)
    group = models.CharField(choices=OperatorGroup.choices(), max_length=20)


class User(models.Model):
    """
    User Model
    """
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=100)
    timezone = models.CharField(max_length=50)


class Store(models.Model):
    """
    Store Model
    """
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=100)
    timezone = models.CharField(max_length=50)

    @property
    def discount_code(self):
        return self.discountcode_set.first().value


class Conversation(models.Model):
    """
    Conversation Model
    """
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


class Chat(models.Model):
    """
    Chat Model
    """
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    payload = models.CharField(max_length=300)
    status = models.CharField(choices=ChatStatus.choices(), default=ChatStatus.New, max_length=20)

    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class DiscountCode(models.Model):
    """
    Discount Code Model
    """
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    value = models.CharField(max_length=100)

    store = models.ForeignKey(Store, on_delete=models.CASCADE)
