"""
                    Importation des bibliothéques
        
"""

import random # bibliothéque pour générer une distrubition unifore continue
import matplotlib.pyplot as plt # bibliothéque pour afficher les figures

"""
                    Déclarations des fonctions qu'on va utiliser 

"""

def gen_tabel(n): # fonction qui va générer les valeurs xn
    
    a=[] # initialisation d'un tableau vide
    for i in range(n+1) : # parcours de 0 vers n+1 echantillon
        a.append(random.uniform(0,1)) # calcule des xn avec dans un intervale uniforme entre [0,1]
    return a # retourner le tableau qui contient les xn
              
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

plt.plot(n,teta,color="red",label="Moyenne empérique") # dessinier téta en focntion de n avec la couleur Rouge
plt.plot(n,Xn,color="green",label="Variance empérique") # dessinier Xn barre en fonction de n avec la couleur Vert
plt.xlabel("Nombre d'echantillon")
plt.ylabel("Variables aléatoires")
plt.title("Courbe de la moyenne empérique et la variance empérique")
plt.legend()
plt.grid() # grid la figure
plt.show() # affichier la figure


