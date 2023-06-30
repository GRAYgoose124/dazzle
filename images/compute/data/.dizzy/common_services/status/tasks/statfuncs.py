import logging
from dizzy import Task

logger = logging.getLogger(__name__)


class Task(Task):
    """A task"""

    @staticmethod
    def run(ctx):
        ctx["Task"] = "A"
        return "Task"


class Info(Task):
    """Gets info about loaded services."""

    requested_actions = ["entity_info", "service_info"]

    @staticmethod
    def run(ctx):
        try:
            info = Info.get_action("entity_info")()
        except Exception as e:
            logger.error(f"Error getting entity info: {e}")
            info = {}

        ctx["entity_info"] = info

        return info
