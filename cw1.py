import numpy as np

#Example done in class using Rule of Mixture and HT Method
#Data given:
S3 = 0.2
G12 = 1
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





