from __future__ import annotations

from pydantic import BaseModel


class UserConsole(BaseModel):
    command_history: list[History]
    current_scope: list[str]


class Command(BaseModel):

    console: UserConsole

    def action(self) -> str:
        raise NotImplementedError(
            f'Command {self.__class__.__name__}'
            'does not implement action method')


class History(BaseModel):
    command: type[Command] | None
    output: str
