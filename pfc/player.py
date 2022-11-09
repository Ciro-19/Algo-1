import cv2


class Player:
    def __init__(self:object,name_user:str,liste_choice:list):
        self.liste_choice = liste_choice
        self.name_user = name_user
        if self.name_user == "dolorean":
            self._easter_egg()
            return
        self.liste_choice = liste_choice
        self.player_liste_coup = []
        self.liste_coup = []
        print("Player {}".format(name_user))
    def _Ia_choice(self:object, liste_coup:list, coup_user:str, player)->str:
        self.player_liste_coup = player.stock_coup(coup_user)
        if liste_coup[1] >= 2:
            if liste_coup[0] == "paper":
                choice_ia = "scissor"
            elif liste_coup[0] == "rock":
                choice_ia = "paper"
            else:
                choice_ia = "rock" 
        else:
            if len(self.player_liste_coup) != 0:
                if max(self.player_liste_coup, key=self.player_liste_coup.count) == "rock":
                    choice_ia = "paper"
                elif max(self.player_liste_coup, key=self.player_liste_coup.count) == "paper":
                    choice_ia = "scissor"
                else:
                    choice_ia = "rock"
            else:
                choice_ia = "paper"
        
        return choice_ia


    def _easter_egg(self):
        print("vite nous allons mourir!")
        int(input("Emmett Brown vous demande choisir une date ou voyager: "))
        cap = cv2.VideoCapture('x.mp4')
        
        if (cap.isOpened()== False): 
            print("Error opening video stream or file")
        
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                cv2.imshow('Frame',frame)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else: 
                break
        cap.release()
        
        cv2.destroyAllWindows()
        return 




    def choice_user_possi(self:object,liste_coup=[],choice_user=None,player=False)->str:
        if self.name_user != "ia":
            for i in range(len(self.liste_choice)):
                print("{} - {}".format(i, self.liste_choice[i]))
            choice_user = -1
            while choice_user < 0 or choice_user > 2:
                try:
                    choice_user = int(input("votre choix : "))
                except:
                    pass
            return self.liste_choice[choice_user]
        else:
            return self._Ia_choice(liste_coup, choice_user, player)

    def stock_coup(self, choice_user):
        self.liste_coup.append(choice_user)
        return self.liste_coup