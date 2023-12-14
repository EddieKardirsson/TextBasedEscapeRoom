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


class GameMode:
    # Member variables made up of amount of attempts solving the code and instantiating the room
    def __init__(self):
        self.attempts = 0
        objects = self.create_objects()
        self.room = Room(731, objects)

    # Returns a list with all the objects in the room
    def create_objects(self):
        return [GameObject(
            "Sweater",
            "It's a blue sweater that had the number 12 switched on it.",
            "Someone has unstitched the second number, leaving only the 1.",
            "The sweater smells of laundry detergent."),
            GameObject(
                "Chair",
                "It's a wooden chair with only 3 legs.",
                "Someone had deliberately snapped off one of the legs.",
                "It smells like old wood."),
            GameObject(
                "Journal",
                "The final entry states that time should be hours then minutes then seconds (H-M-S).",
                "The cover is worn and several pages are missing.",
                "It smells like musty leather."),
            GameObject(
                "Bowl of soup",
                "It appears to be tomato soup.",
                "It has cooled down to room temperature.",
                "You detect 7 different herbs and spices."),
            GameObject(
                "Clock",
                "The hour hand is pointing towards the soup, the minute hand towards the chair, "
                "and the second hand towards the sweater.",
                "The battery compartment is open and empty.",
                "It smells of plastic."), ]

    # Player will see a prompt during each turn
    def take_turn(self):
        prompt = self.get_room_prompt()
        selection = int(input(prompt))
        # Only takes the selection prompted if it's a valid input
        if selection >= 1 and selection <= 5:
            self.select_object(selection-1)
            self.take_turn()

    # Generates a prompt including the names of he objects inside the room
    def get_room_prompt(self):
        prompt = "Enter the 3-digit lock code or choose an item to interact with:\n"
        index = 1
        for name in self.room.get_game_object_names():
            prompt += f"{index}. {name}\n"
            index += 1
        return prompt

    # Selects the object player chooses and prompts for interaction
    def select_object(self, index):
        selected_object = self.room.game_objects[index]
        prompt = self.get_object_interaction_string(selected_object.name)
        interaction = input(prompt)
        clue = self.interact_with_object(selected_object, interaction)
        print(clue)

    # Returns object interaction prompt
    def get_object_interaction_string(self, name):
        return (f"How do you want to interact with the {name}?\n"
                f"1. Look\n"
                f"2. Touch\n"
                f"3. Smell\n")

    # Shows the interaction message
    def interact_with_object(self, object, interaction):
        if interaction == "1":
            return object.look()
        elif interaction == "2":
            return object.touch()
        else:
            return object.sniff()
        return ""


# Debug/Test: Create a GameMode instance and call the take_turn() function that returns
# a console prompt with a list of objects
game = GameMode()
game.take_turn()
