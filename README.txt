Q: What are the moving pieces of an action? I.e., if a player hits "up" to move up?

A: Events are captured in main.py and passed to engine's handle_events method.

(Engine is made up 4 parts, so far: entities, event_handler, game_map, and player (object from entity class))

In handle_events method, for all events, we pass them to input_handler's event_handler method

The precise subclass of the action + relevant info is captured in variable "action" and we return to
engine's handle_events method. The subclass's perform method is then called (actions.py). In perform, if the player won't
go out of bounds and can walk on the tile, entity's  move method is called, which adds the relevant info the player's variables.

Q: What is the purpose of engine.py?

A: Engine.py is the first "stop" for events. It also draws tiles and entities to the screen.