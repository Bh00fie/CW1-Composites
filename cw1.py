import numpy as np

#Example done in class using Rule of Mixture and HT Method
#Data given:
S3 = 0.2
S12 = 1
WFibre = 0.6 #Fibre weight Fraction
angle = 90
theta = angle*((np.pi)/180)

#Carbon
pFibre = 1870 #km/m^3
EFibre = 310 #GN/m^2
vFibre = 0.23
#Epoxy
pMatrix = 1200 #km/m^3
EMatrix = 2.4 #GN/m^2
vMatrix = 0.33

WMatrix = 1 - WFibre
VFibre = (WFibre/pFibre)/((WFibre/pFibre)+(WMatrix/pMatrix))
VMatrix = 1 - VFibre

#Rule of mixture
#Young Modulus
E1 = EMatrix*VMatrix + EFibre*VFibre

#Shear Modulus
GFibre = EFibre/(2*(1+vFibre))
GMatrix = EMatrix/(2*(1+vMatrix))
G12 = (GFibre*GMatrix)/(GFibre*VMatrix + GMatrix*VFibre)

#Major Poisson Ratio
v12 = vFibre*VFibre + vMatrix*VMatrix

#HT Method
nE = ((EFibre/EMatrix)-1)/((EFibre/EMatrix) + S3)
E2 = EMatrix * ((1+(S3*nE*VFibre))/(1-(nE*VFibre)))

nG = ((GFibre/GMatrix) - 1)/((GFibre/GMatrix) + 1)
G12 = GMatrix * ((1 + S12*nG*VFibre)/(1 - nG*VFibre))

#Minor Poisson Ration
v21 = v12 *(E2/E1)

#Calculating Qmatrix
Q11 = E1 / (1 - v12 * v21)
Q22 = E2 / (1 - v12 * v21)
Q12 = v12 * E2 / (1 - v12 * v21)
Q66 = G12
Q = np.array([[Q11, Q12, 0],
              [Q12, Q22, 0],
              [0, 0, Q66]])

# Calculating Tmatrix
T11 = np.cos(theta) ** 2
T12 = np.sin(theta) ** 2
T13 = 2 * np.sin(theta) * np.cos(theta)
T21 = np.sin(theta) ** 2
T22 = np.cos(theta) ** 2
T23 = -2 * np.sin(theta) * np.cos(theta)
T31 = -np.sin(theta) * np.cos(theta)
T32 = np.sin(theta) * np.cos(theta)
T33 = np.cos(theta) ** 2 - np.sin(theta) ** 2

T = np.array([[T11, T12, T13],
              [T21, T22, T23],
              [T31, T32, T33]])

# Calculate the inverse of T matrix
T_inv = np.linalg.inv(T)

# Calculate the transpose of the inverse matrix
T_inv_transpose = np.transpose(T_inv)