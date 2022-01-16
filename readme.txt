

Q. Why did we create actions.py and input_handlers.py?

A. We need 2 files to deal with actions/inputs of the player. The first will hold the actions
our game can perform  while the second will bridge the gap between those actions
and the keys that we press.

Q: What are the moving pieces of an action?

A: Events are passed to input_handlers.EventHandler via main.py. The relevant subclass is determined and the relevant information
   (i.e., movement amount) is also passed to the subclass in actions.py. The subclass kind is stored in action variable
   and passed back to main.py.

   Back in main.py, we first determine which subclass the action is, then do the relevant calculation.

### main.py

Variables:
    * screen_width
    * screen_height
    * player_x
    * player_y
    * tileset
    * event_handler: Instance of EventHandler() which we import in main

    Methods:

    a. main()

        for event in tcod.event.wait():

            This passes events into either event_handler.ev_quit or event_handler.ev_keydown and assigns the action subclass to action

            Then checks if action is None or subclass of MovementAction or subclass of EscapeAction. Performs relevant calculations using info stored in subclass.


### input_handlers.py

    ## Class EventHandler

        Methods:

        a. ev_quit(self, event: tcod.event.Quit)

            Raises SystemExit(), just for when the player quits the game

        b. ev_keydown(self, event: tcod.event.KeyDown)

            Takes in key presses the player does. Matches key presses to action types and returns action. Passes relevant
            info to relevant subclass.

