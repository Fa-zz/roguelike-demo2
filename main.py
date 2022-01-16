import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler


def main():
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet("dejavu16x16_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    event_handler = EventHandler()

    with tcod.context.new_terminal(
            screen_width,
            screen_height,
            tileset=tileset,
            title="Tutorial",
            vsync=True
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")  # This sets up the console with our width and height. Order="F" is for numpy library
        while True:
            root_console.print(x=player_x, y=player_y, string="@") # Prints the player's x and y coordinates to console

            context.present(root_console)   # This method updates/refreshes the screen

            root_console.clear()

            for event in tcod.event.wait():

                action = event_handler.dispatch(event)  # Essentially (event_handler.ev_quit or event_handler.ev_keydown)

                if action is None:  # Remember that action is either None or an action subclass.
                    continue

                if isinstance(action, MovementAction):  # If action is an instance of MovementAction
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()