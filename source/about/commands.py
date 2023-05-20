from about.console import Command, UserConsole


class Help(Command):

    def action(self, console: UserConsole, command_name: str | None) -> None:
        print("Help: ", args, kwargs)
