from player import Player

class MyGame:
    def __init__(self:object):
        self.name_user = input("entrez votre nom: ")
        self.choice_ia_or_player = input("tapez ia pour jouer avec ia sinon rentrez le pseudo du deuxieme Player: ")
        self.liste_choice = ["rock", "paper", "scissor"]
        self.player_1 = Player(self.name_user, self.liste_choice)
        self.player_2 = Player(self.choice_ia_or_player, self.liste_choice)
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
            choice = self.winner[(choice_user, choice_ia)]
            if choice_ia == choice:
                return 0
            return choice
        except:
            return 1

    
    def _nbre_point(self:object, point_user:int, point_ia:int):
        if point_user < point_ia:
            print(self.choice_ia_or_player," winner avec une avance de ", point_ia - point_user, "et un score de = ", point_ia)
        elif point_user > point_ia:
            print(self.name_user," winner avec une avance de ", point_user - point_ia, "et un score de = ", point_user)
        else:
            print("equality parfaite point {} = {}, point {} = {}".format(self.choice_ia_or_player,point_ia, self.name_user ,point_user))
    

    def _calcul_point(self:object, choice_user:str, choice_ia:str, point_user:int, point_ia:int)->list[int]:
        if self._is_winner(choice_user, choice_ia) == 1:
            print("{} winner".format(self.name_user))
            point_user += 1
        elif self._is_winner(choice_user, choice_ia) == 2:
            print("equal")
        else:
            print("{} winner".format(self.choice_ia_or_player))
            point_ia += 1
        return [point_user, point_ia]


    def _calcul_ia(self:object, choice_user:str,nbre_coup_rock:int, nbre_coup_scissor:int, nbre_coup_paper:int, liste_coup:list)->list[list, int]:
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
        continue_game = 0
        point_ia = 0
        point_user = 0
        liste_coup = [0,0]
        nbre_coup_rock = 0
        nbre_coup_scissor = 0
        nbre_coup_paper = 0
        while continue_game != 3 and self.name_user != "dolorean" and self.choice_ia_or_player != "dolorean":
            if self.name_user != "ia":
                player_1_coup = self.player_1.choice_user_possi(self.choice_ia_or_player)
                result = self._calcul_ia(player_1_coup, nbre_coup_rock, nbre_coup_scissor, nbre_coup_paper, liste_coup)
                liste_coup = result[0]
                nbre_coup_rock = result[1]
                nbre_coup_scissor = result[2]
                nbre_coup_paper = result[3]
                player_ia = self.player_2.choice_user_possi(liste_coup,player_1_coup,self.player_1)
                print("{} = {}".format(self.choice_ia_or_player,player_ia))
                print("{} = {}".format(self.name_user, player_1_coup))
            else:
                player_1_coup = self.player_2.choice_user_possi(self.name_user)
                result = self._calcul_ia(player_1_coup, nbre_coup_rock, nbre_coup_scissor, nbre_coup_paper, liste_coup)
                liste_coup = result[0]
                nbre_coup_rock = result[1]
                nbre_coup_scissor = result[2]
                nbre_coup_paper = result[3]
                player_ia = self.player_1.choice_user_possi(liste_coup,player_1_coup,self.player_2)
                print("{} = {}".format(self.name_user,player_ia))
                print("{} = {}".format(self.choice_ia_or_player, player_1_coup))
            point_all = self._calcul_point(player_1_coup, player_ia,point_user,point_ia)
            point_user = point_all[0]
            point_ia = point_all[1]
            continue_game += 1
        self._nbre_point(point_user, point_ia)

