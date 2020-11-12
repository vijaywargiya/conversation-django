from enum import Enum


class ChatStatus(str, Enum):
    """
    Chat Status
    """

    New = "New"
    Sent = "Sent"

    @classmethod
    def choices(cls):
        return tuple((x.name, x.value) for x in cls)


class OperatorGroup(str, Enum):
    """
    Operator Groups
    """

    Sales = "Sales"

    @classmethod
    def choices(cls):
        return tuple((x.name, x.value) for x in cls)
