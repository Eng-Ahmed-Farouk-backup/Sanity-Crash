class Item:
    def __init__(self, name, description, buying_price = 0, selling_price = 0):
        self.name = name
        self.description = description

    def use(self, player):
        pass

class HealthPotion1(Item):
    def __init__(self):
        super().__init__("Health Potion", "Restores 10 HP", 5, 3)
    def use(self, player):
        player.heal(10)
        player.inventory.remove(self)

class HealthPotion2(Item):
    def __init__(self):
        super().__init__("Health Potion+", "Restores 20 HP", 13, 10)
    def use(self, player):
        player.heal(20)
        player.inventory.remove(self)

class HealthPotion3(Item):
    def __init__(self):
        super().__init__("Health Potion++", "Restores 35 HP", 25, 17)
    def use(self, player):
        player.heal(35)
        player.inventory.remove(self)
