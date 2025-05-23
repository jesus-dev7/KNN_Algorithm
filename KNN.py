import matplotlib.pyplot as plt
from math import sqrt
import csv
import numpy as np
from scipy.interpolate import griddata

def afficher_graph():
    global X, Y, Z, x, y, z
    global Axe
    Axe = plt.axes(projection = "3d")
    plt.xlabel('Vitesse')
    plt.ylabel('Defense')
    Axe.set_zlabel("Attaque")
    N, H = np.meshgrid(np.linspace(min(X), max(X), int(len(X)/10)), np.linspace(min(Y), max(Y), int(len(Y)/10)))
    Z_3D = griddata((X, Y), Z, (N, H), method = "linear")
    Z_3D = np.nan_to_num(Z_3D, nan=np.nanmean(Z_3D))
    Vals = (N*5 + H*5 + Z_3D * 10)
    Norm = plt.Normalize(Vals.min(), Vals.max())
    Couleurs = plt.cm.inferno_r(Norm(Vals))
    Axe.plot_surface(N, H, Z_3D, facecolors = Couleurs, rstride = 1, cstride = 1, edgecolor = None, shade = False, alpha = 0.5)
    x = int(input("Entrer X:"))
    y = int(input("Entrer Y:"))
    z = int(input("Entrer Z:"))
    X.append(x)
    Y.append(y)
    Z.append(z)
    Axe.scatter(x, y, z, c = "black", s = 100)
    plt.show()

def calcul_distance():
    """
    """
    global K
    K = int(input("Echantillon(Distance):"))
    Axe__ = plt.axes(projection = "3d")
    plt.xlabel('Vitesse')
    plt.ylabel('Defense')
    Axe.set_zlabel("Attaque")
    N, H = np.meshgrid(np.linspace(min(X), max(X), int(len(X)/10)), np.linspace(min(Y), max(Y), int(len(Y)/10)))
    Z_3D = griddata((X, Y), Z, (N, H), method = "linear")
    Z_3D = np.nan_to_num(Z_3D, nan=np.nanmean(Z_3D))
    Vals = (N*5 + H*5 + Z_3D * 10)
    Norm = plt.Normalize(Vals.min(), Vals.max())
    Couleurs = plt.cm.inferno_r(Norm(Vals))
    Axe__.plot_surface(N, H, Z_3D, facecolors = Couleurs, rstride = 1, cstride = 1, edgecolor = None, shade = False, alpha = 0.5)
    for P, M, I in zip(X, Y, Z):
        Distance = sqrt((P - x)**2 + (M - y)**2 + (I - z)**2)
        Distance = round(Distance, 1)
        if Distance <= K:
            Newlist1 = [x, P]
            Newlist2 = [y, M]
            Newlist3 = [z, I]
            Axe__.plot(Newlist1, Newlist2, Newlist3, linestyle='--', label = f"{Distance}")
            plt.legend(loc="upper left")
            plt.xlabel('Vitesse')
            plt.ylabel('Defense')
            Axe__.set_zlabel("Attaque")
            Axe__.scatter(Newlist1, Newlist2, Newlist3, c = "blue", s = 100)
    plt.show()
    def K_Voisins():
        Ptns = []
        k = int(input("k plus proches voisins:"))
        for p, m, i in zip(X, Y, Z):
            distance = sqrt((p - x)**2 + (m - y)**2 + (i - z)**2)
            distance = round(distance, 1)
            Ptns.append([p, m, i, distance])
        for _ in range(len(Ptns) - k):
            Ptns.remove(max(Ptns, key = lambda d: d[3]))
        print(Ptns)
        X__ = []
        Y__ = []
        Z__ = []
        for Elem__ in Ptns:
            X__.append(Elem__[0])
            Y__.append(Elem__[1])
            Z__.append(Elem__[2])
        print(X__, Y__, Z__)
        Axe__ = plt.axes(projection = "3d")
        plt.xlabel('Vitesse')
        plt.ylabel('Defense')
        Axe.set_zlabel("Attaque")
        """N, H = np.meshgrid(np.linspace(min(X), max(X), int(len(X)/10)), np.linspace(min(Y), max(Y), int(len(Y)/10)))
        Z_3D = griddata((X, Y), Z, (N, H), method = "linear")
        Z_3D = np.nan_to_num(Z_3D, nan=np.nanmean(Z_3D))
        Vals = (N*5 + H*5 + Z_3D * 10)
        Norm = plt.Normalize(Vals.min(), Vals.max())
        Couleurs = plt.cm.inferno_r(Norm(Vals))
        Axe__.plot_surface(N, H, Z_3D, facecolors = Couleurs, rstride = 1, cstride = 1, edgecolor = None, shade = False, alpha = 0.10)"""
        for Coo1, Coo2, Coo3 in zip(X__, Y__, Z__):
            Type___ = "Error"
            for Elem in BigList:
                print(Elem)
                if int(Elem.get("SPD")) == Coo1:
                    if int(Elem.get("DEF")) == Coo2:
                        if int(Elem.get("ATK")) == Coo3:
                            Type___ = Elem["TYPE1"]
                            break
            Couleurs = {
                "Water": "blue",
                "Dragon": "darkgreen",
                "Normal": "white",
                "Poison": "purple",
                "Bug": "green",
                "Error": "black",
                "Fighting": "brown"
            }
            Vari = Couleurs.get(Type___, "gray")
            Newlist1_ = [x, Coo1]
            Newlist2_ = [y, Coo2]
            Newlist3_ = [z, Coo3]
            Axe__.plot(Newlist1_, Newlist2_, Newlist3_, linestyle='--')
            plt.xlabel('Vitesse')
            plt.ylabel('Defense')
            Axe__.set_zlabel("Attaque")
            Axe__.scatter(Newlist1_, Newlist2_, Newlist3_, c = Vari, s = 100)
        
    K_Voisins()
    def ChercherType():
        global BigList
        print(BigList)
        Types = {}
        for AnElem in BigList:
            try:
                NewX = int(AnElem["SPD"])
                NewY = int(AnElem["DEF"])
                NewZ = int(AnElem["ATK"])
                print(AnElem)
                NewDistance = sqrt((NewX - x)**2 + (NewY - y)**2 + (NewZ - z)**2)
                if NewDistance <= K:
                    tp = AnElem["TYPE1"]
                    match tp:
                        case _:
                            if tp not in Types:
                                Types[tp] = 1
                            else:
                                Types[tp] += 1
            except:
                pass
        print(Types)
        try:
            Type = max(Types, key = Types.get)
            print(Type)
        except:
            print("Error")
    ChercherType()
    plt.show()
       
def ClearCSV():
    global X, Y, Z
    X = []
    Y = []
    Z = []
    with open("pokemon.csv", "r+", encoding = "utf-8") as fichier:
        Dict = csv.DictReader(fichier)
        NewDict = {}
        global BigList
        BigList = []
        for Ligne in Dict:
            Droit = 1
            for Q, V in Ligne.items():
                if V != '' and Q != 'LEGENDARY' or type(V) != list and not (V.isdigit() and int(V) > 1000):
                    NewDict[Q] = V
            if Droit == 1:
                BigList.append(NewDict.copy())
            try:
                X.append(int(NewDict["SPD"]))
                Y.append(int(NewDict["DEF"]))
                Z.append(int(NewDict["ATK"]))
            except KeyError as e:
                print(e)
    Axes = plt.axes(projection = "3d")
    plt.xlabel('Vitesse')
    plt.ylabel('Defense')
    Axes.set_zlabel("Attaque")
    N, H = np.meshgrid(np.linspace(min(X), max(X), int(len(X)/10)), np.linspace(min(Y), max(Y), int(len(Y)/10)))
    Z_3D = griddata((X, Y), Z, (N, H), method = "linear")
    Z_3D = np.nan_to_num(Z_3D, nan=np.nanmean(Z_3D))
    Vals = (N*5 + H*5 + Z_3D * 10)
    Norm = plt.Normalize(Vals.min(), Vals.max())
    Couleurs = plt.cm.inferno(Norm(Vals))
    Axes.plot_surface(N, H, Z_3D, facecolors = Couleurs, rstride = 1, cstride = 1, edgecolor = None, shade = False)
    plt.show()

ClearCSV()
afficher_graph()
calcul_distance()