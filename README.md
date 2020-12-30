# Projet_Analyse_Num
# Introduction général:

Ce projet permet d'étuder une fonction f(x) et de la  représenter graphiquement  aussi de calculer et de représenter les méthodes d'intégration numériques .

Tout d'abord ,on peut  définir une fonction mathématique (polynome, trigonométrique..) avec son intervalle ,on donnant comme résultat son primitivé et sa représentation , dérivéet sa représentation et/ou aussi n ordre de dérivé en spécifiant n et sa représentation . En plus , on peut représenté ,avec la fonction donné au début ,plusierus méthodes de l'analyse numérique comme (méthode de rectangle , méthode des trapézes , méthode des points milieux , méthodes de simspon)en donnant pour chaque fonction sa valeur approché ,valeur exacte et l'erreur.

# Etude d'une fonction :

## 1.But

une étude de fonction est la détermination de certaines propriétés d'une fonction numérique pour en tracer une représentation graphique à partir d'une expression analytique ou d'une équation fonctionnelle, ou encore pour en déduire le nombre et la disposition d'antécédents pour diverses valeurs numériques.


## 2.Etude de fonction:

Pour étudier une fonction f(x), il faut passer d'abord par la détermination du domaine de définition et vise essentiellement la description des variations, voire des lignes de niveau dans le cas de fonctions de plusieurs variables.

## 3.Etude graphique:

Lorsqu'une fonction est donnée par une représentation de courbe, la lecture graphique permet de lire son domaine de définition, à savoir l'ensemble des points de l'axe des abscisses pour lesquels la courbe associe une ordonnée.

Les intersections de la courbe avec l'axe des abscisses indiquent les points d'annulation de la fonction,si la fonction est continue,déterminer sa signe(si la courbe est au-dessus de l'axe des abscisses, la fonction est positive sur cet intervalle et si la courbe est en dessous de l'axe des abscisses, la fonction est négative sur cet intervalle)

La lecture graphique permet aussi de repérer les intervalles en abscisse sur lesquels la fonction est monotone, c'est-à-dire soit croissante, soit décroissante.

## 4.Etude de primitive :

une primitive d’une fonction  f est une fonction F dont f est la dérivée : F'=f. Il s’agit donc d’un antécédent pour l’opération de dérivation.

La détermination d’une primitive sert d’abord au calcul des intégrales de fonctions continues sur un segment, en application du théorème fondamental de l'analyse.:
![](https://latex.codecogs.com/gif.latex?f%28x%29%20dx%20%3D%20F%28b%29-F%28a%29)
photo de dérivé
 
 ## 5.Etude de dérivé:
 La dérivée d'une fonction f est une fonction qui, à tout nombre pour lequel f admet un nombre dérivé, associe ce nombre dérivé. La dérivée en un point d'une fonction de plusieurs variables réelles, ou à valeurs vectorielles, est plus couramment appelée différentielle de la fonction en ce point, et n'est pas traitée ici. La dérivée d'une fonction f en x est usuellement notée f'(x) ou df/dx(x)}.
 
 ### 5.a.Ordre de dérivé:
Soit f une fonction dérivable sur un intervalle I ,  Si f' est dérivable sur I sa fonction dérivée f''  (ou  est appelée dérivée seconde de f.
On peut continuer le processus de dérivation et définir une relation de récurrence pour calculer la fonction dérivée  à l'ordre f**(n) à l'ordre n.
La fonction f est de classe C**(n) sur l'intervalle I si f**(n) existe sur I en étant continue sur I.

# Méthodes d'intégration numérique: 

## 1.But

Le but  est d’aborder le calcul général de l’intégrale d’une fonction f(x) sur un domaine fini délimité par des bornes finies a et b.


## 2.Méthode de Réctangle:

Cette méthode, très élémentaire, basée sur les sommes de Cauchy-Riemann (approchant l'aire sous une courbe) et appliquée à une fonction f continue, permet le calcul approché d'intégrales en choisissant une subdivision régulière de pas         xi+1 - xi = (b - a)/n, donc indépendant de i avec une valeur de n "suffisamment grande".

On obtient une succession de rectangles en rose ci-contre, d'où le nom de cette méthode, approchant l'aire sous la courbe,  où ci est choisi ici au "milieu" de [xi ; xi+1]. On calcule :
Sn = h × Σf(ci) , i variant de 0 à n - 1

avec : h = (b - a)/n , xi = a + i.h , ci = (xi+1 + xi)/2 = a + ih + h/2. Le passage à la limite fournit l'intégrale cherchée

En analyse numérique, la méthode des trapèzes est une méthode pour le calcul numérique d'une intégrale ,s'appuyant sur l'interpolation linéaire par intervalles.

## 3.Méthode des trapèzes:

En analyse numérique, la méthode des trapèzes est une méthode pour le calcul numérique d'une intégrale ,s'appuyant sur l'interpolation linéaire par intervalles.
intégrale

####gif

Le principe est d'assimiler la région sous la courbe représentative d'une fonction f définie sur un segment [a , b] à un trapèze et d'en calculer l'aire T :


## 4.Méthode de simpson:

En analyse numérique, la méthode de Simpson, du nom de Thomas Simpson, est une technique de calcul numérique d'une intégrale, c'est-à-dire, le calcul approché de:
intégrale

Cette méthode utilise l'approximation d'ordre 2 de f par un polynôme quadratique P prenant les mêmes valeurs que f aux points d'abscisse a, b et m = (a + b)⁄2. Pour déterminer l'expression de cette parabole (polynôme de degré 2), on utilise l'interpolation lagrangienne. Le résultat peut être mis sous la forme :

formule

Un polynôme étant une fonction très facile à intégrer, on approche l'intégrale de la fonction f sur l'intervalle [a, b], par l'intégrale de P sur ce même intervalle. On a ainsi, la simple formule :


valeur approché

photo

## 5.Méthode des points milieux:


En analyse numérique, la méthode du point médian est une méthode permettant de réaliser le calcul numérique d'une intégrale


###intégrale
Le principe est d'approcher l'intégrale de la fonction f par l'aire d'un rectangle de base le segment [a,b] et de hauteur

f(a+b/2)

ce qui donne : 
r=b-a f(a+b/2)
  
Cette aire est aussi celle du trapèze de base [a,b] et dont le côté opposé est tangent au graphe de f en  c= (a+b)/2 ce qui explique sa relative bonne précision.

taswira 

![test](https://latex.codecogs.com/gif.latex?V.A%20%3D%20%5Cfrac%20%7Bb-a%7Dn%20%5Csum%5Climits%20_%7Bk%3D0%7D%5E%7Bn-1%7D%20f%28t_k%29)

