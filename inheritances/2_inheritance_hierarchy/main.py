"""
Let's add a new game unit: Crossbowman. A crossbowman is always an archer, but not all archers are crossbowmen. Crossbowmen have several arrows, but they have an additional method: triple_shot().
"""

class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    """
    1. Complete the use_arrows method on the Archer class. It should remove num arrows, but if there aren't enough arrows to remove, it should raise a not enough arrows exception instead.
    """
    def use_arrows(self, num):
        if self.__num_arrows <= num:
            raise Exception("not enough arrows")
        self.__num_arrows -= num

"""
2. Complete the Crossbowman class.
    1. Its constructor should call its parent's constructor.
    2. Its triple_shot method should:
        - Use 3 arrows
        - Get the name of the target Human using its methods
        - Return the string TARGET was shot by 3 crossbow bolts where TARGET is the name of the Human that was shot
"""
class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)

    def triple_shot(self, target):
        self.use_arrows(3)
        target_name = target.get_name()
        return f"{target_name} was shot by 3 crossbow bolts"