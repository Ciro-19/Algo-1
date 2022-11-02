class MyGame:
    def __init__(self:object, choice_user:str, choice_ia:str):
        self.choice_user = choice_user
        self.choice_ia = choice_ia
    

    def is_winner(self:object)->int:
        if (self.choice_user == "feuille" and self.choice_ia == "pierre") or (self.choice_user == "pierre" and self.choice_ia == "ciseau") or (self.choice_user == "ciseau" and self.choice_ia == "feuille"):
            return 1
        elif (self.choice_user == self.choice_ia):
            return 2
        else:
            return 0
    
    
    def continue_game_func(self:object)->str:
        continue_game = ""
        while continue_game != "y" and continue_game != "n":
            continue_game = input("continuer ? (y/n)")
        return continue_game


class Player:
    def __init__(self:object,name_user:str,liste_choix:list):
        self.liste_choix = liste_choix
        print("Joueur {}".format(name_user))


    def choice_user_possi(self:object)->str:
        cpt = 0
        for i in self.liste_choix:
            print("{} - {}".format(cpt,i))
            cpt += 1
        choice_user = -1
        while choice_user < 0 or choice_user > 2:
            choice_user = int(input("votre choix : "))
        return self.liste_choix[choice_user]


class Ia:
    def __init__(self:object, liste_choix:list, liste_coup:list):
        self.liste_choix = liste_choix
        self.liste_coup = liste_coup


    def Ia_choice(self:object)->str:
        if self.liste_coup[1] >= 2:
            if self.liste_coup[0] == "feuille":
                choix_ia = "ciseau"
            elif self.liste_coup[0] == "pierre":
                choix_ia = "feuille"
            else:
                choix_ia = "pierre" 
        else:
            coup_jouer = []
            with open("dataUser.txt", "r") as file_data_open:
                for row in file_data_open:
                    coup_jouer.append(row)
            coup_jouer = "".join(coup_jouer).split()
            if len(coup_jouer) != 0:
                if max(coup_jouer, key=coup_jouer.count) == "pierre":
                    choix_ia = "feuille"
                elif max(coup_jouer, key=coup_jouer.count) == "feuille":
                    choix_ia = "ciseau"
                else:
                    choix_ia = "pierre"
            else:
                choix_ia = "feuille"
        
        return choix_ia


continue_game = "o"
liste_choix = ["pierre", "feuille", "ciseau"]
name_user = input("votre nom: ")
point_ia = 0
point_user = 0
nbre_coup_pierre = 0
nbre_coup_ciseau = 0
nbre_coup_feuille = 0
liste_coup = [0,0]
while continue_game != "n":
    player_1 = Player(name_user, liste_choix).choice_user_possi()
    with open("dataUser.txt", "a") as file_data:
        file_data.write(" " + player_1)
    player_ia = Ia(liste_choix, liste_coup).Ia_choice()
    print("choix ia = {}".format(player_ia))
    print("choix user = {}".format(player_1))
    control_game = MyGame(player_1, player_ia)
    print(control_game.is_winner())
    if control_game.is_winner() == 1:
        print("gagner")
        point_user += 1
    elif control_game.is_winner() == 2:
        print("égalité")
    else:
        print("perdu")
        point_ia += 1
    if player_1 == "pierre":
        nbre_coup_pierre += 1
        nbre_coup_ciseau = 0
        nbre_coup_feuille = 0
        liste_coup = [player_1, nbre_coup_pierre]
    elif player_1 == "feuille":
        nbre_coup_feuille += 1
        nbre_coup_ciseau = 0
        nbre_coup_pierre = 0
        liste_coup = [player_1, nbre_coup_feuille]
    else:
        nbre_coup_ciseau += 1
        nbre_coup_pierre = 0
        nbre_coup_feuille = 0
        liste_coup = [player_1, nbre_coup_ciseau]
    continue_game = control_game.continue_game_func()
if point_user < point_ia:
    print("Ia gagne avec une avance de ", point_ia - point_user, "et un score de = ", point_ia)
elif point_user > point_ia:
    print("User gagne avec une avance de ", point_user - point_ia, "et un score de = ", point_user)
else:
    print("égalité parfaite point ia = {}, point user = {}".format(point_ia, point_user))






