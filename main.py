class GameObject:
    # Initialize properties for name, appearance, feel and smell
    def __init__(self, name, appearance, feel, smell):
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell

    # Return string describing the object appearance
    def look(self):
        return f"You look at the {self.name}. {self.appearance}\n"

    # Return string describing object feel
    def touch(self):
        return f"You touch the {self.name}. {self.feel}\n"

    # Return string describing object smell
    def sniff(self):
        return f"You smell on the {self.name}. {self.smell}\n"


class Room:
    # Room class with an escape code and a list of game objects as member variables
    def __init__(self, escape_code, game_objects=[]):
        self.escape_code = escape_code
        self.game_objects = game_objects

    # Returns if the code player enters match with the escape code
    def check_code(self, code):
        return self.escape_code == code

    # Returns a list of the names of the game objects existing inside the room
    def get_game_object_names(self):
        names = []
        for obj in self.game_objects:
            names.append(obj.name)
        return names


obj_knife = GameObject("Knife", "It looks sharp", "It feels light", "It smells like metal")
obj_cardbox = GameObject("Cardbox", "It looks like a generic cardbox", "It feels soft", "It smells like shit")

game_objects = [obj_knife, obj_cardbox]

room = Room(384, game_objects)

print(room.get_game_object_names())
print(room.check_code(666))
print(room.check_code(384))
