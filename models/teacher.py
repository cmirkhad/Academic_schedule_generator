class Teacher:
    def __init__(self, id, name, surname, working_days, working_graphic):
        self.id = id
        self.name = name
        self.surname = surname
        self.working_days = working_days
        self.working_graphic = working_graphic

    @classmethod
    def getNameById(cls, teachers, id):
        for i in teachers:
            if i.id == id:
                return f'{i.name} {i.surname}'
        return "No teacher with this id"
