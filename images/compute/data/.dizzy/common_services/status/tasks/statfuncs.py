from dizzy import Task


class Task(Task):
    """A task"""

    @staticmethod
    def run(ctx):
        ctx["Task"] = "A"
        return "Task"


class Info(Task):
    """B task"""

    dependencies = ["Task"]

    @staticmethod
    def run(ctx):
        ctx["Info"] = f"Info about {ctx['Task']}"
        return f"{ctx['Task']}"
