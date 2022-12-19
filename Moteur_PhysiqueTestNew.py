import time
import numpy as np
import random as rdm
import matplotlib.pyplot as plt
m=500 #masse du planeur (kg)
g=9.81 #constante gravitationelle (m3 kg−1 s−2) orienté vers le bas
rho = 1.3 #masse volumique de l'air (kg m-3)
S = 16 #surface alaire du planeur (m2)
h = 0.1 #pas d'Euler
AF=0
B =[1,1,1000,25,0,-1]
#matrice initiale contenant [r;theta;z;rp;thetap;zp]

inclinaison=0

def SetTimeStep(t):
    global TimeStep
    global h
    global ExecutionTime
    h = t
    ExecutionTime = time.time() + t



def Vitesse (B):
    v=((B[3]**2)+(B[5]**2)+(B[0]*B[4])**2)**0.5
    return v
def Pente (B):
    pente=float(np.arctan(B[5]/(B[3]**2+((B[0]*B[4])**2))**0.5)*180/np.pi)
    return pente
def Incidence (pente,assiette):
     incidence=float(-pente+assiette)
     return incidence
def Beta (B):
    beta=float(np.arctan((B[0]*B[4])/B[3])*180/np.pi)
    return beta
def Cz(incidence)  :
    cz=0.15*(incidence+4)
    return cz
def Cx (Cz):
    cx=0.03+0.01*(Cz)**2
    return cx
def ExecuteEuler(assiette):
    global B
    global m
    global S
    global g
    global rho
    global h
    global AF
    global inclinaison
    
    
    v= Vitesse(B)
    pente= Pente(B)
    incidence= Incidence(pente,assiette)
    cz=Cz(incidence)
    cx=Cx(cz)
    beta= Beta(B)
    
    r2point=(1/(2*m))*rho*S*(v**2)*(cz*(np.sin(-(pente*np.pi/180))*np.cos(beta*np.pi/180)-np.sin(beta*np.pi/180)*np.sin(inclinaison*np.pi/180))-cx*(np.cos(-(pente*np.pi/180))*np.cos(beta*np.pi/180)))+B[0]*(B[4]**2)
    theta2point=(1/(2*m*B[0]))*rho*S*(v**2)*(cz*((np.sin((inclinaison*np.pi/180))*np.cos(beta*np.pi/180))+np.sin(-(pente*np.pi/180))*np.sin(beta*np.pi/180))-(cx*np.sin(beta*np.pi/180)*np.cos(pente*np.pi/180)))-((2*B[3]*B[4])/(B[0]))
    z2point=-g+(1/(2*m))*rho*S*(v**2)*((cz*np.cos(-(pente*np.pi/180))*np.cos(inclinaison*np.pi/180))+cx*(np.sin(-(pente*np.pi/180))))
    
    
    new_rp=B[3]+h*r2point
    new_thetap=B[4]+h*theta2point
    new_zp=B[5]+h*z2point
    
    new_r=B[0]+h*new_rp
    new_theta=B[1]+h*new_thetap
    new_z=B[2]+h*new_zp
    
    X=B[0]*np.cos((B[1]*180)/np.pi)
    Y=B[0]*np.cos((B[1]*180)/np.pi)
    
    newv=v
    
    newB=[new_r,new_theta,new_z,new_rp,new_thetap,new_zp,newv,X,Y]
    return newB
    
def ascendance(B): #fonction qui calcul les ascendances 
    A=B[5]=B[5]+2 ##vitesse verticale = 1m/s-1 
    return A
    
Mat_z=[]
Mat_x=[]
Mat_y=[] 
matb=[]
u=[]
Q=0
while Q<6000:
    
    test=ExecuteEuler()
    B=test
    
    matb.append(B)
    
    Mat_z.append(test[2])
    x=test[0]*np.cos((test[1]*180)/np.pi)
    Mat_x.append(x)
    
    y=test[0]*np.sin((test[1]*180)/np.pi)
    Mat_y.append(y)
    if -5000<x<5000 and -5000<y<5000:
        ascendance(B)
        matb.append(B)
        Mat_z.append(test[2])
        x=test[0]*np.cos((test[1]*180)/np.pi)
        Mat_x.append(x)
        y=test[0]*np.sin((test[1]*180)/np.pi)
        Mat_y.append(y)
    
    p=test[6]
    u.append(p)
    Q+=1
 
t=np.linspace(0,6000,6000)
plt.plot(t,u,"b")
plt.show()
fig = plt.figure()
ax = plt.axes(projection='3d')
zline = np.array(Mat_z)
xline = np.array(Mat_x)
yline = np.array(Mat_y)
ax.plot3D(xline, yline, zline, 'red')