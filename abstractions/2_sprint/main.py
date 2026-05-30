""""
In Age of Dragons, humans can "sprint" to move twice as fast. However, sprinting requires __stamina. Each time a human sprints, it loses stamina. Once it is out of stamina, it can no longer sprint.
"""

class Human:
    """
    Complete all the missing methods:
    """

    """
    2. For each of the sprint methods:
        1. Call __raise_if_cannot_sprint() to raise an exception if the human is out of stamina.
        2. Use __use_sprint_stamina() once to use the stamina needed to sprint.
        3. Move twice in the direction of the sprint.
    """
    def sprint_right(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.move_right()
        self.move_right()

    def sprint_left(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.move_left()
        self.move_left()

    def sprint_up(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.move_up()
        self.move_up()

    def sprint_down(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.move_down()
        self.move_down()

    """
    Complete the private helper methods, which are intended to be used by the other four sprinting methods.
    1. __raise_if_cannot_sprint(): Raise the exception: not enough stamina to sprint if the human is out of stamina.
    2. __use_sprint_stamina(): Remove one stamina from the human.
    """
    def __raise_if_cannot_sprint(self):
        if self.__stamina <= 0:
            raise Exception("not enough stamina to sprint")

    def __use_sprint_stamina(self):
        self.__stamina -= 1

    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed

    def get_position(self):
        return self.__pos_x, self.__pos_y

    def __init__(self, pos_x, pos_y, speed, stamina):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed
        self.__stamina = stamina