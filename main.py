"""
sam
lucas
idriss
"""
class MyGame:
    def __init__(self:object, name_user:str):
        self.name_user = name_user
        ROCK = "rock"
        PAPER = "paper"
        SCISSOR = "scissor"
        self.winner = {
            (ROCK , PAPER): PAPER,
            (PAPER , SCISSOR): SCISSOR,
            (SCISSOR , ROCK): ROCK,
            (ROCK , ROCK): 2,
            (PAPER , PAPER): 2,
            (SCISSOR , SCISSOR): 2
        }


    def _is_winner(self:object, choice_user:str,choice_ia:str)->int:
        try:
            if choice_ia == self.winner[(choice_user, choice_ia)]:
                return 0
            return self.winner[(choice_user, choice_ia)]
        except:
            return 1

    
    def _nbrePoint(self:object, point_user:int, point_ia:int):
        if point_user < point_ia:
            print("Ia gagne avec une avance de ", point_ia - point_user, "et un score de = ", point_ia)
        elif point_user > point_ia:
            print("User gagne avec une avance de ", point_user - point_ia, "et un score de = ", point_user)
        else:
            print("égalité parfaite point ia = {}, point user = {}".format(point_ia, point_user))
    

    def _continue_game_func(self:object)->str:
        continue_game = ""
        while continue_game != "y" and continue_game != "n":
            continue_game = input("continuer ? (y/n)")
        return continue_game


    def _calculPoint(self:object, choice_user:str, choice_ia:str, point_user:int, point_ia:int)->list[int]:
        if self._is_winner(choice_user, choice_ia) == 1:
            print("gagner")
            point_user += 1
        elif self._is_winner(choice_user, choice_ia) == 2:
            print("égalité")
        else:
            print("perdu")
            point_ia += 1
        return [point_user, point_ia]


    def _calculIa(self:object, choice_user:str,nbre_coup_rock:int, nbre_coup_scissor:int, nbre_coup_paper:int, liste_coup:list)->list[list, int]:
        if choice_user == "rock":
            nbre_coup_rock += 1
            nbre_coup_scissor = 0
            nbre_coup_paper = 0
            liste_coup = [choice_user, nbre_coup_rock]
        elif choice_user == "paper":
            nbre_coup_paper += 1
            nbre_coup_scissor = 0
            nbre_coup_rock = 0
            liste_coup = [choice_user, nbre_coup_paper]
        else:
            nbre_coup_scissor += 1
            nbre_coup_rock = 0
            nbre_coup_paper = 0
            liste_coup = [choice_user, nbre_coup_scissor]
        return [liste_coup, nbre_coup_rock, nbre_coup_scissor, nbre_coup_paper]


    def start_game(self:object):
        continue_game = "o"
        liste_choix = ["rock", "paper", "scissor"]
        point_ia = 0
        point_user = 0
        liste_coup = [0,0]
        nbre_coup_rock = 0
        nbre_coup_scissor = 0
        nbre_coup_paper = 0
        while continue_game != "n":
            player_1 = Player(self.name_user, liste_choix).choice_user_possi()
            with open("dataUser.txt", "a") as file_data:
                file_data.write(" " + player_1)
            result = self._calculIa(player_1, nbre_coup_rock, nbre_coup_scissor, nbre_coup_paper, liste_coup)
            liste_coup = result[0]
            nbre_coup_rock = result[1]
            nbre_coup_scissor = result[2]
            nbre_coup_paper = result[3]
            player_ia = Ia(liste_choix, liste_coup).Ia_choice()
            print("choix ia = {}".format(player_ia))
            print("choix user = {}".format(player_1))
            point_all = self._calculPoint(player_1, player_ia,point_user,point_ia)
            point_user = point_all[0]
            point_ia = point_all[1]
            continue_game = self._continue_game_func()
        self._nbrePoint(point_user, point_ia)


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
        print(self.liste_coup)
        if self.liste_coup[1] >= 2:
            if self.liste_coup[0] == "paper":
                choix_ia = "scissor"
            elif self.liste_coup[0] == "rock":
                choix_ia = "paper"
            else:
                choix_ia = "rock" 
        else:
            coup_jouer = []
            with open("dataUser.txt", "r") as file_data_open:
                for row in file_data_open:
                    coup_jouer.append(row)
            coup_jouer = "".join(coup_jouer).split()
            if len(coup_jouer) != 0:
                if max(coup_jouer, key=coup_jouer.count) == "rock":
                    choix_ia = "paper"
                elif max(coup_jouer, key=coup_jouer.count) == "paper":
                    choix_ia = "scissor"
                else:
                    choix_ia = "rock"
            else:
                choix_ia = "paper"
        
        return choix_ia





name_user = input("entrez votre nom: ")
start_game = MyGame(name_user)
start_game.start_game()

