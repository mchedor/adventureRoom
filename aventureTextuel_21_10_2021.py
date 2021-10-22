import json

class Salle:
    def __init__(self):
        #initialisation des json
        #initialisation des map(maison,monde,magasin)
        self.x=0
        self.y=2
        with open('map.json') as f:
            self.map = json.load(f)
        with open('salle.json') as f:
            self.salle = json.load(f)
    def get_salle(self, x,y):
        #retourne l'ID de la salle de coordoné x,y
        try:
            return self.map[y][x]
        except:
            return 0
    def action(self, entrer):
        #menu de la salle
        #les fleches pour changer de salle
        #[0] pour rechercher
        #[1:9] pour interagir
        if entrer=="z":
                self.y+=-1
                return "y",-1
        elif entrer=="s":
                self.y+=1
                return "y",1
        elif entrer=="q":
                self.x+=-1
                return "x",-1
        elif entrer=="d":
                self.x+=1
                return "x",1
        elif entrer=="e":
            exit()
        
    def annonce(self):
        act=input("action :  ")
        pos,signe=self.action(act)
        if self.get_salle(self.x,self.y)==0:
            if pos=="y":
                self.y-=signe
            elif pos=="x":
                self.y-=signe
        print(self.salle["salle"][self.map[self.y][self.x]]["name"])

if __name__=="__main__":
    s=Salle()
    print(s.map)
    while True:
        s.annonce()

