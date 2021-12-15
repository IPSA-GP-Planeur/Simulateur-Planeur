import time
import numpy as np
import Gestionnaire_Evenement as WindowEvent
TimeStep = 0



m=500 #masse du planeur (kg)
g=9.81 #constante gravitationelle (m3 kg−1 s−2) orienté vers le bas
rho = 1.3 #masse volumique de l'air (kg m-3)
S = 16 #surface alaire du planeur (m2)
h = 0.1 #pas d'Euler

A = [0,1000,30,-1]
#matrice initiale contenant [X, Z, Vx, Vy]



def SetTimeStep(t):
    global TimeStep
    global h
    global ExecutionTime
    h = t
    ExecutionTime = time.time() + t



def Cz(alpha)  :
    #Le coefficient de portance est représenté par une fonction linéaire si alpha <15
    if alpha <= 15 :
        return 0.15*(alpha + 4)
    #Cz est approximée par un polynome du 2nd degrée si alpha >15
    if alpha > 15 :
        y = -1.91025*alpha**2 + 58.3679*alpha - 442.86
        if y > 0:
            return y #la fonction ne renvoit que les valeurs positives de Cz
        else :
            return 0 #sinon elle renvoit une portance nulle
        
def Cx(alpha, AF) :
    #Le coefficient de trainée est une fonction quadratique de Cz
    return  0.03+0.01*(Cz(alpha)**2) * (1 + 7*(AF/100))


def ExecuteEuler(theta):
    #méthode d'Euler renvoyant la matrice A à l'instant t+h
    
    global m
    global S
    global g
    global rho
    global h
    global A
    global AF
    #on recupère les constantes
    
    gamma = np.arctan(A[3]/A[2])* 180 /np.pi
    
    #angle entre l'horizon et Va, dépend des vitesses Vx et Vy
    alpha = (theta - gamma) 

    #angle entre Va et l'axe horizontal de l'avion, dépend de theta défini par l'utilisateur
    AF = WindowEvent.af
    #On récupère la valeur des aérofreins définie par l'utilisateur
    
    vx_new = A[2]
    vy_new = A[3]
    #On récupère les valeurs des vitesses Vx et Vy de l'instant t
    
    va = np.sqrt((vx_new)**2 + (vy_new)**2)
    #on calcule la vitesse Va comme la norme de (Vx,Vy)
    
    ax_new = (1/m)*0.5*rho*S*(va**2)*((Cz(alpha)*np.sin((-gamma)/360*2*np.pi)-Cx(alpha, AF)*np.cos((-gamma)/360*2*np.pi)))
    ay_new = (1/m)*(0.5*rho*S*(va**2)*((Cz(alpha)*np.cos((-gamma)/360*2*np.pi)+Cx(alpha, AF)*np.sin((-gamma)/360*2*np.pi)))-m*g)
    #on calcule les accélérations ax et ay d'après les équations du PFD 
    
    A_new = [vx_new, vy_new, ax_new, ay_new]
    #On crée une matrice représentant la dérivé temporelle de A à l'instant t
    
    A = A+h*np.array(A_new)
    #oOn utilise l'approximation d'Euler
    return A 
    #on obtient la matrice A à l'insant t+h







    
    
    
    
    
    
    
    
    