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


def choice_user_possi(liste_choix):
    cpt = 0
    for i in liste_choix:
        print("{} - {}".format(cpt,i))
        cpt += 1
    choice_user = input("votre choix : ")
    try:
        choice_user = int(choice_user)
        return choice_user
    except:
        print("entrez un chiffre: ")
        return choice_user_possi(liste_choix)


def continue_game_func():
    continue_game = ""
    while continue_game != "y" and continue_game != "n":
        continue_game = input("continuer ? (y/n)")
    return continue_game

continue_game = "o"
liste_choix = ["pierre", "feuille", "ciseau"]
while continue_game != "n":
    choice_user = choice_user_possi(liste_choix)
    choice_ia = choice(liste_choix)
    print("choix ia = {}".format(choice_ia))
    print("choix user = {}".format(liste_choix[choice_user]))
    control_game = MyGame(liste_choix[choice_user], choice_ia)
    print(control_game.is_winner())
    if control_game.is_winner() == 1:
      print("gagner")
    elif control_game.is_winner() == 2:
      print("égalité")
    else:
      print("perdu")
    continue_game = continue_game_func()






