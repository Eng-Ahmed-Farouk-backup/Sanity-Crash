import random
class Enemy:
    def __init__(self, name, hp, attack, defense = 0, armor_penetration = 0, armor = 0, agility = 0, loot = {}):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.armor_penetration = armor_penetration
        self.armor = armor
        self.agility = agility
        self.loot = loot
    def is_alive(self):
        return self.hp > 0
    def take_damage(self, player):
        if player.get_agility() > self.agility and random.random() < player.get_agility() - self.agility:
            return -1
        damage = max(player.get_attack() - self.defense, 0)
        damage = max(damage - (self.get_armor() - player.get_armor_penetration()), 0)
        self.hp -= damage
        return damage
    def get_attack(self):
        return self.attack
    def get_defense(self):
        return self.defense
    def get_armor_penetration(self):
        return self.armor_penetration
    def get_armor(self):
        return self.armor
    def get_agility(self):
        return self.agility
    def drop_loot(self):
        loot = []
        for item, chance in self.loot.items():
            if random.random() < chance:
                loot.append(item)
        return loot
