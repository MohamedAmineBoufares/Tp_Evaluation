"""
                    Importation des bibliothéques
        
"""

import matplotlib.pyplot as plt # bibliothéque pour afficher les figures
import random  # bibliothéque pour génerer une distribution discréte entre [0,1]
import numpy as np # bibliothéque pour la création d'axe des x

"""
                    Déclarations des fonctions qu'on va utiliser 

"""

def gen_tabel(n): # Focntion qui va fénérer les valeurs xn 
    x=[]
    a=[] # intialisation d'un tableau vide dans lequelle on va stocker les xn
    for i in range(n):
        x.append(random.uniform(0,1)) #génerer une distrubtion discréte uniforme entre [0,1] avec n echantillon
    for i in x: # boucle for qui va calculer les xn selon les contraintes de la fonction f
        if i<0.3: # premier condition si x<0.3
            a.append(0) # f(x) = 0
        elif i>= 0.3 and i<0.5: # si 0.3 =< x < 0.5
            a.append(2) # f(x) = 2
        elif i>=0.5: # si x >= 0.5
            a.append(6) # f(x) = 6
        
    return a # retourner le resultat finale de a aprés calcule des xn
              
def moy_emp(a) : # fonction qui calcule la moyenne empérique
    
    n=len(a) # determiner n le nombre totale des xn dans a
    return (1/n)*(sum(a)) # calcule de Xn barre et retourner la valeur de Xn barre finale

def var_emp(a,xn_): # fonction qui calcule la variance empérique
    var=0
    n=len(a) # determiner le nombre des xn dans a
    for i in a:
        var=(i-xn_)**2 # formule qui calcule la variance avec xn_ est la moyenne empérique
    return var/n # suite de la formule de la variance

"""
                    paramétres de la distrubition

"""

n=[10,100,1000,10000] # differents valeurs de n: nombre des échantillons
teta=[] # intialisation du tableau qui va stocker les valeurs de la variance
Xn=[] # intialisation du tableau qui va stocker les valeurs de la moyenne

for i in n: # boucle qui va parcourir les differents valeurs de n
    t=gen_tabel(i) # génération d'un tableau t qui va stocker les xn
    Xn.append(moy_emp(t)) # calcule des différents valeurs Xn barre est les stocker dans Xn[]
    teta.append(var_emp(t,moy_emp(t))) # calcule des différentes valeurs de la variance est les stocker dans téta[]
print(Xn,"\n",teta) # affichage de Xn barre et téta

"""
                    Affichage des Figuers

"""

plt.plot(n,teta,color="red",label="Moyenne empérique") # dessinier téta en focntion de n avec la couleur Rouge
plt.plot(n,Xn,color="green",label="Variance empérique") # dessinier Xn barre en fonction de n avec la couleur Vert
plt.xlabel("Nombre d'echantillon")
plt.ylabel("Variables aléatoires")
plt.title("Courbe de la moyenne empérique et la variance empérique")
plt.legend()
plt.grid() # grid la figure
plt.show() # affichier la figure