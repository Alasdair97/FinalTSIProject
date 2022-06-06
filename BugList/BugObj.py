from abc import ABC


class Bug(ABC):
    # Attributes
    Bug_ID_Counter = 0

    # Constructors
    def __init__(self, servarity, type, error_code):
        self.Value = "Bug"
        self.Servarity = str(servarity)
        self.Type = str(type)
        self.Code = str(error_code)
        self.id = Bug.Bug_ID_Counter
        Bug.Bug_ID_Counter += 1

    # Methods
    def type(self, description):
        self.Description = str(description)
