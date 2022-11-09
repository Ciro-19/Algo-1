from player import Player
from random import choice

class MyGame:
    def __init__(self):
        #tab jeux
        self.tabGrille = [[0,1,2],[3,4,5],[6,7,8]]
        #instance player
        self.player_1 = Player(1)
        self.player_2 = Player(2)
        self.name_user_1 = self.player_1.name_user()
        self.name_user_2 = self.player_2.name_user()
        #tab signe
        self.signe = ["X", "O"]
        #choix signe
        self.signe_user_1 = self.player_1.choice_signe(self.signe)
        self.signe_user_2 = self.signe[self.signe.index(self.signe_user_1) - 1]
        self.dictG = {self.signe_user_1:self.name_user_1, self.signe_user_2:self.name_user_2}
        print("j1 = ",self.signe_user_1)
        print("j2 = ",self.signe_user_2)
        #change
        self.change_player = 0
        self.cpt = 0


    def _grille(self):
        print(""" 
        |  {}  |  {}  |  {}  |
        -------------------
        |  {}  |  {}  |  {}  |
        -------------------
        |  {}  |  {}  |  {}  |
        """.format(self.tabGrille[0][0],self.tabGrille[0][1],self.tabGrille[0][2],self.tabGrille[1][0],self.tabGrille[1][1],self.tabGrille[1][2],self.tabGrille[2][0],self.tabGrille[2][1],self.tabGrille[2][2]))


    def _tour_play(self):
        change = self.change_player
        if self.change_player == 1:
            self.change_player -= 1
        else:
            self.change_player += 1
        return change


    def _choice_place(self):
        self._grille()
        while True:
            choix_emplacement_user = -1
            while choix_emplacement_user < 0 or choix_emplacement_user > len(self.tabGrille) - 1:
                choix_emplacement_user = int(input("ou mettre notre signe: "))
                for i in range(len(self.tabGrille)):
                    for j in range(len(self.tabGrille[i])):
                        if choix_emplacement_user == self.tabGrille[i][j] and type(self.tabGrille[i][j]) != str:
                            choix_emplacement_user = [i , j]
                            print("choice",choix_emplacement_user)
                            return choix_emplacement_user
                        else:
                            pass
            


    def _place_signe(self, joue):
        if self.name_user_2 != "ia":
            if joue == 0:
                if self.name_user_1 == "ia":
                    choice_ia = self._best_coup_ia()
                    print("choice" ,choice_ia)
                    choice_ia_x = choice_ia[0]
                    choice_ia_y = choice_ia[1]
                    self.tabGrille[choice_ia_x][choice_ia_y] = self.signe_user_1
                else:
                    print("joueur {} joue".format(self.name_user_1))
                    choice_emplacement = self._choice_place()
                    print("x",choice_emplacement)
                    choice_emplacement_x = choice_emplacement[0]
                    choice_emplacement_y = choice_emplacement[1]
                    self.tabGrille[choice_emplacement_x][choice_emplacement_y]= self.signe_user_1
            else:
                if self.name_user_2 == "ia":
                    choice_ia = self._best_coup_ia()
                    print("choice" ,choice_ia)
                    choice_ia_x = choice_ia[0]
                    choice_ia_y = choice_ia[1]
                    self.tabGrille[choice_ia_x][choice_ia_y] = self.signe_user_2
                else:
                    print("joueur {} joue".format(self.name_user_2))
                    choice_emplacement = self._choice_place()
                    choice_emplacement_x = choice_emplacement[0]
                    choice_emplacement_y = choice_emplacement[1]
                    self.tabGrille[choice_emplacement_x][choice_emplacement_y] = self.signe_user_2
        else:
            if joue == 1:
                if self.name_user_1 == "ia":
                    choice_ia = self._best_coup_ia()
                    print("choice" ,choice_ia)
                    choice_ia_x = choice_ia[0]
                    choice_ia_y = choice_ia[1]
                    self.tabGrille[choice_ia_x][choice_ia_y] = self.signe_user_1
                else:
                    print("joueur {} joue".format(self.name_user_1))
                    choice_emplacement = self._choice_place()
                    print("x",choice_emplacement)
                    choice_emplacement_x = choice_emplacement[0]
                    choice_emplacement_y = choice_emplacement[1]
                    self.tabGrille[choice_emplacement_x][choice_emplacement_y]= self.signe_user_1
            else:
                if self.name_user_2 == "ia":
                    choice_ia = self._best_coup_ia()
                    print("choice" ,choice_ia)
                    choice_ia_x = choice_ia[0]
                    choice_ia_y = choice_ia[1]
                    self.tabGrille[choice_ia_x][choice_ia_y] = self.signe_user_2
                else:
                    print("joueur {} joue".format(self.name_user_2))
                    choice_emplacement = self._choice_place()
                    choice_emplacement_x = choice_emplacement[0]
                    choice_emplacement_y = choice_emplacement[1]
                    self.tabGrille[choice_emplacement_x][choice_emplacement_y] = self.signe_user_2


    def _horizontal_check(self):
        for i in range(len(self.tabGrille)):
            for j in range(len(self.tabGrille[i])):
                if len(set(self.tabGrille[i])) == 1:
                    return [True, self.tabGrille[i][j]]
        return [False, False]


    def _ligne_check(self):
        f = []
        cpt = 0
        for i in range(3):
            for i in range(len(self.tabGrille)):
                for j in range(len(self.tabGrille[i])):
                    f.append(self.tabGrille[i][cpt])
            if len(set(f)) == 1:
                return [True, f[0]]
            cpt += 1
            f = []
        return [False, False]


    def _diagonale_check(self,right=False):
        if not right:
            f = []
            cpt = 0
            for i in range(len(self.tabGrille)):
                f.append(self.tabGrille[i][cpt])
                cpt += 1
            if len(set(f)) == 1:
                return [True, f[0]]
            return [False, False]
        else:
            f = []
            cpt = 2
            for i in range(len(self.tabGrille)):
                f.append(self.tabGrille[i][cpt])
                cpt -= 1
            if len(set(f)) == 1:
                return [True, f[0]]
            return [False, False]


    def _is_winner(self):
        egalite = False
        checkH0 = self._horizontal_check()
        if checkH0[0]:
            return checkH0
        checkH1 = self._horizontal_check()
        if checkH1[0]:
            return checkH1
        checkH2 = self._horizontal_check()
        if checkH2[0]:
           return checkH2
        checkL0 = self._ligne_check()
        if checkL0[0]:
            return checkL0
        checkL1 = self._ligne_check()
        if checkL1[0]:
            return checkL1
        checkL2 = self._ligne_check()
        if checkL2[0]:
            return checkL2
        checkD0 = self._diagonale_check()
        if checkD0[0]:
            return checkD0
        checkD1 = self._diagonale_check(True)
        if checkD1[0]:
            return checkD1
        for i in range(len(self.tabGrille)):
            for j in range(len(self.tabGrille[i])):
                if type(self.tabGrille[i][j]) != str:
                    egalite = True
                    if egalite:
                        return False, False
        return "égalité", "égalité"
 

    #ia
    def _best_coup_ia(self):
        best_score = -100
        best_coup = ""
        for i in range(len(self.tabGrille)):
            for j in range(len(self.tabGrille[i])):
                if type(self.tabGrille[i][j]) != str:
                    save = self.tabGrille[i][j]
                    if self.name_user_1 == "ia":
                        self.tabGrille[i][j] = self.signe_user_1
                    else:
                        self.tabGrille[i][j] = self.signe_user_2
                    score = self._minimax(False)
                    self.tabGrille[i][j] = save
                    if score > best_score:
                        best_score = score
                        best_coup = (i,j)
        return best_coup

    """def _min_max(self) :
        max = self._max()

    def _min(self) :
        # Simule l'adverse
        max = self._max()
        "if quelqu'un gagne ou plateau plein" return()

    def _max(self) :
        # Simule mes coups
        min = self._min()
        "if quelqu'un gagne ou plateau plein" return()
    """
    def _minimax(self, maximizingPlayer):
        winner = self._is_winner()
        if self.name_user_1 == "ia":
            if winner[1] == self.signe_user_1:
                return 10
            elif winner[1] == self.signe_user_2:
                return -10
            elif winner[1] == "égalité":
                return 0
        else:
            if winner[1] == self.signe_user_2:
                return 10
            elif winner[1] == self.signe_user_1:
                return -10
            elif winner[1] == "égalité":
                return 0
        if maximizingPlayer:
            best_score = -100
            for i in range(len(self.tabGrille)):
                for j in range(len(self.tabGrille[i])):
                    if type(self.tabGrille[i][j]) != str:
                        save = self.tabGrille[i][j]
                        if self.name_user_1 == "ia":
                            self.tabGrille[i][j] = self.signe_user_1
                        else:
                            self.tabGrille[i][j] = self.signe_user_2
                        score = self._minimax(False)
                        self.tabGrille[i][j] = save
                        if score > best_score:
                            best_score = score
            return best_score
        else:
            best_score = 100
            for i in range(len(self.tabGrille)):
                for j in range(len(self.tabGrille[i])):
                    if type(self.tabGrille[i][j]) != str:
                        save = self.tabGrille[i][j]
                        if self.name_user_1 == "ia":
                            self.tabGrille[i][j] = self.signe_user_1
                        else:
                            self.tabGrille[i][j] = self.signe_user_2
                        score = self._minimax(True)
                        self.tabGrille[i][j] = save
                        if score < best_score:
                            best_score = score
            return best_score

    #ia

    def start_game(self):
        cpt = 0
        while cpt != (len(self.tabGrille) * 3):
            joue = self._tour_play()
            self._place_signe(joue)
            self._grille()
            winner = self._is_winner()
            print(self.tabGrille)
            if winner[0]:
                print("{} a gagner".format(self.dictG[winner[1]]))
                break
            cpt += 1
