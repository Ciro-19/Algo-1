from random import choice

class MyGame:
    def __init__(self, choice_user, choice_ia):
        self.choice_user = choice_user
        self.choice_ia = choice_ia
    

    def is_winner(self):
        if (self.choice_user == "feuille" and self.choice_ia == "pierre") or (self.choice_user == "pierre" and self.choice_ia == "ciseau") or (self.choice_user == "ciseau" and self.choice_ia == "feuille"):
            return 1
        elif (self.choice_user == self.choice_ia):
            return 2
        else:
            return 0


class Player:
    def __init__(self,name_user,liste_choix):
        self.liste_choix = liste_choix
        print("Joueur {}".format(name_user))


    def choice_user_possi(self):
        cpt = 0
        for i in self.liste_choix:
            print("{} - {}".format(cpt,i))
            cpt += 1
        choice_user = -1
        while choice_user < 0 or choice_user > 2:
            choice_user = int(input("votre choix : "))
        return choice_user
        



def continue_game_func():
    continue_game = ""
    while continue_game != "y" and continue_game != "n":
        continue_game = input("continuer ? (y/n)")
    return continue_game

continue_game = "o"
liste_choix = ["pierre", "feuille", "ciseau"]
name_user = input("votre nom: ")
while continue_game != "n":
    player_1 = Player(name_user, liste_choix).choice_user_possi()
    choice_ia = choice(liste_choix)
    print("choix ia = {}".format(choice_ia))
    print("choix user = {}".format(liste_choix[player_1]))
    control_game = MyGame(liste_choix[player_1], choice_ia)
    print(control_game.is_winner())
    if control_game.is_winner() == 1:
      print("gagner")
    elif control_game.is_winner() == 2:
      print("égalité")
    else:
      print("perdu")
    continue_game = continue_game_func()






