"""
                    Importation des bibliothéques
        
"""

import matplotlib.pyplot as plt # bibliothéque pour afficher les figures
from scipy.stats import randint  # bibliothéque pour génerer une distribution discréte
import numpy as np # bibliothéque pour la création d'axe des x

"""
                    Déclarations des fonctions qu'on va utiliser 

"""

def gen_tabel(b,c,n): # Focntion qui va fénérer les valeurs xn 
    
    a=[] # intialisation d'un tableau vide dans lequelle on va stocker les xn
    x=randint.rvs(b,c,size=n) #génerer une distrubtion discréte uniforme
    for i in x: # boucle for qui va calculer les xn selon les contraintes de la fonction f
        if i<b: # premier condition si x<a
            a.append(0) # f(x) = 0
        elif i>= b and i<c: # si a =< x < b
            a.append(1+(i-b)/(c-b+1)) # f(x) = valuer a calculé
        elif i>=c: # si x >= b
            a.append(1) # f(x) = 1
        
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
a=5 # differents valeurs de a
b=50 # differents valeurs de b
Xn=[] # intialisation d'un tableau pour stocker les valeur de la moyenne calculer
teta=[] # intialisation d'un tableau pour stocker les valeur de la variance calculer

w=np.linspace(0,n, num=len(n)) # calcul d'axe des x

for i in n: # boucle for dans la quelle on va varier a et b et calculer la moyenne et la varinca respectivement
    t=gen_tabel(a,b,i) # génération d'une table avec n variable alétoire entre a et b d
    Xn.append(moy_emp(t)) # calcule de la moyenne empérique
    teta.append(var_emp(t,moy_emp(t))) # calcule de la variance empérique

print(Xn,"\n",teta) # affichage de la moyenne et la varince avec un retour à la ligne entre chaque valeur

"""
                    Affichage des Figuers

"""

plt.plot(n,teta,color="red",label="Variance empérique") # dessinier téta en focntion de n avec la couleur Rouge
plt.plot(n,Xn,color="green",label="Moyenne empérique") # dessinier Xn barre en fonction de n avec la couleur Vert
plt.xlabel("Nombre d'echantillon")
plt.ylabel("Variables aléatoires")
plt.title("Courbe de la moyenne empérique et la variance empérique")
plt.legend()
plt.grid() # grid la figure
plt.show() # affichier la figure