class GameObject:

    def __init__(self, name, appearance, feel, smell):
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell

    def look(self):
        return f"You look at the {self.name}. {self.appearance}\n"

    def touch(self):
        return f"You touch the {self.name}. {self.feel}\n"

    def sniff(self):
        return f"You smell on the {self.name}. {self.smell}\n"


game_object = GameObject("Knife", "Some appearance", "Some feel", "Some smell")

print(game_object.sniff())
