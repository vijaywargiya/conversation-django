from datetime import datetime

import pytz

from cartloop.constants import ChatStatus
from cartloop.models import Chat
from cartloop.schedules.constants import TIMEZONES, TIME_RANGE


class SendMessages:
    """
    Send messages periodic job. Runs every hour
    """

    def __init__(self):
        """
        Init method.
        """
        eligible_chats = self._collect_messages_to_send()
        self._send_all(eligible_chats)

    def _collect_messages_to_send(self) -> [Chat]:
        """
        Collect chats that are eligible to be sent

        Returns:
            [Chat]: eligible chats
        """
        eligible_chats = Chat.objects.filter(user__timezone__in=self._active_timezones(),
                                             status=ChatStatus.New.value).order_by('created_at').limit(90)

        return eligible_chats

    def _send_all(self, chats: [Chat]):
        """
        Iterated through the chat objects and sends them one by one.

        Args:
            chats:

        Returns:
            None:
        """
        for chat in chats:
            self._send(chat)

    def _send(self, chat: Chat):
        """
        Sends chat and updates the status to Sent. Currently mocked

        Args:
            chat: chat object that needs to be sent

        Returns:
            None
        """
        # does not send the chat currently

        chat.status = ChatStatus.Sent
        chat.save()

    def _active_timezones(self) -> [str]:
        """
        Returns the list of active timezones.

        Returns:
            [str]: List of active timezones
        """
        return [
            timezone for timezone in TIMEZONES if self._is_timezone_active(timezone)
        ]

    def _is_timezone_active(self, timezone: str) -> bool:
        """
        Checks if the passed timezone is suitable for sending messages or not.

        Args:
            timezone: timezone to be checked

        Returns:
            bool: true if the timezone is active
        """
        current_datetime = datetime.now().astimezone(pytz.timezone(timezone))
        return True if TIME_RANGE[0] < current_datetime.time() < TIME_RANGE[1] else False
