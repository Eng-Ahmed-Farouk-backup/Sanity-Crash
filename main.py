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



class Act1:
    def __init__(self, player):
        self.player = player
    def beginning(self):
        println(f"""You are {self.player.name}
                Your grandmother passed away 3 years ago
                And for her memorial, You and other members of your family go to visit her grave
                Her grave is in the middle of the desert as she wanted to be buried there
                Since the grave is very far away, you and your family go there by a bus you rented
                For respect, all of you do not take your phones with you
                You are preparing for this long trip
                """)
        options = ["Go with your family","Fake being sick to stay home","Refuse going to the grave"]
        option = interactive_menu(options,"What do you do?")
        if option == options[0]:
            println("You go with your family to the grave")
            self.act1()
        elif option == options[1]:
            println("""
                    You fake being sick
                    Your family to go to the grave without you""")
            self.act2()
        elif option == options[2]:
            println("""
                    You refuse going to the grave
                    Your family is very angry and decides you will go there by force""")
            self.act1()
    def act1(self):
        println("""
                You go on the bus with your family
                After a few hours, you arrive at the grave
                After doing your prayers, you decide to explore the desert alone for fun
                You go to discover the desert but your uncle got sick in the middle of the day
                Your Family decides to go back and take your uncle to the hospital
                You do not notice and you keep exploring
                When you come back and do not find your family
                You start to panic and try to find them but you cannot find them
                """)
        options = ["Keep wandering in the desert","Keep waiting in the grave"]
        option = interactive_menu(options,"What do you do?")
        if option == options[0]:
            self.act2_1()
        elif option == options[1]:
            println("""
                    You wait at the grave
                    Your family finally notices you are missing and they come back to find you
                    They find you at the grave and they are very mad at you
                    They decide to leave you at the grave and go back to the city without you"""
            )
            self.act2_1()
    def act2_1(self):
        println("""
                You wander in the desert
                But suddenly a bandit appears and tries to rob you""")
        bandit = Enemy("Bandit", 30, 8, 0, 0, 0, 0.05, {HealthPotion1():0.5})
        fight(self.player, bandit)
        if not self.player.is_alive():
            println("""
                    You died in the desert
                    Your family finds your body
                    You are buried next to your grandmother
                    GAME OVER""")
            os._exit(1)
        else:
            println("You have defeated the bandit")
            options = ["Keep wandering in the desert","Keep waiting in the grave"]
            option = interactive_menu(options,"What do you do?")
            if option == options[0]:
                self.act3_1()
            elif option == options[1]:
                self.act3_2()
    def act3_1(self):
        println("""
                You keep wandering in the desert
                But now you find a house in the middle of the desert
                You knock on the door
                Nobody answers at first
                But then
                A man opens the door and invites you in""")
        options = ["Go inside the house","Refuse and keep wandering in the desert"]
        option = interactive_menu(options,"What do you do?")
        if option == options[0]:
            self.act4_1()
        elif option == options[1]:
            println("""
                    You refuse to go inside the house
                    The man sees that as very disrespectful and he gets very mad
                    He decides to attack you""")
            man = Enemy("Stranger", 80, 15, 0, 0, 0, 0.3, {HealthPotion2():0.5})
            fight(self.player,man)
            if not self.player.is_alive():
                println("""
                        You died in the desert
                        The man does not bury you
                        He eats your body and leaves your bones in the desert for scavengers to eat
                        GAME OVER""")
                os._exit(1)
            else:
                println("""
                        You enter the house and stay there for a week
                        The police finally finds you and they take you back to the city
                        You get arrested and executed for murdering the man""")
                os._exit(1)
    def act3_2(self):
        println("""
                You go back to the grave and keep waiting there
                But you notice that there were footsteps that feel new
                You realize that your family came back to the grave to check if you were there
                But they did not find you and they left again""")
        options = ["Keep waiting in the grave","Go back to wandering in the desert"]
        option = interactive_menu(options,"What do you do?")
        if option == options[0]:
            println("""
                    You keep waiting in the grave
                    But no one comes back
                    You die of thirst and hunger in the desert
                    After you die by an hour
                    The police finds your body and your family buries you next to your grandmother""")
            os._exit(1)
        elif option == options[1]:
            self.act3_1()
    def act4_1(self):
        println("""
                You enter the house and the man is very nice to you
                He gives you food and water but on one condition
                For every day you stay in his house you have to do a task for him and give him 5 golden coins
                """)
        options = ["Accept the deal and stay in the house","Refuse the deal"]
        option = interactive_menu(options,"What do you do?")
        if option == options[0]:
            self.act5_1()
        elif option == options[1]:
            println("The man gets very angry at you and he decides to attack you")
            man = Enemy("Stranger", 80, 15, 0, 0, 0, 0.3, {HealthPotion2():0.5})
            fight(self.player,man)
            if not self.player.is_alive():
                println("""
                        You died in the desert
                        The man does not bury you
                        He eats your body and leaves your bones in the desert for scavengers to eat
                        GAME OVER""")
                os._exit(1)
            else:
                println("""
                        You stay at the house for a week after defeating the man
                        The police finally finds you and they take you back to the city
                        You get arrested and executed for murdering the man
                        GAME OVER""")
                os._exit(1)
    def act5_1(self):
        println("""
                You accept the deal and you stay in the house
                For the first day He wants you to fight his child to train him""")
        child = Enemy("Child", 20, 5, 0, 0, 0, 0.3)
        fight(self.player, child)
        if not self.player.is_alive():
            println("""
                    The child defeated you
                    The man is very mad about how weak you are
                    He decides that you will be the snack for his child and he kills you and feeds you to his child
                    GAME OVER""")
            os._exit(1)
        else:
            println("""
                    The man is impressed by your strength and feels proud of his child
                    He lets you stay in the house and lets you eat with him and his child
                    You sleep for the day and the next day he gives you a task to do
                    You have to go to a nearby village and get the 5 gold that a villager owes the man""")
            options = ["Accept the task and go to the village","Refuse the task"]
            option = interactive_menu(options,"Do you accept the task?")
            if option == options[0]:
                self.act6_1()
            elif option == options[1]:
                println("The man gets very mad at you and he decides to attack you")
                man = Enemy("Stranger", 80, 15, 0, 0, 0, 0.3, {HealthPotion2():0.5})
                fight(self.player,man)
                if not self.player.is_alive():
                    println("""
                            You died in the desert
                            The man does not bury you
                            He eats your body and leaves your bones in the desert for scavengers to eat
                            GAME OVER""")
                    os._exit(1)
                else:
                    println("""
                            You stay at the house for a week
                            The police finally finds you and they take you back to the city
                            You get arrested and executed for murdering the man
                            GAME OVER""")
                    os._exit(1)
    def act6_1(self):
        println("You go to the village")
        options = ["Go to the villager and ask for the money","Go to the market","Go back to the house"]
        option = interactive_menu(options,"What do you do?")
        if option == options[2]:
            println("""
                    You return back to the house and the man gets very mad that you did not complete the task
                    He attacks you and you have to fight him""")
            man = Enemy("Stranger", 80, 15, 0, 0, 0, 0.3, {HealthPotion2():0.5})
            fight(self.player,man)
            if not self.player.is_alive():
                println("""
                        You died in the desert
                        The man does not bury you
                        He eats your body and leaves your bones in the desert for scavengers to eat
                        GAME OVER""")
                os._exit(1)
            else:
                println("""
                        You stay at the house for a week
                        The police finally finds you and they take you back to the city
                        You get arrested and executed for murdering the man
                        GAME OVER""")
                os._exit(1)
        elif option == options[1]:
            self.act_market1()
        elif option == options[0]:
            self.act7_1()
    
    def act_market1(self):
        println(""""
                You go to the market and you find a trader selling items
                You can buy items from the trader or you can steal from him
                You can also go to the villager to ask for the money""")
        options = ["Buy from the trader","Steal from the trader","Go to the villager"]
        option = interactive_menu(options,"What do you do?")
        if option == options[0]:
            items = {
                HealthPotion1(): 10,
                HealthPotion2(): 20,
                StrengthPotion1(): 15,
                StrengthPotion2(): 30
            }
            self.market_buy(items)
        elif option == options[1]:
            self.market_steal()
        elif option == options[2]:
            self.act7_1()
    
    def act7_1(self):
        println("""
                You go to the villager and ask for the money
                the villager asks about your story and you tell him about your situation
                the villager is very kind and he offers to fight the man for you
                You accept and he goes to fight the man
                You go with him to the house and he beats the man
                You thank him and he goes away
                You stay at the house for a week with the child of the man
                TO BE CONTINUED...""")
        

        

        


if __name__ == "__main__":
    game = Game()
            println(f"Player name set to {self.settings['Player name']}")
