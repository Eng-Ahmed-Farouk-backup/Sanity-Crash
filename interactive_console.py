import os
import time
import keyboard

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def interactive_menu(options, header = ""):
    current = 0
    clear_console()
    print(header)
    for i,option in enumerate(options):
        print(f"-> {option}" if i == current else f"   {option}")
    time.sleep(1)
    while True:
        clear_console()
        print(header)
        for i,option in enumerate(options):
            print(f"-> {option}" if i == current else f"   {option}")
        
        key = keyboard.read_key()
        if key == "up" or key == "down":
            current = (current + 1)%len(options) if key == "down" else (current - 1)%len(options)
        elif key == "enter":
            return options[current]
        


def println(msg):
    for m in msg.split("\n"):
        print(m)
        start_time = time.time()
        while time.time() < start_time+max(len(m)/25,3):
            key = keyboard.is_pressed("space")
            if key:break
        time.sleep(0.2)

def fight(player, enemy):
    println(f"You encountered {enemy.name}!")
    while player.is_alive() and enemy.is_alive():
        println(f"{player.name} HP: {player.hp} | {enemy.name} HP: {enemy.hp}")
        action = interactive_menu(["Attack","Run","Use Item"],"Choose your action:")
        if action == "Attack":
            damage = enemy.take_damage(player)
            if damage == -1:
                println(f"You dodged {enemy.name}'s attack!")
            else:
                println(f"You dealt {damage} damage to {enemy.name}!")
            if enemy.is_alive():
                damage = player.take_damage(enemy)
                if damage == -1:
                    println(f"You dodged {enemy.name}'s attack!")
                else:
                    println(f"{enemy.name} dealt {damage} damage to you!")
        elif action == "Run":
            println("You ran away!")
            break
        elif action == "Use Item":
            if not player.inventory:
                println("You have no items!")
                continue
            item_names = [item.name for item in player.inventory]
            item = interactive_menu(item_names,"Select an item to use:")
            selected_item = next(item for item in player.inventory if item.name == item)
            player.use_item(selected_item)
            println(f"You used {selected_item.name}!")
    loot = enemy.drop_loot()
    if loot:
        println(f"You found {', '.join(item.name for item in loot)} on {enemy.name} body!")
        player.inventory.extend(loot)
        

