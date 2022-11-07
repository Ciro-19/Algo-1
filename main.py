"""
sam
lucas
idriss
"""
class MyGame:
    def __init__(self:object):
        self.name_user = input("entrez votre nom: ")
        self.choice_ia_or_player = input("tapez ia pour jouer avec ia sinon rentrez le pseudo du deuxieme Player: ")
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

    
    def _nbrePoint(self:object, point_user:int, point_ia:int):
        if point_user < point_ia:
            print(self.choice_ia_or_player," winner avec une avance de ", point_ia - point_user, "et un score de = ", point_ia)
        elif point_user > point_ia:
            print(self.name_user," winner avec une avance de ", point_user - point_ia, "et un score de = ", point_user)
        else:
            print("equality parfaite point {} = {}, point {} = {}".format(self.choice_ia_or_player,point_ia, self.name_user ,point_user))
    

<<<<<<< HEAD
    def _calcul_point(self:object, choice_user:str, choice_ia:str, point_user:int, point_ia:int)->list[int]:
=======
    def _continue_game_func(self:object)->str:
        continue_game = ""
        while continue_game != "y" and continue_game != "n":
            continue_game = input("continuer ? (y/n)")
        return continue_game


    def _calculPoint(self:object, choice_user:str, choice_ia:str, point_user:int, point_ia:int)->list[int]:
>>>>>>> 4ced7ba035fe3f923d31f06c1f8b50f72b240665
        if self._is_winner(choice_user, choice_ia) == 1:
            print("{} winner".format(self.name_user))
            point_user += 1
        elif self._is_winner(choice_user, choice_ia) == 2:
            print("equal")
        else:
            print("{} winner".format(self.choice_ia_or_player))
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
        continue_game = 0
        liste_choice = ["rock", "paper", "scissor"]
        point_ia = 0
        point_user = 0
        liste_coup = [0,0]
        nbre_coup_rock = 0
        nbre_coup_scissor = 0
        nbre_coup_paper = 0
        while continue_game != 3:
            player_1 = Player(self.name_user, liste_choice).choice_user_possi()
            if self.choice_ia_or_player == "ia":
                with open("cerveauIa.txt", "a") as file_data:
                    file_data.write(" " + player_1)
                result = self._calculIa(player_1, nbre_coup_rock, nbre_coup_scissor, nbre_coup_paper, liste_coup)
                liste_coup = result[0]
                nbre_coup_rock = result[1]
                nbre_coup_scissor = result[2]
                nbre_coup_paper = result[3]
                player_ia = Ia(liste_choice, liste_coup).Ia_choice()
            else:
                player_ia = Player(self.choice_ia_or_player, liste_choice).choice_user_possi()
            print("{} = {}".format(self.choice_ia_or_player,player_ia))
            print("{} = {}".format(self.name_user, player_1))
            point_all = self._calculPoint(player_1, player_ia,point_user,point_ia)
            point_user = point_all[0]
            point_ia = point_all[1]
<<<<<<< HEAD
            continue_game += 1
        self._nbre_point(point_user, point_ia)
=======
            continue_game = self._continue_game_func()
        self._nbrePoint(point_user, point_ia)
>>>>>>> 4ced7ba035fe3f923d31f06c1f8b50f72b240665


class Ia:
    def __init__(self:object, liste_choice:list, liste_coup:list):
        self.liste_choice = liste_choice
        self.liste_coup = liste_coup


    def Ia_choice(self:object)->str:
        print(self.liste_coup)
        if self.liste_coup[1] >= 2:
            if self.liste_coup[0] == "paper":
                choice_ia = "scissor"
            elif self.liste_coup[0] == "rock":
                choice_ia = "paper"
            else:
                choice_ia = "rock" 
        else:
            coup_play = []
            with open("cerveauIa.txt", "r") as file_data_open:
                for row in file_data_open:
                    coup_play.append(row)
            coup_play = "".join(coup_play).split()
            if len(coup_play) != 0:
                if max(coup_play, key=coup_play.count) == "rock":
                    choice_ia = "paper"
                elif max(coup_play, key=coup_play.count) == "paper":
                    choice_ia = "scissor"
                else:
                    choice_ia = "rock"
            else:
                choice_ia = "paper"
        
        return choice_ia



class Player:
    def __init__(self:object,name_user:str,liste_choice:list):
        self.liste_choice = liste_choice
        print("Player {}".format(name_user))


    def choice_user_possi(self:object)->str:
        for i in range(len(self.liste_choice)):
            print("{} - {}".format(i, self.liste_choice[i]))
        choice_user = -1
        while choice_user < 0 or choice_user > 2:
            try:
                choice_user = int(input("votre choix : "))
            except:
                pass
        return self.liste_choice[choice_user]

start_game = MyGame()
start_game.start_game()

