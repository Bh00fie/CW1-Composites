import numpy as np

#Example done in class using Rule of Mixture and HT Method
#Data given:
S3 = 0.2
S12 = 1
WFibre = 0.6 #Fibre weight Fraction
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

print(Q)

