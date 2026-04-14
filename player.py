import random
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 50
        self.max_hp = 50
        self.base_attack = 10
        self.inventory = []
        self.base_defense = 0
        self.armor_penetration = 0
        self.base_armor = 0
        self.base_agility = 5/100
    def is_alive(self):
        return self.hp > 0
    def take_damage(self, enemy):
        if enemy.get_agility() > self.base_agility and random.random() < enemy.get_agility() - self.base_agility:
            return -1
        damage = max(enemy.get_attack() - self.get_defense(), 0)
        damage = max(damage - (self.get_armor() - enemy.get_armor_penetration()), 0)
        self.hp -= damage
        return damage
    def heal(self, amount):
        self.hp = min(self.hp + amount, self.max_hp)
    def add_item(self, item):
        self.inventory.append(item)
    def use_item(self, item):
        item.use(self)
    def get_attack(self):
        return self.base_attack
    def get_defense(self):
        return self.base_defense
    def get_armor_penetration(self):
        return self.armor_penetration
    def get_armor(self):
        return self.base_armor
    def get_agility(self):
        return self.base_agility
