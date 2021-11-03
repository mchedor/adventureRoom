import json
import pygame


class Salle:
    def __init__(self):
        #initialisation des json
        #initialisation des map(maison,monde,magasin)
        
        self.x=0
        self.y=3

        self.lieu_name="maisonR"
        with open('map.json') as f:
            self.map = json.load(f)
        with open('salle.json') as f:
            self.salle_dict = json.load(f)
        with open('element2jeu.json') as f:    
            self.element2jeu = json.load(f)
        self.inventaire=[]
    def get_map(self, x,y, name_lieu_get_map, name_map_get_map):
        #retourne l'ID de coordoné x,y
        try:
            return self.map[name_lieu_get_map][name_map_get_map][y][x]
        except:
            return 0

    def get_salle(self, x,y, name_lieu_get_salle):
        #retourne l'ID de la salle de coordoné x,y
        try:
            return self.map[name_lieu_get_salle]["salle"][y][x]
        except:
            return 0
    
    def get_mur(self, x,y, name_lieu_get_mur):
        #retourne les portes qui touchent la salle
        #dans l'ordre: [z,s,q,d] ou [haut, bas, gauche, droite]
        rep_get_mur={}
        try:
            rep_get_mur["h"]=self.map[name_lieu_get_mur]["mur"][((y-1)*2)+1][x]
            rep_get_mur["b"]=self.map[name_lieu_get_mur]["mur"][(y*2)+1][x]
            rep_get_mur["g"]=self.map[name_lieu_get_mur]["mur"][y*2][x]
            rep_get_mur["d"]=self.map[name_lieu_get_mur]["mur"][y*2][x+1]
            erreur_action=None
            #on cherche toute les direction
            for i in rep_get_mur:
                #pour chaque direction on stoke le contenu (mur,porte,objet) dans "contenui"
                contenui=rep_get_mur[i]
                #on stoke la condition pour avancer (none=>on ne peut pas, false=> dans toute condition,"objet"=>on peut si on a l'objet)
                condition_get_mur=self.element2jeu["deplacement"][contenui]["condition"]
                
                if condition_get_mur==False:
                    rep_get_mur[i]=True
                elif condition_get_mur in self.inventaire:
                    rep_get_mur[i]=True
                elif condition_get_mur:
                    rep_get_mur[i]=False
                    #on explique la raison du refu du deplacent
                    erreur_action=self.element2jeu["deplacement"][contenui]["erreur"]
                else:
                    rep_get_mur[i]=False 
            if erreur_action:
                rep_get_mur["erreur"]=erreur_action
        except ValueError as a:
            rep_get_mur["erreur"]=a#"erreur exept in Salle.get_mur()"
        
        return rep_get_mur
        
    def action(self, entrer):
        #menu de la salle
        #les fleches pour changer de salle
        #[0] pour rechercher
        #[1:9] pour interagir
        mur=self.get_mur(self.x,self.y,self.lieu_name)
        print("mur : ", mur)
        print("inv : ",self.inventaire)
        if entrer=="z" and mur["h"]==True:
                self.y+=-1
        elif entrer=="s" and mur["b"]==True:
                self.y+=1
        elif entrer=="q" and mur["g"]==True:
                self.x+=-1
        elif entrer=="d" and mur["d"]==True:
                self.x+=1
        elif entrer=="e":
            exit()
        else:
            #on affiche la raison de l'impossibiliter du déplacement
            print(mur["erreur"])
            return 0
        
        #ON VERRIFIE SI LA SALLE EST JOIN
        #salle_action contient l'ID de la salle 
        salle_action = self.map[self.lieu_name]["salle"][self.y][self.x]
        #lieu_name_action est une variable de passage contenant le nom du premier lieu.
        lieu_name_action=self.lieu_name
        #si la salle avec cette ID est "join" (mene vers un autre lieu)
        if self.salle_dict[self.lieu_name][salle_action]["join"]:
            #on change le lieu par le lieu stoké dans le "join"
            self.lieu_name=self.salle_dict[self.lieu_name][salle_action]["join"]["lieu"] 
            # on modifie x et y à partir de la salle d'arriver contenut dans "join" et on récupere dans cette salle la la "pos"
            self.x=self.salle_dict[self.lieu_name][self.salle_dict[lieu_name_action][salle_action]["join"]["salle"]]["pos"]["x"]
            self.y=self.salle_dict[self.lieu_name][self.salle_dict[lieu_name_action][salle_action]["join"]["salle"]]["pos"]["y"]   
        
        #ON VERRIFIE SI LA SALLE CONTIENT UN OBJET
        #salle_action contient l'ID de la salle 
        salle_action = self.map[self.lieu_name]["salle"][self.y][self.x]
        #salle_action contient la salle 
        salle_action = self.salle_dict[self.lieu_name][salle_action]
        if "object" in salle_action:
            if self.element2jeu["object"][salle_action["object"]]["name"] not in self.inventaire:
                self.inventaire.append(self.element2jeu["object"][salle_action["object"]]["name"])
            

    def annonce(self):
        print(self.salle_dict[self.lieu_name][self.map[self.lieu_name]["salle"][self.y][self.x]]["name"])

debug=None
if __name__=="__main__":
    s=Salle()
    print(s.map)
    while True:
        act=input("action :  ")
        s.action(act)
        s.annonce()
        y=s.y
        if debug:
            print("x :",s.x,"\ny : ", y)
            print("mur y :\n h :",((y-1)*2)+1)
            print("s :",(y*2)+1)
            print("g :",y*2)
            print("d :",y*2)


