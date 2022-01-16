class Action:
    pass


class EscapeAction(Action):  # Used when the player hits "Esc". Subclass of action
    pass


class MovementAction(Action):  # Used when the player is moving around. Subclass of action
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy