import numpy as np

m = 500  # masse du planeur (kg)
g = 9.81  # constante gravitationelle (m3 kg−1 s−2) orienté vers le bas
rho = 1.3  # masse volumique de l'air (kg m-3)
S = 16  # surface alaire du planeur (m2)


def Cz(alpha):
    # Le coefficient de portance est représenté par une fonction linéaire si alpha <15
    if alpha <= 15:
        return 0.15 * (alpha + 4)
    # Cz est approximée par un polynome du 2nd degrée si alpha >15
    if alpha > 15:
        y = -1.91025 * alpha ** 2 + 58.3679 * alpha - 442.86
        if y > 0:
            return y  # la fonction ne renvoit que les valeurs positives de Cz
        else:
            return 0  # sinon elle renvoit une portance nulle


def Cx(alpha, aerofrein):
    # Le coefficient de trainée est une fonction quadratique de Cz
    return 0.03 + 0.01 * (Cz(alpha) ** 2) * (1 + 7 * (aerofrein / 100))


def ExecuteEuler(commandePlaneur, planeur, h):
    # méthode d'Euler renvoyant la matrice A à l'instant t+h

    gamma = np.arctan(planeur["Vz"] / planeur["Vy"]) * 180 / np.pi

    # incidence, angle entre l'horizon et Va, dépend des vitesses Vx et Vy
    alpha = (commandePlaneur["Y"] - gamma)

    # angle entre Va et l'axe horizontal de l'avion, dépend de theta défini par l'utilisateur

    normeV = np.sqrt((planeur["Vy"]) ** 2 + (planeur["Vz"]) ** 2)
    # on calcule la vitesse Va comme la norme de (Vx,Vy)

    Ay = (1 / m) * 0.5 * rho * S * (normeV ** 2) * (
        (Cz(alpha) * np.sin((-gamma) / 360 * 2 * np.pi) - Cx(alpha, commandePlaneur["Spoiler"]) * np.cos((-gamma) / 360 * 2 * np.pi)))
    Az = (1 / m) * (0.5 * rho * S * (normeV ** 2) * (
        (Cz(alpha) * np.cos((-gamma) / 360 * 2 * np.pi) + Cx(alpha, commandePlaneur["Spoiler"]) * np.sin(
            (-gamma) / 360 * 2 * np.pi))) - m * g)
    # on calcule les accélérations ay et az d'après les équations du PFD

    planeur = {"Y": planeur["Y"] + h * planeur["Vy"], "Z": planeur["Z"] + h * planeur["Vz"],
               "Vy": planeur["Vy"] + h * Ay, "Vz": planeur["Vz"] + h * Az}
    # On utilise l'approximation d'Euler

    return planeur
    # on obtient la matrice A à l'insant t+h