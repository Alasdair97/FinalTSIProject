from abc import ABC


class Bug(ABC):
    # Attributes
    Bug_ID_Counter = 0

    # Constructors
    def __init__(self, servarity, type, description):
        self.Value = "Bug"
        self.Servarity = servarity
        self.Type = type
        self.Description = description
        self.id = Bug.Bug_ID_Counter
        Bug.Bug_ID_Counter += 1