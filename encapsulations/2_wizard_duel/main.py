class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    """
    1. get_fireballed() should:
        1. Reduce the fireball_damage by the wizard's __stamina
        2. Reduce the wizard's health by the resulting fireball_damage
    """
    def get_fireballed(self, fireball_damage):
        fireball_damage -= self.__stamina
        self.health -= fireball_damage

    """
    2. drink_mana_potion() should:
        1. Increase the potion_mana by the wizard's __intelligence
        2. Increase the wizard's mana by the resulting potion_mana
    """
    def drink_mana_potion(self, potion_mana):
        potion_mana += self.__intelligence
        self.mana += potion_mana