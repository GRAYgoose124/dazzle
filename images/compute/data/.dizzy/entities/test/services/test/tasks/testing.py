from dizzy import Task


class TestA(Task):
    """A task"""

    @staticmethod
    def run(ctx):
        ctx["TestA"] = "A"
        return "TestA"


class TestB(Task):
    """B task"""

    dependencies = ["TestA"]

    @staticmethod
    def run(ctx):
        ctx["TestB"] = f"{ctx['TestA']}B"
        return f"{ctx['TestA']}B"