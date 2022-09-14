class Fan_club:
    def __init__(self, name):
        self.__name = name
        self.__status = "not activated"

    def __str__(self):
        return f"Fan_club {self.__name} {self.__status}"


    def activate(self):
        self.__status = "activated"


if __name__ == "__main__":
    team = Fan_club("Стасіка")
    team.activate()
    print(team)
