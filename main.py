from interactive_console import *
from player import Player
from enemy import Enemy
from items import *

class Game:
    def __init__(self):
        self.settings = {
            "difficulty":"Normal",
            "Player name":"Player"
        }
        self.player = Player(self.settings["Player name"])
        self.act = Act1(self.player)
        self.main_menu()
        
    def main_menu(self):
        println("Welcome to SANITY CRASH")
        while True:
            option = interactive_menu(["Play","Settings","Exit"])
            if option == "Exit":
                os._exit(1)
            elif option == "Settings":
                self.settings_menu()
            elif option == "Play":
                self.act.beginning()
            clear_console()

    def settings_menu(self):
        option = interactive_menu(["Difficulty: "+self.settings["difficulty"],"Player name: "+self.settings["Player name"],"Back"],"Settings")
        if option == "Back":
            return
        elif option.startswith("Difficulty: "):
            difficulties = ["Story Mode","Easy","Normal","Hard","Hardcore"]
            options = [f"Difficulty: {dif}" for dif in difficulties]
            option1 = interactive_menu(options,"Select Difficulty")
            self.settings["difficulty"] = option1.split(": ")[1]
            println(f"Difficulty set to {self.settings['difficulty']}")
        elif option.startswith("Player name: "):
            name = input("Enter player name: ")
            self.settings["Player name"] = name
            self.player.name = name
            println(f"Player name set to {self.settings['Player name']}")
