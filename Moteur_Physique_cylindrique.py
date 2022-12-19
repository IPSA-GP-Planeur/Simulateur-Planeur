import numpy as np

m = 500  # masse du planeur (kg)
g = 9.81  # constante gravitationelle (m3 kg−1 s−2) orienté vers le bas
rho = 1.3  # masse volumique de l'air (kg m-3)
S = 16  # surface alaire du planeur (m2)


def ExecuteEuler(commandePlaneur, planeurCylindrique,
                 h):  # méthode d'Euler renvoyant la matrice A à l'instant t+h
    global m
    global S
    global g
    global rho
    AF = commandePlaneur["Spoiler"]
    inclinaison = commandePlaneur["Y"]
    assiette = commandePlaneur["X"]
    # on recupère les constantes

    v = ((planeurCylindrique["rp"] ** 2) + (planeurCylindrique["zp"] ** 2) + (
                planeurCylindrique["r"] * planeurCylindrique[
            "thetap"]) ** 2) ** 0.5  ##on calcule la vitesse Va comme la norme de (Vx,Vy) /vitesse sol

    pente = float(np.arctan(planeurCylindrique["zp"] / (planeurCylindrique["rp"] ** 2 + (
                (planeurCylindrique["r"] * planeurCylindrique["thetap"]) ** 2)) ** 0.5) * 180 / np.pi)

    incidence = float(-pente + assiette)

    cz = 0.15 * (incidence + 4)  # Le coefficient de portance est représenté par une fonction linéaire

    cx = 0.03 + 0.01 * (cz) ** 2 * (1 + 7 * (AF / 100))  # Le coefficient de trainée est une fonction quadratique de Cz

    beta = float(
        np.arctan((planeurCylindrique["r"] * planeurCylindrique["thetap"]) / planeurCylindrique["rp"]) * 180 / np.pi)

    r2point = (1 / (2 * m)) * rho * S * (v ** 2) * (cz * (
                np.sin(-(pente * np.pi / 180)) * np.cos(beta * np.pi / 180) - np.sin(beta * np.pi / 180) * np.sin(
            inclinaison * np.pi / 180)) - cx * (np.cos(-(pente * np.pi / 180)) * np.cos(beta * np.pi / 180))) + \
              planeurCylindrique["r"] * (planeurCylindrique["thetap"] ** 2)
    theta2point = (1 / (2 * m * planeurCylindrique["r"])) * rho * S * (v ** 2) * (cz * (
                (np.sin((inclinaison * np.pi / 180)) * np.cos(beta * np.pi / 180)) + np.sin(
            -(pente * np.pi / 180)) * np.sin(beta * np.pi / 180)) - (cx * np.sin(beta * np.pi / 180) * np.cos(
        pente * np.pi / 180))) - (
                              (2 * planeurCylindrique["rp"] * planeurCylindrique["thetap"]) / (planeurCylindrique["r"]))
    z2point = -g + (1 / (2 * m)) * rho * S * (v ** 2) * (
                (cz * np.cos(-(pente * np.pi / 180)) * np.cos(inclinaison * np.pi / 180)) + cx * (
            np.sin(-(pente * np.pi / 180))))
    # on calcule r2point theta2point et z2point

    new_rp = planeurCylindrique["rp"] + h * r2point
    new_thetap = planeurCylindrique["thetap"] + h * theta2point
    new_zp = planeurCylindrique["zp"] + h * z2point
    # On utilise l'approximation d'euler pour obtenir rpoin thetapoint et zpoint

    new_r = planeurCylindrique["r"] + h * new_rp
    new_theta = planeurCylindrique["theta"] + h * new_thetap
    new_z = planeurCylindrique["z"] + h * new_zp
    # On utilise l'approximation d'euler pour obtenir r theta et z

    newplaneurCylindrique = {"r": new_r, "theta": new_theta, "z": new_z, "rp": new_rp, "thetap": new_thetap, "zp": new_zp}

    # on crée la nouvelle matrice B à l'instant t+h
    Mat_xyz = []

    x = float(newplaneurCylindrique["r"] * np.cos((newplaneurCylindrique["theta"] * 180) / np.pi))
    Mat_xyz.append(x)

    y = float(newplaneurCylindrique["r"] * np.sin((newplaneurCylindrique["theta"] * 180) / np.pi))
    Mat_xyz.append(y)

    Mat_xyz.append(newplaneurCylindrique["z"])

    newplaneurCartesien = {"Y": float(newplaneurCylindrique["r"] * np.sin((newplaneurCylindrique["theta"] * 180) / np.pi)),
               "Z": newplaneurCylindrique["z"],
               "X": float(newplaneurCylindrique["r"] * np.cos((newplaneurCylindrique["theta"] * 180) / np.pi)),
               "Vy": planeurCylindrique["rp"] + planeurCylindrique["zp"], "Vz": newplaneurCylindrique["zp"],
               "Vx": planeurCylindrique["r"] * planeurCylindrique["thetap"]}

    return newplaneurCylindrique, newplaneurCartesien
